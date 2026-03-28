# debate_simulator.py

import time
from brain import generate_argument
from tune import tune_output
from opponent import opponent
from groq_agent import generate_groq_argument


# ── CONFIG ─────────────────────────────────────────────

TOPIC = "AI should replace human financial analysts"
SONNET_STANCE = "PRO"
GROQ_STANCE = "CON"

MAX_TURNS = 10   # simulate ~15 min (can increase to 12–14)


# ── RUN DEBATE ─────────────────────────────────────────

def run_debate():
    print(f"\n🔥 DEBATE START")
    print(f"Topic: {TOPIC}")
    print(f"Sonnet: {SONNET_STANCE} | Groq: {GROQ_STANCE}\n")

    start_time = time.time()
    turn = 1

    last_message = "No previous argument."

    debate_log = []

    while turn <= MAX_TURNS:
        print(f"\n================ TURN {turn} ================\n")

        # ── SONNET TURN ─────────────────────────
        opponent.add_message(last_message)

        ctx = opponent.get_context_for_brain(
            topic=TOPIC,
            our_stance=SONNET_STANCE,
            run_llm=False   # faster for simulation
        )

        sonnet_raw = generate_argument(
            topic=TOPIC,
            stance=SONNET_STANCE,
            opponent_ctx=ctx,
            turn_count=turn,
            start_time=start_time
        )

        sonnet_final = tune_output(sonnet_raw)

        print(f"🧠 SONNET:\n{sonnet_final}\n")

        debate_log.append(("SONNET", sonnet_final))

        # ── GROQ TURN ───────────────────────────
        groq_msg = generate_groq_argument(
            topic=TOPIC,
            stance=GROQ_STANCE,
            opponent_msg=sonnet_final,
            turn=turn
        )

        print(f"⚔️ GROQ:\n{groq_msg}\n")

        debate_log.append(("GROQ", groq_msg))

        # next loop
        last_message = groq_msg
        turn += 1

        time.sleep(1)  # avoid rate issues

    print("\n🏁 DEBATE END\n")

    return debate_log


# ── SAVE LOG ───────────────────────────────────────────

def save_log(log):
    with open("debate_log.txt", "w", encoding="utf-8") as f:
        for speaker, msg in log:
            f.write(f"{speaker}:\n{msg}\n\n")


if __name__ == "__main__":
    log = run_debate()
    save_log(log)
    print("📄 Debate saved to debate_log.txt")