import re
from config import PAYLOAD_CHAR_LIMIT


# ── Basic Cleaning ─────────────────────────────────────

def clean_text(text: str) -> str:
    """Remove extra whitespace and weird formatting."""
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text


# ── Trim to Limit ──────────────────────────────────────

def trim_to_limit(text: str, limit: int = PAYLOAD_CHAR_LIMIT) -> str:
    """
    Ensures message stays within character limit.
    Trims at last sentence boundary before limit.
    """
    if len(text) <= limit:
        return text

    trimmed    = text[:limit]
    last_punct = max(trimmed.rfind("."), trimmed.rfind("!"), trimmed.rfind("?"))

    if last_punct > 0:
        return trimmed[:last_punct + 1]

    return trimmed


# ── Main Tune Function ─────────────────────────────────

def tune_output(raw_text: str) -> str:
    text = clean_text(raw_text)
    text = trim_to_limit(text)
    return text


# ── Sanity Test ────────────────────────────────────────

if __name__ == "__main__":
    sample = """
    AI is transforming the world. AI is transforming the world.
    The evidence clearly supports our position on this matter.
    """
    print("=== RAW ===")
    print(sample)
    print("\n=== TUNED ===")
    print(tune_output(sample))