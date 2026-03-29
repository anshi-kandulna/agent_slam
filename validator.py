# validator.py
# Validates outgoing messages and builds WebSocket payloads
# Also validates incoming server messages

import json
from config import PAYLOAD_CHAR_LIMIT


# ── Outgoing validation ────────────────────────────────────────────────────────

def validate_outgoing(message: str) -> tuple[bool, str]:
    """
    Validates a debate message string before sending.
    Returns (is_valid, error_reason).
    """
    if not isinstance(message, str):
        return False, "Message must be a string"

    if not message.strip():
        return False, "Message is empty"

    if len(message) > PAYLOAD_CHAR_LIMIT:
        return False, f"Message too large: {len(message)} chars (limit: {PAYLOAD_CHAR_LIMIT})"

    return True, ""


def build_payload(message: str) -> str | None:
    """
    Builds outgoing debate message payload.
    Required format per spec:
    {
        "type": "debate-message",
        "data": { "message": "..." }
    }
    Returns JSON string if valid, None if invalid.
    """
    is_valid, reason = validate_outgoing(message)
    if not is_valid:
        print(f"[validator] ❌ Invalid outgoing message: {reason}")
        return None

    payload = {
        "type": "debate-message",
        "data": {
            "message": message
        }
    }
    return json.dumps(payload, ensure_ascii=False)


# ── Incoming message parsing ───────────────────────────────────────────────────

def parse_incoming(raw: str) -> dict | None:
    """Parses raw incoming WebSocket message into dict."""
    try:
        data = json.loads(raw)
        if not isinstance(data, dict):
            print(f"[validator] ⚠️ Unexpected message shape: {raw}")
            return None
        return data
    except json.JSONDecodeError as e:
        print(f"[validator] ⚠️ JSON decode error: {e}")
        return None


def get_message_type(parsed: dict) -> str:
    """Extracts message type. Returns 'unknown' if missing."""
    return parsed.get("type", "unknown")


def is_my_turn(parsed: dict, my_team: str) -> bool:
    return parsed.get("data", {}).get("turn", "") == my_team


def is_error(parsed: dict) -> bool:
    return get_message_type(parsed) == "error"


def is_match_live(parsed: dict) -> bool:
    return parsed.get("data", {}).get("status", "") == "started"


def extract_debate_message(parsed: dict) -> str | None:
    if get_message_type(parsed) != "debate-message":
        return None
    return parsed.get("data", {}).get("message", None)


def extract_error_text(parsed: dict) -> str:
    return parsed.get("data", {}).get("message", "Unknown error")


def extract_previous_messages(parsed: dict) -> list | None:
    if get_message_type(parsed) != "previous-message":
        return None
    return parsed.get("data", {}).get("conversations", [])


def is_match_finished(parsed: dict) -> bool:
    return get_message_type(parsed) == "match-finish"


# ── Sanity check ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Outgoing Tests ===")
    print(build_payload("AI is transforming the financial sector."))
    print(build_payload(""))
    print(build_payload("x" * 2600))

    print("\n=== Sandbox Tests ===")

    print("\n=== Incoming Tests ===")
    raw_turn = json.dumps({
        "type": "match-state",
        "from": "system",
        "data": {"turn": "team1", "status": "started"}
    })
    parsed = parse_incoming(raw_turn)
    print(f"Is my turn (team1): {is_my_turn(parsed, 'team1')}")
    print(f"Is my turn (team2): {is_my_turn(parsed, 'team2')}")
    print(f"Is match live:      {is_match_live(parsed)}")

    raw_error = json.dumps({
        "type": "error",
        "from": "system",
        "data": {"message": "It's not your turn! Please wait for your turn."}
    })
    parsed_err = parse_incoming(raw_error)
    print(f"\nIs error:   {is_error(parsed_err)}")
    print(f"Error text: {extract_error_text(parsed_err)}")

    print("\n=== Previous Messages Test ===")
    raw_prev = json.dumps({
        "type": "previous-message",
        "from": "system",
        "data": {
            "message": "Match is already live!",
            "conversations": [
                {"team": "team1", "message": "Opening argument here", "timestamp": "2026-03-18T10:20:00.000Z"}
            ]
        }
    })
    parsed_prev = parse_incoming(raw_prev)
    print(f"Previous messages: {extract_previous_messages(parsed_prev)}")

    print("\n=== Match Finish Test ===")
    raw_finish = json.dumps({
        "type": "match-finish",
        "from": "system",
        "data": {"message": "The match has ended!"}
    })
    print(f"Is finished: {is_match_finished(parse_incoming(raw_finish))}")