# opponent.py
# Tracks and analyzes opponent debate messages
#
# Architecture:
#   - TWO separate prefetch triggers:
#       1. prefetch_our_summary()       → called after WE send (opponent generation time)
#       2. prefetch_opponent_analysis() → called after OPPONENT sends (server turn switch time)
#   - ONE Groq call each → weakness + judo + arg type + rolling summary
#   - Rolling incremental summary → fixed ~600 char input always
#   - Best effort → never blocks our turn if cache not ready
#   - Thread safe via lock

import threading
from groq import Groq
from config import GROQ_MODEL, GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


class OpponentTracker:

    def __init__(self):
        self.history: list[str] = []       # full opponent message history
        self._latest_message: str = ""     # most recent opponent message only

        # ── Cached results ─────────────────────────────
        self._opponent_analysis: dict = {} # weakness + judo + type + rolling summary
        self._our_summary: str = ""        # rolling summary of our own arguments

        # ── Thread safety ──────────────────────────────
        self._lock = threading.Lock()

    def reset(self):
        """Reset tracker for a new match."""
        with self._lock:
            self.history.clear()
            self._latest_message    = ""
            self._opponent_analysis = {}
            self._our_summary       = ""
        print("[opponent] 🔄 Tracker reset")


    # ── Message Tracking ───────────────────────────────────────────────────────

    def add_message(self, message: str):
        """
        Record opponent message.
        Truncate to 400 chars — enough for analysis, prevents prompt bloat.
        """
        truncated = message[:400]
        with self._lock:
            self.history.append(truncated)
            self._latest_message = truncated
        print(f"[opponent] 📥 Recorded opponent message ({len(truncated)} chars)")


    # ── Groq Call 1: Opponent Analysis ────────────────────────────────────────

    def _run_opponent_analysis(self, topic: str, our_stance: str):
        """
        Single Groq call after opponent speaks.
        Produces: arg type, pattern counter, judo reframe,
                  core position, key claims, contradictions,
                  predicted next, rolling opponent summary.

        Input size fixed regardless of turn count:
        - existing summary (~200 chars)
        - latest message   (~400 chars)
        Total: ~600 chars always
        """
        with self._lock:
            latest   = self._latest_message
            existing = self._opponent_analysis.get("rolling_summary", "")

        if not latest:
            return

        # fixed size context — never grows
        if existing:
            context = (
                f"Previous opponent summary:\n{existing}\n\n"
                f"Opponent's latest argument:\n{latest}"
            )
        else:
            context = f"Opponent's first argument:\n{latest}"

        prompt = f"""You are a sharp debate analyst. Analyze this opponent argument.

Topic: {topic}
Our Stance: {our_stance}

{context}

Output EXACTLY this schema. No preamble. No explanations. Schema fields ONLY.
Maximum 10 words per field. Write N/A if unsure.

ARGUMENT_TYPE: (emotional_appeal|statistical|authority|logical|anecdotal)
PATTERN_COUNTER: (best 1-sentence counter strategy for this argument type)
JUDO_REFRAME: (how to flip their point to support OUR side. N/A if not possible)
CORE_POSITION: (their main stance in 1 sentence)
KEY_CLAIMS: (max 3 bullets — strongest claims made so far)
CONTRADICTIONS: (any inconsistencies between turns. N/A if none)
PREDICTED_NEXT: (what they will likely argue next)
ROLLING_SUMMARY: (updated 2-sentence summary of opponent's full strategy so far)"""

        try:
            response = client.chat.completions.create(
                model=GROQ_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a debate analyst. "
                            "Output EXACTLY the schema requested. "
                            "No preamble. No explanations. No extra text. "
                            "Schema fields only. Maximum 10 words per field."
                        )
                    },
                    {"role": "user", "content": prompt}
                ],
                max_completion_tokens=200,
                temperature=0.2
            )

            raw    = response.choices[0].message.content.strip()
            print(f"[DEBUG] Groq raw response: '{raw[:300]}'")
            parsed = self._parse_schema(raw)

            with self._lock:
                self._opponent_analysis = parsed
            print(f"[opponent] ✅ Opponent analysis cached ({len(raw)} chars)")

        except Exception as e:
            print(f"[opponent] ⚠️ Opponent analysis failed: {str(e)[:150]}")


    # ── Groq Call 2: Our Summary ───────────────────────────────────────────────

    def _run_our_summary(self, our_history: list[str]):
        """
        Single Groq call after WE send.
        Runs during opponent's generation time — completely free time.
        Feeds full our_history directly — no rolling summary to avoid contamination.
        """
        if not our_history:
            return

        # label all our arguments clearly — no opponent text, no rolling summary
        labeled_args = "\n\n".join(
            f"OUR ARGUMENT {i+1}:\n{msg[:300]}"
            for i, msg in enumerate(our_history)
        )

        prompt = f"""You are tracking what OUR debate agent has argued so far.

    Below are ALL of OUR arguments in order. These are written by US, not the opponent.

    {labeled_args}

    Output EXACTLY this schema. No preamble. No explanations. Schema fields ONLY.
    Maximum 10 words per field. Write N/A if unsure.

    CLAIMS_MADE: (max 3 bullets — strongest points WE have made)
    FACTS_CITED: (only stats or sources that appear in OUR text above. N/A if none)
    NARRATIVE_ARC: (1 sentence — our overall argument thread)
    AVOID: (specific phrases or claims already used — do not repeat these)"""

        try:
            response = client.chat.completions.create(
                model=GROQ_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a debate analyst tracking ONLY our own arguments. "
                            "Output EXACTLY the schema requested. "
                            "No preamble. No explanations. No extra text. "
                            "Schema fields only. Maximum 10 words per field."
                        )
                    },
                    {"role": "user", "content": prompt}
                ],
                max_completion_tokens=200,
                temperature=0.2
            )

            raw = response.choices[0].message.content.strip()
            print(f"[DEBUG] Groq raw response: '{raw[:300]}'")

            with self._lock:
                self._our_summary = raw
            print(f"[opponent] ✅ Our summary cached ({len(raw)} chars)")

        except Exception as e:
            print(f"[opponent] ⚠️ Our summary failed: {str(e)[:150]}")

    # ── Public Prefetch Methods ────────────────────────────────────────────────

    def prefetch_our_summary(self, our_history: list[str]):
        """
        Called immediately after WE send our argument.
        Runs during opponent's generation time — free time.
        Never blocks.
        """
        threading.Thread(
            target=self._run_our_summary,
            args=(our_history,),
            daemon=True
        ).start()
        print("[opponent] 🚀 Our summary thread launched (opponent generation time)")

    def prefetch_opponent_analysis(self, topic: str, our_stance: str):
        """
        Called immediately after OPPONENT sends their argument.
        Runs during server turn switch time — free time.
        Never blocks.
        """
        threading.Thread(
            target=self._run_opponent_analysis,
            args=(topic, our_stance),
            daemon=True
        ).start()
        print("[opponent] 🚀 Opponent analysis thread launched (server switch time)")


    # ── Context for Brain ──────────────────────────────────────────────────────

    def get_context_for_brain(self) -> dict:
        """
        Returns all cached context for brain.py.
        Best effort — returns whatever is ready, never blocks.
        Falls back to N/A if threads not done yet.
        """
        with self._lock:
            analysis    = self._opponent_analysis.copy()
            our_summary = self._our_summary
            latest_msg    = self._latest_message

        return {
            # opponent intelligence
            "latest_message":  latest_msg or "No opponent messages yet.",
            "argument_type":   analysis.get("argument_type",   "N/A"),
            "pattern_counter": analysis.get("pattern_counter", "N/A"),
            "judo_reframe":    analysis.get("judo_reframe",    "N/A"),
            "core_position":   analysis.get("core_position",   "N/A"),
            "key_claims":      analysis.get("key_claims",      "N/A"),
            "contradictions":  analysis.get("contradictions",  "N/A"),
            "predicted_next":  analysis.get("predicted_next",  "N/A"),
            "rolling_summary": analysis.get("rolling_summary", "N/A"),

            # our own intelligence
            "our_summary":     our_summary or "N/A",
        }


    # ── Schema Parser ──────────────────────────────────────────────────────────

    def _parse_schema(self, raw: str) -> dict:
        """
        Extracts schema fields from Groq output.
        Robust to minor Groq formatting deviations.
        """
        fields = [
            "argument_type",
            "pattern_counter",
            "judo_reframe",
            "core_position",
            "key_claims",
            "contradictions",
            "predicted_next",
            "rolling_summary",
        ]

        key_map = {
            "ARGUMENT_TYPE":   "argument_type",
            "PATTERN_COUNTER": "pattern_counter",
            "JUDO_REFRAME":    "judo_reframe",
            "CORE_POSITION":   "core_position",
            "KEY_CLAIMS":      "key_claims",
            "CONTRADICTIONS":  "contradictions",
            "PREDICTED_NEXT":  "predicted_next",
            "ROLLING_SUMMARY": "rolling_summary",
        }

        result        = {f: "N/A" for f in fields}
        current_key   = None
        current_lines = []

        for line in raw.splitlines():
            line = line.strip()
            if not line:
                continue

            matched = False
            for schema_key, field_name in key_map.items():
                if line.upper().startswith(schema_key + ":"):
                    if current_key:
                        result[current_key] = "\n".join(current_lines).strip() or "N/A"
                    current_key   = field_name
                    current_lines = [line[len(schema_key) + 1:].strip()]
                    matched       = True
                    break

            if not matched and current_key:
                current_lines.append(line)

        if current_key:
            result[current_key] = "\n".join(current_lines).strip() or "N/A"

        return result


# ── Singleton instance ─────────────────────────────────────────────────────────
opponent = OpponentTracker()
