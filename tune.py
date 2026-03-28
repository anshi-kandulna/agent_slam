# 1. Enforce hard limits
# Keep under PAYLOAD_CHAR_LIMIT
# ✅ 2. Improve persuasion
# Remove fluff
# Strengthen tone
# Add structure (if missing)
# ✅ 3. Fix common LLM issues
# Repetition
# Weak openings
# Robotic phrasing
# Missing structure


# tune.py
# Post-processing layer to refine LLM output before sending

import re
from config import PAYLOAD_CHAR_LIMIT


# ── Basic Cleaning ─────────────────────────────────────

def clean_text(text: str) -> str:
    """
    Remove extra whitespace, newlines, and weird formatting.
    """
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)  # collapse spaces
    return text


# ── Remove Weak Phrases ────────────────────────────────

WEAK_PHRASES = [
    "I think",
    "it seems",
    "it is important to note",
    "in conclusion",
    "overall",
    "arguably",
]

def remove_weak_phrases(text: str) -> str:
    """
    Removes low-confidence / filler phrases.
    """
    for phrase in WEAK_PHRASES:
        text = re.sub(rf"\b{phrase}\b[:,]?\s*", "", text, flags=re.IGNORECASE)
    return text


# ── Deduplicate Sentences ──────────────────────────────

def remove_repetition(text: str) -> str:
    """
    Removes repeated sentences (common LLM issue).
    """
    sentences = re.split(r'(?<=[.!?]) +', text)
    seen = set()
    result = []

    for s in sentences:
        s_clean = s.strip().lower()
        if s_clean not in seen:
            seen.add(s_clean)
            result.append(s.strip())

    return " ".join(result)


# ── Strengthen Tone ────────────────────────────────────

def strengthen_tone(text: str) -> str:
    """
    Makes tone more assertive.
    """
    replacements = {
        "this suggests": "this clearly shows",
        "this indicates": "this proves",
        "could be": "is",
        "may be": "is",
        "might": "will"
    }

    for k, v in replacements.items():
        text = re.sub(rf"\b{k}\b", v, text, flags=re.IGNORECASE)

    return text


# ── Add Light Structure ────────────────────────────────

def add_structure(text: str) -> str:
    """
    Adds minimal structure for readability if missing.
    """
    # If already structured, skip
    if "\n" in text or "1." in text:
        return text

    sentences = re.split(r'(?<=[.!?]) +', text)

    if len(sentences) >= 3:
        # Break into 2–3 lines max
        chunk_size = len(sentences) // 2
        part1 = " ".join(sentences[:chunk_size])
        part2 = " ".join(sentences[chunk_size:])
        return f"{part1}\n{part2}"

    return text


# ── Trim to Limit ──────────────────────────────────────

def trim_to_limit(text: str, limit: int = PAYLOAD_CHAR_LIMIT) -> str:
    """
    Ensures message stays within character limit safely.
    """
    if len(text) <= limit:
        return text

    # Smart trim: cut at last sentence before limit
    trimmed = text[:limit]
    last_punct = max(trimmed.rfind("."), trimmed.rfind("!"), trimmed.rfind("?"))

    if last_punct > 0:
        return trimmed[:last_punct + 1]

    return trimmed


# ── Main Tune Function ─────────────────────────────────

def tune_output(raw_text: str) -> str:
    """
    Main pipeline to refine LLM output.
    Order matters.
    """

    text = clean_text(raw_text)
    text = remove_weak_phrases(text)
    text = remove_repetition(text)
    text = strengthen_tone(text)
    text = add_structure(text)
    text = trim_to_limit(text)

    return text


# ── Sanity Test ────────────────────────────────────────

if __name__ == "__main__":
    sample = """
    In conclusion, I think AI might be useful. AI might be useful.
    It is important to note that this suggests improvements in healthcare.
    """

    print("=== RAW ===")
    print(sample)

    print("\n=== TUNED ===")
    print(tune_output(sample))