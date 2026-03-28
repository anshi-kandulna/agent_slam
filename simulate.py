# simulate.py
# Simulates a full 15-minute debate locally
# No WebSocket needed — tests brain + facts + opponent together

import time
from brain import generate_argument
from facts import get_facts_by_stance, format_facts_for_prompt
from opponent import opponent

TOPIC  = "Influencer marketing is more effective than traditional advertising"
STANCE = "PRO"

# Fix 1: Added 3 more opponent args to reach turn 7
FAKE_OPPONENT_ARGS = [
    "Traditional advertising has decades of proven ROI data. "
    "TV and print ads reach mass audiences that influencers simply cannot match. "
    "Nielsen reports that 92% of consumers trust traditional media over social content.",

    "Influencer fraud is rampant. "
    "Studies show up to 50% of influencer followers are bots. "
    "Brands are paying millions for fake engagement that drives zero real sales.",

    "Traditional advertising is regulated and accountable. "
    "Influencer content often lacks disclosure, misleading consumers "
    "and violating FTC guidelines at alarming rates.",

    "Mass market reach is irreplaceable. "
    "The Super Bowl reaches 100 million viewers — no single influencer comes close "
    "to that kind of simultaneous brand exposure.",

    "Traditional advertising builds brand legacy. "
    "Coca-Cola and Nike built trillion dollar brands long before influencers existed. "
    "Proven methods should not be discarded for unproven trends.",

    "Influencer marketing is completely saturated. "
    "Consumers are fatigued by constant sponsored content from every creator they follow. "
    "Trust in influencers is rapidly declining year over year.",
]

MATCH_DURATION_MS = 570 * 1000

def simulate():
    print("=" * 60)
    print(f"DEBATE SIMULATION")
    print(f"Topic:  {TOPIC}")
    print(f"Stance: {STANCE}")
    print("=" * 60)

    opponent.reset()
    our_history = []

    # Fix 2: Changed range to 7 turns
    for turn in range(5):
        print(f"\n{'─'*60}")
        print(f"TURN {turn + 1}")
        print(f"{'─'*60}")

        # Fix 3: Recalculate finish_time each turn
        # Simulates ~2 minutes passing per turn (realistic match pace)
        fake_finish_time = (time.time() * 1000) + MATCH_DURATION_MS - (turn * 120 * 1000)
        time_remaining_s = (fake_finish_time - time.time() * 1000) / 1000
        print(f"Time remaining: {time_remaining_s:.0f}s")

        # Add fake opponent message (skip turn 0 — opening)
        if turn > 0 and turn - 1 < len(FAKE_OPPONENT_ARGS):
            opp_msg = FAKE_OPPONENT_ARGS[turn - 1]
            opponent.add_message(opp_msg)
            print(f"\n[OPPONENT]: {opp_msg[:150]}...")

        # Get opponent context
        opponent_ctx = opponent.get_context_for_brain(
            topic=TOPIC,
            our_stance=STANCE,
            run_llm=False
        )

        # Generate our argument
        print(f"\n[GENERATING OUR ARGUMENT...]")
        start = time.time()

        result = generate_argument(
            topic=TOPIC,
            stance=STANCE,
            opponent_ctx=opponent_ctx,
            finish_time=fake_finish_time,  # pass updated finish_time
            our_history=our_history
        )

        elapsed = time.time() - start
        print(f"[GENERATED in {elapsed:.1f}s]")
        print(f"[LENGTH: {len(result.encode('utf-8'))} bytes]")
        print(f"\n[US]: {result}")

        our_history.append(result)

        # Rate limit safe gap (skip after last turn)
        # if turn < 6:
        #     print(f"\n[Waiting 12s for rate limit...]")
        #     time.sleep(12)

    print("\n" + "=" * 60)
    print("SIMULATION COMPLETE")
    print("=" * 60)
    print(f"Total turns: {len(our_history)}")
    print(f"Avg length:  {sum(len(a) for a in our_history) // len(our_history)} chars")

if __name__ == "__main__":
    simulate()
