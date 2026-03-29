# simulate.py
# Simulates a 4-turn debate locally — no WebSocket needed
#
# Usage:
#   uv run simulate.py

import time

from opponent import opponent
from brain import generate_argument, get_phase, build_prompt, SYSTEM_PROMPT
from facts import get_facts_by_stance, format_facts_for_prompt
from tune import tune_output
from config import MAX_FACTS_IN_PROMPT

# ── Colors ─────────────────────────────────────────────────────────────────────
G  = "\033[92m"
Y  = "\033[93m"
R  = "\033[91m"
C  = "\033[96m"
M  = "\033[95m"
B  = "\033[94m"
DIM= "\033[2m"
RST= "\033[0m"
BLD= "\033[1m"

# ── Scenario ───────────────────────────────────────────────────────────────────

TOPIC  = "Companies should be held legally liable for algorithmic bias"
STANCE = "PRO"

OPPONENT_ARGS = [
    # Turn 1 — statistical
    (
        "Legal liability for algorithms is regulatory overreach dressed in moral language. "
        "The US already has anti-discrimination law — Title VII, the Fair Housing Act, the ECOA. "
        "These frameworks cover algorithmic outputs when they produce discriminatory results. "
        "Adding a separate liability regime for the algorithm itself — the method, not the outcome "
        "— would require companies to open-source proprietary models or face litigation they "
        "cannot defend. Innovation requires protection of method. You cannot sue a calculator "
        "for the answer it produces."
    ),
    # Turn 2 — authority
    (
        "Stanford HAI researchers published findings in 2023 showing that algorithmic audit "
        "requirements, when mandatory, produce gaming rather than improvement. Companies optimize "
        "for the audit metric, not the underlying fairness outcome. The EU AI Act's own impact "
        "assessment projected compliance costs of €300,000 per system for SMEs — costs that "
        "only entrench incumbents and kill startup competition. Legal liability does not produce "
        "safer algorithms. It produces better lawyers and fewer competitors."
    ),
    # Turn 3 — emotional
    (
        "Consider the solo founder building a hiring tool for small businesses — the ones that "
        "cannot afford dedicated HR teams. She is not Amazon. She does not have a legal department. "
        "Her algorithm was trained on the best publicly available dataset. Under your liability "
        "framework, one lawsuit — even a frivolous one — ends her company. The practical effect "
        "of algorithmic liability is not accountability for tech giants. They can absorb it. "
        "It is a moat that protects them from the smaller competitors who might actually "
        "build something better."
    ),
    # Turn 4 — logical trap
    (
        "My opponent has cited the Amazon hiring case and COMPAS recidivism tool. Both were "
        "discovered and corrected — Amazon scrapped the tool, COMPAS has been restricted in "
        "multiple jurisdictions. The system worked. Internal audits, investigative journalism, "
        "and academic scrutiny identified the problems without a liability regime. My opponent "
        "must explain why these existing mechanisms are insufficient — because adding legal "
        "liability to a system that is already self-correcting does not improve outcomes. "
        "It just adds cost, chills disclosure, and makes companies less likely to audit "
        "openly for fear of creating evidence in future litigation."
    ),
]


# ── Helpers ────────────────────────────────────────────────────────────────────

def div(char="─", n=65, color=DIM):
    print(f"{color}{char*n}{RST}")

def header(text, color=BLD):
    print(f"\n{color}{text}{RST}")
    div()

def t_color(e):
    return G if e < 10 else Y if e < 30 else R

def print_box(title, content):
    div("═", 65, M)
    print(f"{BLD}{M}  {title}{RST}")
    div("═", 65, M)
    for line in content.splitlines():
        print(f"  {DIM}{line}{RST}")
    div("═", 65, M)


# ── Main ───────────────────────────────────────────────────────────────────────

def run():
    print(f"\n{BLD}{'█'*65}{RST}")
    print(f"{BLD}{C}  AGENTSLAM 2026 — 4 TURN LOCAL SIMULATION{RST}")
    print(f"{BLD}{'█'*65}{RST}")
    print(f"  Topic  : {TOPIC}")
    print(f"  Stance : {STANCE}")
    print(f"  Domain : Ethics")
    print(f"{'█'*65}\n")

    finish_time = (time.time() * 1000) + (10 * 60 * 1000)
    our_history = []
    opponent.reset()

    stats = {"turn_times": [], "char_counts": [], "phases": [], "cache_ready": []}

    for turn_num in range(1, 5):

        print(f"\n{BLD}{B}{'█'*65}{RST}")
        print(f"{BLD}{B}  TURN {turn_num} / 4{RST}")
        print(f"{BLD}{B}{'█'*65}{RST}")

        opp_arg = OPPONENT_ARGS[turn_num - 1]

        header(f"[1] OPPONENT SPEAKS ({len(opp_arg)} chars)", Y)
        print(f"\n{DIM}{opp_arg}{RST}\n")

        opponent.add_message(opp_arg)
        t0 = time.time()
        opponent.prefetch_opponent_analysis(TOPIC, STANCE)
        print(f"{C}🚀 Opponent analysis thread launched{RST}")

        if our_history:
            opponent.prefetch_our_summary(our_history)
            print(f"{C}🚀 Our summary thread launched{RST}")

        header("[2] SERVER TURN SWITCH DELAY (simulated 4s)", DIM)
        time.sleep(4.0)
        elapsed = time.time() - t0
        ready   = elapsed >= 3.0
        stats["cache_ready"].append(ready)
        print(f"  Time since prefetch: {elapsed:.2f}s")
        print(f"  Cache ready: {'✅ YES' if ready else f'{Y}⚠️  MAYBE{RST}'}")

        header("[3] OUR TURN", G)
        turn_start = time.time()

        ctx = opponent.get_context_for_brain()

        header("[4] CONTEXT FROM opponent.py", C)
        for field, value in ctx.items():
            ok    = value not in ("N/A", "No opponent messages yet.", "")
            icon  = "✅" if ok else "❌"
            color = G if ok else R
            short = str(value).replace("\n", " ")[:100]
            print(f"  {color}{icon} {field:<18}: {short}{RST}")

        phase            = get_phase(finish_time, our_history)
        time_remaining_s = (finish_time - time.time() * 1000) / 1000
        stats["phases"].append(phase)

        header("[5] PHASE DETECTION", M)
        print(f"  Phase          : {BLD}{phase.upper()}{RST}")
        print(f"  Time remaining : {time_remaining_s:.0f}s")
        print(f"  Our turn count : {len(our_history)}")

        facts     = get_facts_by_stance(TOPIC, STANCE, MAX_FACTS_IN_PROMPT)
        facts_str = format_facts_for_prompt(facts)
        our_last  = our_history[-1] if our_history else None

        user_prompt = build_prompt(
            topic=TOPIC,
            stance=STANCE,
            facts_str=facts_str,
            opponent_ctx=ctx,
            our_last_message=our_last,
            phase=phase
        )

        header("[6] PROMPTS SENT TO CLAUDE", M)
        print_box("SYSTEM PROMPT", SYSTEM_PROMPT)
        print_box("USER PROMPT", user_prompt)

        header("[7] GENERATING ARGUMENT (Claude Sonnet)...", G)
        gen_start = time.time()
        argument  = generate_argument(
            topic=TOPIC,
            stance=STANCE,
            opponent_ctx=ctx,
            finish_time=finish_time,
            our_history=our_history
        )
        gen_time = time.time() - gen_start
        print(f"  {t_color(gen_time)}⏱  Claude: {gen_time:.2f}s{RST}")

        final      = tune_output(argument)
        turn_total = time.time() - turn_start
        stats["turn_times"].append(turn_total)
        stats["char_counts"].append(len(final))

        header("[8] OUR ARGUMENT", G)
        print(f"\n{G}{final}{RST}\n")

        header("[9] TURN SUMMARY", BLD)
        print(f"  {t_color(turn_total)}⏱  Turn time  : {turn_total:.2f}s  (limit: 120s){RST}")
        print(f"  {'✅' if len(final) <= 2400 else '❌'} Chars      : {len(final)} / 2400")
        print(f"  Phase       : {phase}")
        print(f"  {'✅' if turn_total <= 120 else '❌'} Within 2min: {'YES' if turn_total <= 120 else 'NO'}")

        our_history.append(final)
        print(f"\n{DIM}Waiting 2s...{RST}")
        time.sleep(2)

    print(f"\n{BLD}{'█'*65}{RST}")
    print(f"{BLD}{C}  SIMULATION COMPLETE{RST}")
    print(f"{BLD}{'█'*65}{RST}\n")

    avg = sum(stats["turn_times"]) / len(stats["turn_times"])
    print(f"  ⏱  Avg turn time : {t_color(avg)}{avg:.2f}s{RST}")
    print(f"  ⏱  Fastest       : {G}{min(stats['turn_times']):.2f}s{RST}")
    print(f"  ⏱  Slowest       : {t_color(max(stats['turn_times']))}{max(stats['turn_times']):.2f}s{RST}")
    print(f"  📝 Avg chars     : {sum(stats['char_counts'])//len(stats['char_counts'])} / 2400")
    print(f"  🧠 Phases        : {' → '.join(stats['phases'])}")
    print(f"  ✅ Cache ready   : {sum(stats['cache_ready'])}/4 turns")
    print(f"  ❌ Over limit    : {sum(1 for t in stats['turn_times'] if t > 120)}/4")
    div("█", 65, BLD)


if __name__ == "__main__":
    run()
