# main.py
# Orchestrates WebSocket communication + debate flow

import websocket

from config import (
    WS_MATCH_URL,
    WS_SANDBOX_URL,
    AUTH_TOKEN,
    MY_TEAM_NAME,
)
from validator import (
    parse_incoming,
    get_message_type,
    extract_debate_message,
    extract_previous_messages,
    is_match_finished,
    build_payload
)
from opponent import opponent
from brain import generate_argument
from tune import tune_output


# ── Global State ───────────────────────────────────────────────────────────────

connected    = False
finish_time  = None
topic        = ""
my_stance    = ""
match_live   = False
match_paused = False
our_history  = []        # our sent messages, for brain.py context


def reset_match_state():
    global connected, finish_time, topic
    global my_stance, match_live, match_paused, our_history

    finish_time  = None
    topic        = ""
    my_stance    = ""
    match_live   = False
    match_paused = False
    our_history  = []
    opponent.reset()
    print("[main] 🔄 Match state reset")


# ── WebSocket Callbacks ────────────────────────────────────────────────────────

def on_open(ws):
    global connected
    connected = True
    reset_match_state()
    print("[main] 🔌 WebSocket connected — waiting for server welcome...")


def on_message(ws, message):
    global finish_time, topic, my_stance
    global match_live, match_paused, our_history

    parsed = parse_incoming(message)
    if not parsed:
        return

    msg_type = get_message_type(parsed)

    # ── WELCOME ──────────────────────────────────────────
    if msg_type == "welcome":
        print("[main] ✅ Server welcomed us — ready for match")

    # ── MATCH UPDATE ─────────────────────────────────────
    elif msg_type == "match-update":
        data = parsed.get("data", {})
        finish_time = data.get("finishTime")   # set once here
        print(f"[main] 🟢 Match update | finishTime: {finish_time}")

    # ── MATCH STATE ──────────────────────────────────────
    elif msg_type == "match-state":
        data = parsed.get("data", {})

        # extract topic
        topic = data.get("topic", topic)

        # set stance once
        if not my_stance:
            pros_team = data.get("pros", "")
            my_stance = "PRO" if pros_team == MY_TEAM_NAME else "CON"
            print(f"[main] 🎭 Our stance: {my_stance}")

        # mark match live only from status field
        status = data.get("status", "")
        if status == "started":
            match_live   = True
            match_paused = False

        # take turn if conditions met
        if match_live and not match_paused:
            turn = data.get("turn", "")
            if turn == MY_TEAM_NAME:
                print("[main] 🎯 It's our turn!")
                take_turn(ws)

    # ── OPPONENT MESSAGE ──────────────────────────────────
    elif msg_type == "debate-message":
        sender = parsed.get("from", "")
        msg    = extract_debate_message(parsed)

        if msg and sender != MY_TEAM_NAME:
            print(f"[main] 📥 Opponent: {msg[:100]}...")
            opponent.add_message(msg)
        elif sender == MY_TEAM_NAME:
            print("[main] ✅ Our message broadcast confirmed")

    # ── PREVIOUS HISTORY ─────────────────────────────────
    elif msg_type == "previous-message":
        conversations = extract_previous_messages(parsed)
        if conversations:
            print(f"[main] 📜 Loading {len(conversations)} previous messages...")
            for conv in conversations:
                msg  = conv.get("message", "")
                team = conv.get("team", "")
                if not msg:
                    continue
                if team != MY_TEAM_NAME:
                    opponent.add_message(msg)
                else:
                    our_history.append(msg)

    # ── MATCH PAUSED ─────────────────────────────────────
    elif msg_type == "match-paused":
        match_paused = True
        print("[main] ⏸️ Match paused")

    # ── MATCH RESUMED ────────────────────────────────────
    elif msg_type == "match-resumed":
        data         = parsed.get("data", {})
        finish_time  = data.get("finishTime", finish_time)  # update with new finishTime
        match_paused = False
        match_live   = True
        print(f"[main] ▶️ Match resumed | finishTime: {finish_time}")

    # ── MATCH FINISHED ───────────────────────────────────
    elif msg_type == "match-finish" or is_match_finished(parsed):
        match_live = False
        print("[main] 🏁 Match finished!")
        ws.close()

    # ── SERVER INFO ───────────────────────────────────────
    elif msg_type == "info":
        info_msg = parsed.get("data", {}).get("message", "")
        print(f"[main] ℹ️ Info: {info_msg}")
        if "expired" in info_msg.lower():
            print("[main] ⏰ Session expired")
            ws.close()

    # ── ERROR ─────────────────────────────────────────────

    elif msg_type == "sandbox-message":
        msg = parsed.get("data", {}).get("message", "")
        print(f"[main] 🧪 Sandbox: {msg}")

    #not handled
    elif msg_type == "error":
        err       = parsed.get("data", {}).get("message", "")
        err_lower = err.lower()
        print(f"[main] ❌ Server error: {err}")

        if "too many messages" in err_lower or "rate limit" in err_lower:
            print("[main] ⏳ Rate limited — skipping turn")
        elif "not your turn" in err_lower:
            print("[main] ⛔ Not our turn — ignoring")
        elif "too large" in err_lower:
            print("[main] ⚠️ Message too long — trimming next attempt")
        elif "not live" in err_lower:
            print("[main] ⚠️ Match not live — waiting")
        elif "invalid" in err_lower:
            print("[main] ⚠️ Invalid payload format")

    else:
        print(f"[main] ℹ️ Ignored: {msg_type}")


def on_error(ws, error):
    print(f"[main] ⚠️ WebSocket error: {error}")


def on_close(ws, close_status_code, close_msg):
    global connected
    connected = False
    print(f"[main] 🔴 Disconnected | code: {close_status_code} | msg: {close_msg}")


# ── Core Turn Logic ────────────────────────────────────────────────────────────

def take_turn(ws):
    global our_history

    print("[main] 🚀 Generating response...")
    
    if finish_time is None:
        print("[main] ⚠️ finish_time not set yet — skipping turn")
        return

    # get opponent context
    opponent_ctx = opponent.get_context_for_brain(
        topic=topic,
        our_stance=my_stance,
        run_llm=len(opponent.history) > 0  # only if opponent has spoken
    )

    # generate argument
    raw_output = generate_argument(
        topic=topic,
        stance=my_stance,
        opponent_ctx=opponent_ctx,
        finish_time=finish_time,
        our_history=our_history
    )

    # tune output
    final_output = tune_output(raw_output)
    print(f"[main] 🧾 Output ready ({len(final_output)} chars)")

    # validate + build payload
    payload = build_payload(final_output)
    if not payload:
        print("[main] ❌ Payload invalid — skipping turn")
        return

    # send
    try:
        ws.send(payload)
        our_history.append(final_output)  # save only on successful send
        print(f"[main] 📤 Sent ({len(final_output)} chars)")
    except Exception as e:
        print(f"[main] ❌ Send failed: {e}")


# ── Entry Point ────────────────────────────────────────────────────────────────

def run(sandbox: bool = False):
    url = WS_SANDBOX_URL if sandbox else WS_MATCH_URL

    if not url:
        print(f"[main] ❌ {'WS_SANDBOX_URL' if sandbox else 'WS_MATCH_URL'} not set in .env")
        return

    headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}
    print(f"[main] 🔌 Connecting to {'sandbox' if sandbox else 'match'} server...")

    ws = websocket.WebSocketApp(
        url,
        header=headers,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )

    ws.run_forever()


if __name__ == "__main__":
    import sys
    sandbox_mode = "--sandbox" in sys.argv
    run(sandbox=sandbox_mode)
