import os
from dotenv import load_dotenv

load_dotenv()

# ── AI Providers ───────────────────────────────────────
# Groq → opponent analysis (fast)
# Anthropic → brain/argument generation (persuasive)

GROQ_MODEL        = "llama-3.3-70b-versatile"
ANTHROPIC_MODEL   = "claude-sonnet-4-6"  

GROQ_API_KEY      = os.getenv("GROQ_API_KEY", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

# ── Competition ────────────────────────────────────────
WS_MATCH_URL      = os.getenv("WS_MATCH_URL", "")
WS_SANDBOX_URL    = os.getenv("WS_SANDBOX_URL", "")
AUTH_TOKEN        = os.getenv("AUTH_TOKEN", "")
MY_TEAM_NAME      = os.getenv("MY_TEAM_NAME", "")
MY_STANCE         = os.getenv("MY_STANCE", "PRO")   # ADD: PRO or CON, set per match

# ── Timing ─────────────────────────────────────────────
RESPONSE_TIMEOUT  = 85      # seconds — inside 2 min rule
MIN_CALL_GAP      = 12      # seconds — Groq free tier safe
MATCH_DURATION = 600   # 10 min safety buffer
OPENING_TURNS     = 1       # ADD: turn 1 is always opening statement
CLOSING_TURN_MIN  = 6       # ADD: closing can trigger after turn 6 too
CLOSING_TRIGGER = 180   # seconds — trigger closing in last 3 minutes

# ── Payload ────────────────────────────────────────────
PAYLOAD_CHAR_LIMIT = 2500   # conservative under 2500 server limit

# ── Brain ──────────────────────────────────────────────
MAX_FACTS_IN_PROMPT = 4     # ADD: keep prompts lean for speed
MAX_HISTORY_TURNS   = 6     # ADD: cap history sent to Claude (token control)
BRAIN_MAX_TOKENS    = 600   # ADD: keeps response under char limit safely