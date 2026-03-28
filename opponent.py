# opponent.py
# Tracks and analyzes opponent debate messages
# Uses last 2 turns + Groq LLM for weakness detection

import os
from groq import Groq
from config import GROQ_MODEL, GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


class OpponentTracker:
    """
    Tracks opponent's last 2 messages and detects weaknesses via Groq.
    Minimal context, zero extra latency.
    """

    def __init__(self):
        self.history: list[str] = []
        # each entry is just the message string

    def reset(self):
        """Reset tracker for a new match."""
        self.history.clear()

    # ── Message Tracking ───────────────────────────────────────────────────────

    def add_message(self, message: str):
        """Record opponent message. Keep only last 2."""
        self.history.append(message)
        if len(self.history) > 2:
            self.history.pop(0)  # drop oldest, keep last 2
        print(f"[opponent] 📥 Recorded opponent message ({len(message)} chars)")

    def get_last_two_text(self) -> str:
        """Returns last 2 opponent messages as formatted string."""
        if not self.history:
            return "No opponent messages yet."
        lines = []
        for i, msg in enumerate(self.history):
            turn_label = "Previous" if i == 0 and len(self.history) == 2 else "Latest"
            lines.append(f"{turn_label}: {msg}")
        return "\n\n".join(lines)

    # ── LLM Weakness Detection ─────────────────────────────────────────────────

    def detect_weaknesses(self, topic: str, our_stance: str) -> str:
        """
        Uses Groq to analyze opponent's last 2 messages and detect weaknesses.
        Fast and concise — 3 bullet points max.
        """
        if not self.history:
            return "No opponent messages to analyze yet."

        prompt = f"""You are a debate coach analyzing an opponent's arguments.

Debate Topic: {topic}
Our Stance: {our_stance}

Opponent's recent arguments:
{self.get_last_two_text()}

Identify weaknesses in 3 bullet points max:
1. Logical fallacies or flawed reasoning
2. Unsupported or unverifiable claims
3. Contradictions or weak points to exploit

Be sharp and concise. This feeds directly into our rebuttal."""

        try:
            response = client.chat.completions.create(
                model=GROQ_MODEL,
                messages=[
                    {"role": "system", "content": "You are a sharp debate analyst. Be brief and precise."},
                    {"role": "user", "content": prompt}
                ],
                reasoning_effort="high",
                max_completion_tokens=300,
                temperature=0.3
            )
            analysis = response.choices[0].message.content.strip()
            print(f"[opponent] 🔍 Weakness analysis complete ({len(analysis)} chars)")
            return analysis

        except Exception as e:
            print(f"[opponent] ⚠️ Weakness detection failed: {str(e)[:200]}")
            return "Could not analyze weaknesses. Proceed with general rebuttal."

    # ── Context for Brain ──────────────────────────────────────────────────────

    def get_context_for_brain(self, topic: str, our_stance: str, run_llm: bool = True) -> dict:
        """
        Returns structured context for brain.py.
        - last_two_text: last 2 opponent messages formatted
        - weaknesses: Groq analysis (only if run_llm=True and history exists)
        """
        context = {
            "last_two_text": self.get_last_two_text(),
            "weaknesses": None
        }

        if run_llm and self.history:
            context["weaknesses"] = self.detect_weaknesses(topic, our_stance)

        return context


# ── Singleton instance ─────────────────────────────────────────────────────────
opponent = OpponentTracker()
