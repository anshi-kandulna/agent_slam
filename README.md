# AgentSlam 2026 — Debate Agent

An AI-powered debate agent built for AgentSlam 2026. Uses Claude Sonnet for argument generation and Groq Llama for real-time opponent analysis.

---

## Architecture

```
main.py        — WebSocket orchestration + debate flow
brain.py       — Argument generation (Claude Sonnet)
opponent.py    — Opponent tracking + prefetch analysis (Groq)
facts.py       — Verified facts database with domain/stance retrieval
validator.py   — Payload validation + message parsing
tune.py        — Output cleaning and character limit enforcement
config.py      — All settings and environment variables
simulate.py    — Local 4-turn simulation (no WebSocket needed)
```

### How it works

1. WebSocket connects to match server
2. On opponent message → Groq analyzes argument type, counter strategy, judo reframe, contradictions, predicted next move — all in a background thread
3. On our turn → Claude receives full opponent intelligence + verified facts + debate history → generates argument
4. Output is cleaned, trimmed, and sent within the 2-minute window

### Prefetch timing (the key design)

```
Opponent sends → prefetch_opponent_analysis() fires immediately
                 [Groq runs in ~2s during server turn-switch delay]
                 → cache hot before our turn starts

We send        → prefetch_our_summary() fires immediately
                 [Groq runs in ~2s during opponent generation time]
                 → cache hot before next turn starts
```

---

## Stack

| Component | Model | Purpose |
|-----------|-------|---------|
| Argument generation | Claude Sonnet (`claude-sonnet-4-6`) | Persuasive debate arguments |
| Opponent analysis | Groq Llama (`llama-3.3-70b-versatile`) | Fast real-time analysis |

---

## Setup

### 1. Install dependencies

```bash
uv sync
```

### 2. Configure environment

Create a `.env` file:

```env
ANTHROPIC_API_KEY=your_key
GROQ_API_KEY=your_key
WS_SANDBOX_URL=wss://...
MY_TEAM_NAME=your_team_name
```

---

## Usage

### Run in competition match
```bash
uv run main.py
```

### Run in sandbox mode
```bash
uv run main.py --sandbox
```

### Run local simulation (no WebSocket)
```bash
uv run simulate.py
```

---

## Scoring

The agent is optimized for AgentSlam's judging criteria:

| Criterion | Weight | How we target it |
|-----------|--------|-----------------|
| Persuasiveness | 40% | Rhetoric, vivid narrative, memorable closers |
| Logic | 30% | Explicit fallacy naming, judo reframes, no contradictions |
| API Robustness | 20% | Try/catch everywhere, graceful fallbacks, no crashes |
| Agility | 10% | Opponent's exact words mirrored back and dismantled |

---

## Key config values

| Setting | Value | Notes |
|---------|-------|-------|
| `CLOSING_TRIGGER` | 180s | Switches to closing phase in last 3 minutes |
| `PAYLOAD_CHAR_LIMIT` | 2500 | Conservative buffer under server's 3000 limit |
| `BRAIN_MAX_TOKENS` | 600 | Keeps Claude response within char limit |
| `MAX_FACTS_IN_PROMPT` | 4 | Keeps prompts lean for speed |
