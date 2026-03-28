# brain.py
# Core reasoning engine using Anthropic (Claude Sonnet)

import time
from anthropic import Anthropic
from config import (
    ANTHROPIC_API_KEY,
    ANTHROPIC_MODEL,
    MAX_FACTS_IN_PROMPT,
    BRAIN_MAX_TOKENS,
    CLOSING_TRIGGER,
)
from facts import get_facts_by_stance, format_facts_for_prompt

client = Anthropic(api_key=ANTHROPIC_API_KEY)


# ── Phase Detection ────────────────────────────────────────────────────────────

# def get_phase(finish_time: float, our_history: list) -> str:
#     """
#     Detect debate phase using finish_time and our_history.
#     - opening  → we haven't spoken yet
#     - closing  → less than 3 mins remaining
#     - rebuttal → everything else
#     """
#     time_remaining_ms = finish_time - (time.time() * 1000)

#     if time_remaining_ms <= CLOSING_TRIGGER * 1000:  # CLOSING_TRIGGER is in seconds
#         return "closing"

#     if not our_history:
#         return "opening"

#     return "rebuttal"

def get_phase(finish_time: float, our_history: list) -> str:
    """
    Detect debate phase using finish_time and our_history.
    - opening  → we haven't spoken yet
    - closing  → less than 3 mins remaining OR turn 6+
    - defense  → even turns mid-game
    - rebuttal → odd turns mid-game
    """
    turn = len(our_history)  # turn count = how many times we've spoken

    # ── Opening ───────────────────────────────────────
    if turn == 0:
        return "opening"

    # ── Time-based closing (last 3 minutes) ───────────
    if finish_time:
        time_remaining_ms = finish_time - (time.time() * 1000)
        time_remaining_s  = time_remaining_ms / 1000
        if time_remaining_s <= CLOSING_TRIGGER:
            return "closing"

    # ── Turn-based closing (turn 6+) ──────────────────
    # Safety net: match moves faster than expected
    if turn >= 4:
        return "closing"

    # ── Mid-game: alternate rebuttal / defense ────────
    if turn % 2 == 1:
        return "rebuttal"

    return "defense"

# ── Prompt Builder ─────────────────────────────────────────────────────────────

def build_prompt(
    topic: str,
    stance: str,
    facts_str: str,
    opponent_ctx: dict,
    our_last_message: str | None,
    phase: str
) -> str:
    """
    Builds structured prompt for Claude.
    Uses last 2 opponent messages + weakness analysis.
    """

    last_two_text = opponent_ctx.get("last_two_text") or "No opponent messages yet."
    weaknesses    = opponent_ctx.get("weaknesses")    or "No weakness analysis available."

    # only show our last message in rebuttal/closing to avoid contradiction
    our_context = ""
    if our_last_message and phase != "opening":
        our_context = f"\nYOUR LAST ARGUMENT (do not contradict this):\n{our_last_message}"

    phase_instructions = {
        "opening": (
            "- Introduce your stance clearly and confidently.\n"
            "- Present 2 strong arguments with evidence.\n"
            "- Set the tone — you are the stronger side.\n"
            "- End with a bold claim."
        ),
        "rebuttal": (
            "- Directly address opponent's latest argument.\n"
            "- Exploit the weaknesses identified above.\n"
            "- Counter with evidence and logic.\n"
            "- Reinforce your original stance.\n"
            "- Do NOT repeat your previous points word for word."
        ),
        "defense": (
            "- Acknowledge opponent's strongest point in one sentence — shows confidence.\n"
            "- Then dismantle it: explain exactly why it fails under scrutiny.\n"
            "- Reinforce your original argument with a NEW angle not yet used.\n"
            "- Make clear your core position is unshaken.\n"
            "- Do NOT repeat your previous points word for word."
        ),
        "closing": (
            "- This is your FINAL argument — make it count.\n"
            "- Summarize your 2 strongest points briefly.\n"
            "- Expose the biggest flaw in opponent's case.\n"
            "- End with a powerful, memorable statement.\n"
            "- Do NOT introduce new arguments."
        )
    }

    return f"""You are an elite AI debater competing in AgentSlam 2026.

TOPIC: {topic}
YOUR STANCE: {stance}
PHASE: {phase.upper()}

VERIFIED FACTS YOU CAN USE:
{facts_str}

OPPONENT'S RECENT ARGUMENTS:
{last_two_text}

OPPONENT'S WEAKNESSES:
{weaknesses}
{our_context}

PHASE INSTRUCTIONS:
{phase_instructions[phase]}

GLOBAL RULES:
- Stay under 2000 characters.
- Use 1-2 facts with sources — no fabricated statistics.
- Sound confident and human, not robotic.
- Output ONLY the argument text, nothing else.
- Do not use markdown formatting, bold text, or headers. Write in natural flowing prose like a real debater speaking.
"""


# ── Claude Call ────────────────────────────────────────────────────────────────

def call_claude(prompt: str) -> str:
    """Call Claude Sonnet and return generated argument."""
    try:
        response = client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=BRAIN_MAX_TOKENS,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.content[0].text.strip()

    except Exception as e:
        print(f"[brain] ⚠️ Claude error: {str(e)[:200]}")
        # fallback — safe generic response that won't break the match
        return (
            "The evidence overwhelmingly supports our position. "
            "Our opponent has failed to address the core logical foundation "
            "of our argument, and their claims remain unsubstantiated. "
            "We stand firmly by our stance."
        )


# ── Main Entry Point ───────────────────────────────────────────────────────────

def generate_argument(
    topic: str,
    stance: str,
    opponent_ctx: dict,
    finish_time: float,
    our_history: list
) -> str:
    """
    Main entry point called by take_turn() in main.py.

    Args:
        topic:        debate topic from match-state
        stance:       "PRO" or "CON"
        opponent_ctx: from opponent.get_context_for_brain()
        finish_time:  Unix timestamp in ms from server
        our_history:  list of our past messages (full, for phase detection)
    """

    # ── Phase Detection ────────────────────────────────
    phase = get_phase(finish_time, our_history)
    print(f"[brain] 🧠 Phase: {phase} | Time remaining: {(finish_time - time.time()*1000)/1000:.0f}s")

    # ── Facts ──────────────────────────────────────────
    facts = get_facts_by_stance(topic, stance, MAX_FACTS_IN_PROMPT)
    facts_str = format_facts_for_prompt(facts)

    # ── Our Last Message ───────────────────────────────
    # only pass last message to avoid contradiction
    our_last_message = our_history[-1] if our_history else None

    # ── Build Prompt ───────────────────────────────────
    prompt = build_prompt(
        topic=topic,
        stance=stance,
        facts_str=facts_str,
        opponent_ctx=opponent_ctx,
        our_last_message=our_last_message,
        phase=phase
    )

    # ── Generate ───────────────────────────────────────
    argument = call_claude(prompt)
    print(f"[brain] ✅ Generated {phase} argument ({len(argument)} chars)")

    return argument
