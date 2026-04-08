# brain.py
# Core reasoning engine using Anthropic (Claude Sonnet)
# Changes:
#   [1] Removed premature turn-based closing trigger (turn >= 4)
#   [3] Passes full argument history to Claude (compressed) to prevent repetition
#   [4] Split static persona into system prompt, dynamic content into user prompt

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


# ── Static System Prompt ───────────────────────────────────────────────────────
# [Change 4] Persona + hard rules are static → sent as system prompt.
# Anthropic can cache this, and Claude internalises the persona before seeing
# any turn content — leading to more focused, on-brand responses.

SYSTEM_PROMPT = """You are an elite AI debater competing in AgentSlam 2026.

SCORING CRITERIA:
- Persuasiveness (40%): Use rhetoric, vivid evidence, and compelling narrative.
- Logic (30%): Stay consistent. Name logical fallacies explicitly when you spot them.
- Agility (10%): Mirror the opponent's exact words, then dismantle them.

ABSOLUTE RULES:
- Never fabricate statistics — only use facts from the VERIFIED FACTS section.
- Never concede. Never say "you make a valid point" or "I agree".
- If the opponent makes a strong point — reframe it to support YOUR side.
- No markdown, no bullet points — flowing prose only, like a real debater speaking.
- Output ONLY the argument text, nothing else. No preamble, no labels.
- Stay under 2400 characters."""


# ── Phase Detection ────────────────────────────────────────────────────────────
# [Change 1] Removed the `turn >= 4 → closing` early trigger.
# That block was causing the agent to stop attacking from the middle of the
# debate onward. Now only the time-based trigger (last 3 minutes) fires closing.

def get_phase(finish_time: float, our_history: list) -> str:
    """
    Detect debate phase using finish_time and our_history.
    - opening  → we haven't spoken yet
    - closing  → less than 3 mins remaining (time-based only)
    - rebuttal → odd turns mid-game
    - defense  → even turns mid-game
    """
    turn = len(our_history)

    if turn == 0:
        return "opening"

    if finish_time:
        time_remaining_s = (finish_time - time.time() * 1000) / 1000
        if time_remaining_s <= CLOSING_TRIGGER:
            return "closing"

    if turn % 2 == 1:
        return "rebuttal"

    return "defense"


# ── Prompt Builder ─────────────────────────────────────────────────────────────

def build_user_prompt(
    topic: str,
    stance: str,
    facts_str: str,
    opponent_ctx: dict,
    our_summary: str | None,
    phase: str
) -> str:
    last_two_text = opponent_ctx.get("last_two_text") or "No opponent messages yet."
    weaknesses    = opponent_ctx.get("weaknesses")    or "No weakness analysis available."

    our_context = ""
    if our_summary and phase != "opening":
        our_context = f"\nYOUR PREVIOUS ARGUMENTS (do NOT repeat these points):\n{our_summary}"

    phase_instructions = {
        "opening": (
            "- Introduce your stance clearly and confidently.\n"
            "- Present 2 strong arguments with evidence.\n"
            "- Set the tone — you are the stronger side.\n"
            "- End with a bold claim."
        ),
        "rebuttal": (
            "- Directly address the opponent's latest argument.\n"
            "- Exploit the weaknesses identified above.\n"
            "- Counter with evidence and logic.\n"
            "- Reinforce your original stance.\n"
            "- Do NOT repeat your previous points word for word."
        ),
        "defense": (
            "- Acknowledge the opponent's strongest point in one sentence — shows confidence.\n"
            "- Then dismantle it: explain exactly why it fails under scrutiny.\n"
            "- Reinforce your original argument with a NEW angle not yet used.\n"
            "- Make clear your core position is unshaken.\n"
            "- Do NOT repeat your previous points word for word."
        ),
        "closing": (
            "- This is your FINAL argument — make it count.\n"
            "- Summarize your 2 strongest points briefly.\n"
            "- Expose the biggest flaw in the opponent's case.\n"
            "- End with a powerful, memorable statement.\n"
            "- Do NOT introduce new arguments."
        )
    }

    return f"""TOPIC: {topic}
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
{phase_instructions[phase]}"""


# ── Claude Call ────────────────────────────────────────────────────────────────

def call_claude(user_prompt: str) -> str:
    try:
        response = client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=BRAIN_MAX_TOKENS,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_prompt}]
        )
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
    phase = get_phase(finish_time, our_history)
    time_remaining = (finish_time - time.time() * 1000) / 1000
    print(f"[brain] 🧠 Phase: {phase} | Turn: {len(our_history)} | Time remaining: {time_remaining:.0f}s")

    facts = get_facts_by_stance(topic, stance, MAX_FACTS_IN_PROMPT)
    facts_str = format_facts_for_prompt(facts)

    # [Change 3] Compress full history so Claude knows what ground is covered
    our_summary = None
    if our_history:
        our_summary = "\n".join(
            f"Turn {i+1}: {msg[:120]}{'...' if len(msg) > 120 else ''}"
            for i, msg in enumerate(our_history)
        )

    user_prompt = build_user_prompt(
        topic=topic,
        stance=stance,
        facts_str=facts_str,
        opponent_ctx=opponent_ctx,
        our_summary=our_summary,
        phase=phase
    )

    argument = call_claude(user_prompt)
    print(f"[brain] ✅ Generated {phase} argument ({len(argument)} chars)")
    return argument
