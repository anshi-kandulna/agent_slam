# test_groq.py
from opponent import opponent
import time

test_messages = [
    "AI will never replace human creativity because machines lack consciousness and emotional depth. Studies show 87% of creative professionals believe AI-generated art lacks authentic meaning.",
    "Furthermore, the economic argument for AI replacing jobs is flawed. History shows automation creates more jobs than it destroys."
]

print("=== Test 1: Message tracking ===\n")
for msg in test_messages:
    opponent.add_message(msg)
print(f"History length: {len(opponent.history)} (expected 2)\n")

print("=== Test 2: Opponent analysis (Groq) ===\n")
opponent.prefetch_opponent_analysis(
    topic="AI will replace human creativity",
    our_stance="PRO"
)
time.sleep(5)  # wait for thread

print("=== Test 3: Our summary (Groq) ===\n")
our_history = ["AI already composes music, writes code, and generates award-winning art. The question is not if, but when it surpasses human output entirely."]
opponent.prefetch_our_summary(our_history)
time.sleep(5)  # wait for thread

print("=== Test 4: get_context_for_brain ===\n")
ctx = opponent.get_context_for_brain()
for k, v in ctx.items():
    print(f"[{k}]: {v}\n")

print("Done.")