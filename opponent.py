# opponent.py
# Tracks and analyzes opponent debate messages
# Change [2]: Added prefetch_analysis() + _cached_analysis so Groq runs
#             in the background the moment the opponent sends a message,
#             instead of blocking our turn generation.

import os
from groq import Groq
from config import GROQ_MODEL, GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


class OpponentTracker:
    """
    Tracks opponent's last 2 messages and detects weaknesses via Groq.
    Weakness analysis is now prefetched in a background thread as soon as
    the opponent message arrives, so it's ready by the time our turn starts.
    """

    def __init__(self):
        self.history: list[str] = []
        self._cached_analysis: str | None = None   # [Change 2] prefetch cache

    def reset(self):
        self.history.clear()
        self._cached_analysis = None               # [Change 2] clear on reset

    # ── Message Tracking ───────────────────────────────────────────────────────

    def add_message(self, message: str):
        """Record opponent message. Keep only last 2."""
        self.history.append(message)
        if len(self.history) > 2:
            self.history.pop(0)
        # Invalidate cache — new message means old analysis is stale
        self._cached_analysis = None              # [Change 2]
        print(f"[opponent] 📥 Recorded opponent message ({len(message)} chars)")

    def get_last_two_text(self) -> str:
        if not self.history:
            return "No opponent messages yet."
        lines = []
        for i, msg in enumerate(self.history):
            turn_label = "Previous" if i == 0 and len(self.history) == 2 else "Latest"
            lines.append(f"{turn_label}: {msg}")
        return "\n\n".join(lines)

    # ── LLM Weakness Detection ─────────────────────────────────────────────────

    def detect_weaknesses(self, topic: str, our_stance: str) -> str:
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

    # ── [Change 2] Prefetch Method ─────────────────────────────────────────────
    # Called from main.py in a background daemon thread the moment an opponent
    # message arrives. Stores result in _cached_analysis so get_context_for_brain
    # can return it instantly when our turn fires.

    def prefetch_analysis(self, topic: str, our_stance: str):
        """
        Run Groq weakness analysis in the background during the opponent's turn.
        Result is cached so our turn starts with analysis already ready.
        """
        print("[opponent] 🔄 Prefetching weakness analysis in background...")
        self._cached_analysis = self.detect_weaknesses(topic, our_stance)
        print("[opponent] ✅ Prefetch complete — analysis cached")

    # ── Context for Brain ──────────────────────────────────────────────────────
    # [Change 2] Returns cached analysis if available; only calls Groq live
    # as a fallback if prefetch didn't run (e.g. very fast turn switch).

    def get_context_for_brain(self, topic: str, our_stance: str, run_llm: bool = True) -> dict:
        weaknesses = None

        if self.history:
            if self._cached_analysis:
                # Prefetch already ran — use the cached result instantly
                print("[opponent] ⚡ Using prefetched analysis")
                weaknesses = self._cached_analysis
            elif run_llm:
                # Fallback: prefetch didn't complete in time, run synchronously
                print("[opponent] ⏳ Prefetch not ready — running Groq synchronously")
                weaknesses = self.detect_weaknesses(topic, our_stance)

        return {
            "last_two_text": self.get_last_two_text(),
            "weaknesses": weaknesses or "No analysis available."
        }


# ── Singleton instance ─────────────────────────────────────────────────────────
opponent = OpponentTracker()
