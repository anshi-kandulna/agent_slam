# groq_agent.py
# Simple opponent agent using Groq

import os
from groq import Groq
from config import GROQ_MODEL

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def generate_groq_argument(topic: str, stance: str, opponent_msg: str, turn: int) -> str:
    """
    Generates opponent argument using Groq model.
    """

    prompt = f"""
You are an AI debate opponent.

Topic: {topic}
Your stance: {stance}

Opponent's last argument:
{opponent_msg}

Instructions:
- Be aggressive but logical
- Attack opponent’s claims directly
- Use examples or reasoning
- Do NOT repeat previous points
- Keep under 2000 characters

Turn: {turn}

Output only the argument.
"""

    try:
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "system", "content": "You are a competitive debater."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_completion_tokens=500
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"[groq] error: {e}")
        return "Your argument lacks evidence and logical consistency."