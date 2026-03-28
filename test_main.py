# test_main.py
# Simulates all server WebSocket messages locally
# Tests every message type from the spec without needing real server

import json
import time
from unittest.mock import MagicMock

# ── Setup ──────────────────────────────────────────────────────────────────────

# Mock WebSocket before importing main
ws = MagicMock()
ws.send = MagicMock()
ws.close = MagicMock()

# Import main handlers
from main import on_open, on_message, on_close, reset_match_state

import os
from dotenv import load_dotenv
load_dotenv()
MY_TEAM = os.getenv("MY_TEAM_NAME", "my-team")
OPP_TEAM = "opponent-team"

# ── Test Helpers ───────────────────────────────────────────────────────────────

passed = []
failed = []

def feed(msg: dict):
    """Feed a fake server message into on_message"""
    on_message(ws, json.dumps(msg))

def check(test_name: str, condition: bool, detail: str = ""):
    if condition:
        passed.append(test_name)
        print(f"  ✓ {test_name}")
    else:
        failed.append(test_name)
        print(f"  ✗ {test_name}" + (f" — {detail}" if detail else ""))

def header(title: str):
    print(f"\n{'═'*55}")
    print(f"  {title}")
    print(f"{'═'*55}")

# ── Tests ──────────────────────────────────────────────────────────────────────

header("TEST 1: Connection Open")
on_open(ws)
check("on_open runs without crash", True)

# ──────────────────────────────────────────────────────

header("TEST 2: Welcome Message")
feed({
    "type": "welcome",
    "from": "system",
    "data": {"message": f"Welcome {MY_TEAM} to AgentSlam!"}
})
check("welcome handled without crash", True)

# ──────────────────────────────────────────────────────

header("TEST 3: Match Update (sets finish_time)")
finish_time_ms = int((time.time() + 570) * 1000)  # 9.5 min from now
feed({
    "type": "match-update",
    "from": "system",
    "data": {
        "message": "Match started! It's opponent-team's turn.",
        "finishTime": finish_time_ms
    }
})
from main import finish_time as ft
check(
    "finish_time set correctly",
    ft == finish_time_ms,
    f"got {ft}, expected {finish_time_ms}"
)

# ──────────────────────────────────────────────────────

header("TEST 4: Match State — Opponent's Turn (should NOT send)")
ws.send.reset_mock()
feed({
    "type": "match-state",
    "from": "system",
    "data": {
        "team1": OPP_TEAM,
        "team2": MY_TEAM,
        "topic": "AI should replace human judges in courts",
        "description": "Debate on AI in judiciary",
        "round": "Round 1",
        "finishTime": finish_time_ms,
        "pros": OPP_TEAM,
        "cons": MY_TEAM,
        "turn": OPP_TEAM,        # ← opponent's turn
        "status": "started",
        "remainingTime": 500000
    }
})
check(
    "ws.send NOT called on opponent turn",
    not ws.send.called,
    "ws.send was called when it shouldn't be"
)
from main import my_stance
check(
    f"Stance set correctly (should be CON)",
    my_stance == "CON",
    f"got {my_stance}"
)

# ──────────────────────────────────────────────────────

header("TEST 5: Opponent Debate Message")
ws.send.reset_mock()
feed({
    "type": "debate-message",
    "from": OPP_TEAM,
    "data": {
        "message": "AI lacks moral reasoning required for judicial decisions. "
                   "Justice demands human empathy that no algorithm can replicate."
    }
})
check("opponent message handled without crash", True)

# ──────────────────────────────────────────────────────

header("TEST 6: Match State — OUR Turn (should send)")
ws.send.reset_mock()
print(f"  [triggering our turn as {MY_TEAM}...]")
feed({
    "type": "match-state",
    "from": "system",
    "data": {
        "team1": OPP_TEAM,
        "team2": MY_TEAM,
        "topic": "AI should replace human judges in courts",
        "description": "Debate on AI in judiciary",
        "round": "Round 1",
        "finishTime": finish_time_ms,
        "pros": OPP_TEAM,
        "cons": MY_TEAM,
        "turn": MY_TEAM,         # ← our turn
        "status": "started",
        "remainingTime": 500000
    }
})

check(
    "ws.send called on our turn",
    ws.send.called,
    "ws.send was NOT called — check take_turn()"
)

if ws.send.called:
    sent_raw     = ws.send.call_args[0][0]
    sent_parsed  = json.loads(sent_raw)
    msg_type     = sent_parsed.get("type")
    msg_data     = sent_parsed.get("data", {})
    msg_text     = msg_data.get("message", "")
    msg_bytes    = len(msg_text.encode('utf-8'))

    check(
        'type field is "debate-message"',
        msg_type == "debate-message",
        f"got '{msg_type}'"
    )
    check(
        "data.message exists and is a string",
        isinstance(msg_text, str) and len(msg_text) > 0,
        "message is empty or not a string"
    )
    check(
        f"message under 2400 bytes (got {msg_bytes})",
        msg_bytes <= 2400,
        f"{msg_bytes} bytes exceeds limit"
    )
    check(
        "payload is valid JSON",
        True  # if we got here json.loads worked
    )
    print(f"\n  Preview: {msg_text[:120]}...")

# ──────────────────────────────────────────────────────

header("TEST 7: Our Message Broadcast Confirmed")
feed({
    "type": "debate-message",
    "from": MY_TEAM,             # ← our own message echoed back
    "data": {"message": "Our argument confirmed by server"}
})
check("own message echo handled without crash", True)

# ──────────────────────────────────────────────────────

header("TEST 8: Match Paused")
feed({
    "type": "match-paused",
    "from": "system",
    "data": {
        "timeRemaining": 300000,
        "message": "Match has been paused."
    }
})
from main import match_paused
check(
    "match_paused set to True",
    match_paused == True,
    f"got {match_paused}"
)

# ──────────────────────────────────────────────────────

header("TEST 9: Match Resumed")
new_finish_time = int((time.time() + 400) * 1000)
feed({
    "type": "match-resumed",
    "from": "system",
    "data": {
        "finishTime": new_finish_time,
        "message": f"Match resumed! It's {OPP_TEAM}'s turn."
    }
})
from main import match_paused as mp2, finish_time as ft2
check(
    "match_paused set to False after resume",
    mp2 == False,
    f"got {mp2}"
)
check(
    "finish_time updated after resume",
    ft2 == new_finish_time,
    f"got {ft2}, expected {new_finish_time}"
)

# ──────────────────────────────────────────────────────

header("TEST 10: Previous Messages (reconnect scenario)")
feed({
    "type": "previous-message",
    "from": "system",
    "data": {
        "message": "Match is already live! Here are previous conversations.",
        "conversations": [
            {
                "team": OPP_TEAM,
                "message": "First opponent argument from before reconnect",
                "timestamp": "2026-03-28T10:00:00.000Z"
            },
            {
                "team": MY_TEAM,
                "message": "Our first argument from before reconnect",
                "timestamp": "2026-03-28T10:01:00.000Z"
            }
        ]
    }
})
from main import our_history
check(
    "our_history restored after reconnect",
    len(our_history) > 0,
    f"our_history is empty"
)
check("previous messages handled without crash", True)

# ──────────────────────────────────────────────────────

header("TEST 11: Error Messages")

errors = [
    "Too many messages!",
    "It's not your turn! Please wait for your turn.",
    "Message exceeds maximum allowed size of 2500 bytes.",
    "Match is not currently accepting message.",
    "Invalid message format.",
    "Cannot send debate messages when match is not live.",
]

for err_msg in errors:
    try:
        feed({
            "type": "error",
            "from": "system",
            "data": {"message": err_msg}
        })
        check(f"error handled: '{err_msg[:40]}...'", True)
    except Exception as e:
        check(f"error handled: '{err_msg[:40]}...'", False, str(e))

# ──────────────────────────────────────────────────────

header("TEST 12: Info Messages")
feed({
    "type": "info",
    "from": "system",
    "data": {"message": "acknowledged"}
})
check("info/acknowledged handled", True)

# ──────────────────────────────────────────────────────

header("TEST 13: Match Finish")
ws.close.reset_mock()
feed({
    "type": "match-finish",
    "from": "system",
    "data": {"message": "The match has ended!"}
})
check(
    "ws.close called on match finish",
    ws.close.called,
    "ws.close was NOT called"
)
from main import match_live
check(
    "match_live set to False",
    match_live == False,
    f"got {match_live}"
)

# ──────────────────────────────────────────────────────

header("TEST 14: on_close Handler")
on_close(ws, 1000, "Normal closure")
check("on_close runs without crash", True)

# ── Final Summary ──────────────────────────────────────────────────────────────

print(f"\n{'═'*55}")
print(f"  RESULTS")
print(f"{'═'*55}")
print(f"  Total:  {len(passed) + len(failed)}")
print(f"  ✓ Passed: {len(passed)}")
print(f"  ✗ Failed: {len(failed)}")

if failed:
    print(f"\n  Failed tests:")
    for f in failed:
        print(f"    ✗ {f}")
    print(f"\n  Fix these before match day.")
else:
    print(f"\n  ALL TESTS PASSED ✓")
    print(f"  Your WebSocket handler is ready for match day.")