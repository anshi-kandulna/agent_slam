# brain.py
# Core reasoning engine using Claude Sonnet
#
# Changes from previous version:
#   - Fixed KeyError: "mid" → "rebuttal"
#   - System/user prompt split
#   - Scoring matrix in system prompt
#   - Updated to use new opponent_ctx fields from opponent.py

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


# ── System Prompt (static — sent every call) ───────────────────────────────────

SYSTEM_PROMPT = """You are an elite AI debater competing in AgentSlam 2026.

You are being scored by an AI judge on these exact criteria:
- Persuasiveness (40%): Use rhetoric, vivid evidence, and compelling narrative. Make the judge feel your argument.
- Logic (30%): Keep arguments internally consistent. Name opponent fallacies explicitly by type.
- Agility (10%): Directly address opponent's exact words. Mirror their argument back, then dismantle it.

ABSOLUTE RULES:
- Never fabricate statistics, percentages, dates, or research — hallucination penalty is severe
- Only cite facts provided to you in the VERIFIED FACTS section
- If no facts available — argue with pure logic, no invented numbers
- Never concede to opponent. Never say "you make a valid point" or "admittedly" or "I agree"
- If opponent makes a strong point — reframe it to support YOUR side instead
- No markdown, no bullet points, no headers — flowing prose only
- Output ONLY the argument text, nothing else
- Stay under 2000 characters
- Sound like a confident human debater, not a robot"""


# ── Phase Detection ────────────────────────────────────────────────────────────

def get_phase(finish_time: float, our_history: list) -> str:
    """
    Detect debate phase:
    - opening → first turn
    - closing → last 3 minutes
    - mid     → everything else
    """
    turn = len(our_history)

    # opening — always first
    if turn == 0:
        return "opening"

    # time-based closing — last 3 minutes
    if finish_time:
        time_remaining_s = (finish_time - (time.time() * 1000)) / 1000
        if time_remaining_s <= CLOSING_TRIGGER:
            return "closing"

    return "mid"


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
    Builds user prompt for Claude.
    System prompt is passed separately in call_claude().
    """

    # ── Opponent context ───────────────────────────────
    latest_message  = opponent_ctx.get("latest_message")  or "No opponent messages yet."
    argument_type   = opponent_ctx.get("argument_type")   or "N/A"
    pattern_counter = opponent_ctx.get("pattern_counter") or "N/A"
    judo_reframe    = opponent_ctx.get("judo_reframe")    or "N/A"
    contradictions  = opponent_ctx.get("contradictions")  or "N/A"
    predicted_next  = opponent_ctx.get("predicted_next")  or "N/A"
    rolling_summary = opponent_ctx.get("rolling_summary") or "N/A"

    # ── Our context ────────────────────────────────────
    our_summary = opponent_ctx.get("our_summary") or "N/A"

    our_context = ""
    if our_last_message and phase != "opening":
        our_context = f"\nYOUR LAST ARGUMENT (do not contradict this):\n{our_last_message}\n"

    # ── Phase instructions ─────────────────────────────
    phase_instructions = {
        "opening": (
            "- Introduce your stance clearly and confidently.\n"
            "- Present 2 strong arguments with evidence from VERIFIED FACTS.\n"
            "- Set the tone — you are the stronger side.\n"
            "- End with a bold, memorable claim."
        ),
        "mid": (
            "- Directly address opponent's LATEST ARGUMENT — use their exact words.\n"
            "- Use the PATTERN COUNTER if applicable.\n"
            "- Use the JUDO REFRAME if available — flip their point to our advantage.\n"
            "- Name any logical fallacy explicitly.\n"
            "- Exploit any CONTRADICTIONS found in their arguments.\n"
            "- Reinforce your original stance with a NEW angle not yet used.\n"
            "- Do NOT repeat claims listed in YOUR DEBATE HISTORY."
        ),
        "closing": (
            "- This is your FINAL argument — make it count.\n"
            "- Summarize your 2 strongest points briefly.\n"
            "- Expose the biggest flaw in opponent's overall strategy.\n"
            "- End with a powerful, memorable statement the judge will remember.\n"
            "- Do NOT introduce new arguments."
        )
    }

    return f"""TOPIC: {topic}
YOUR STANCE: {stance}
PHASE: {phase.upper()}

VERIFIED FACTS YOU CAN USE:
{facts_str}

OPPONENT INTELLIGENCE:
- Latest argument: {latest_message}
- Argument type: {argument_type}
- Counter strategy: {pattern_counter}
- Judo reframe (flip their point): {judo_reframe}
- Their contradictions to exploit: {contradictions}
- They will likely argue next: {predicted_next}
- Their overall strategy: {rolling_summary}

YOUR DEBATE HISTORY:
{our_summary}
{our_context}
PHASE INSTRUCTIONS:
{phase_instructions[phase]}"""


# ── Claude Call ────────────────────────────────────────────────────────────────

def call_claude(prompt: str) -> str:
    """Call Claude Sonnet with system/user split and return argument."""
    try:
        response = client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=BRAIN_MAX_TOKENS,
            system=SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        # print(prompt)
        return response.content[0].text.strip()

    except Exception as e:
        print(f"[brain] ⚠️ Claude error: {str(e)[:200]}")
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
    """

    # ── Phase Detection ────────────────────────────────
    phase = get_phase(finish_time, our_history)
    time_remaining = (finish_time - time.time() * 1000) / 1000
    print(f"[brain] 🧠 Phase: {phase} | Time remaining: {time_remaining:.0f}s")

    # ── Facts ──────────────────────────────────────────
    facts     = get_facts_by_stance(topic, stance, MAX_FACTS_IN_PROMPT)
    facts_str = format_facts_for_prompt(facts)

    # ── Our Last Message ───────────────────────────────
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
