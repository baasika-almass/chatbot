import re
import random
from datetime import datetime

# ─── Response Data ────────────────────────────────────────────────────────────

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the function break up with the loop? It felt it was going in circles.",
    "Why do Python programmers wear glasses? Because they can't C!",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
]

GREETINGS = ["hi", "hello", "hey", "hii", "hiya"]
FAREWELLS = ["bye", "goodbye", "see you", "exit", "quit"]


# ─── Response Logic ──────────────────────────────────────────────────────────

def get_response(message, user_name):
    """Generate a response based on pattern matching the user's message."""
    msg = message.lower().strip()

    # Greetings
    if any(msg.startswith(g) for g in GREETINGS):
        return f"Hello {user_name}! How can I help you today?"

    # Farewells
    if any(f in msg for f in FAREWELLS):
        return f"Goodbye {user_name}! Have a great day! 👋"

    # How are you
    if "how are you" in msg:
        return "I'm just code, but I'm running smoothly! How about you?"

    # Name
    if "your name" in msg:
        return "I'm PyBot — a simple rule-based chatbot built in Python!"

    # Time
    if "time" in msg:
        now = datetime.now().strftime("%I:%M %p")
        return f"Right now it's {now}."

    # Date
    if "date" in msg or "today" in msg:
        today = datetime.now().strftime("%A, %d %B %Y")
        return f"Today's date is {today}."

    # Joke
    if "joke" in msg:
        return random.choice(JOKES)

    # Thanks
    if "thank" in msg:
        return "You're welcome!"

    # Math expression like "5 + 3" or "10 * 2"
    math_result = try_math(msg)
    if math_result is not None:
        return f"That equals {math_result}"

    # Fallback
    return "Hmm, I'm not sure how to respond to that. Try asking my name, the time, a joke, or a math problem!"


def try_math(msg):
    """Check if the message is a simple math expression and solve it."""
    pattern = r"(-?\d+(?:\.\d+)?)\s*([\+\-\*/])\s*(-?\d+(?:\.\d+)?)"
    match = re.search(pattern, msg)
    if not match:
        return None

    a = float(match.group(1))
    op = match.group(2)
    b = float(match.group(3))

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            return "undefined (division by zero)"
        result = a / b
    else:
        return None

    # Show as integer if it's a whole number
    if result == int(result):
        return int(result)
    return round(result, 2)


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("\n  🤖 PYBOT — Simple Chatbot")
    print("  " + "=" * 30)

    user_name = input("  What's your name? ").strip() or "friend"
    print(f"\n  PyBot: Hi {user_name}! Ask me your name, the time, a joke,")
    print("         or give me a math problem like '5 + 3'.")
    print("         Type 'bye' to exit.\n")

    while True:
        user_input = input(f"  {user_name}: ").strip()

        if not user_input:
            continue

        response = get_response(user_input, user_name)
        print(f"  PyBot: {response}\n")

        if any(f in user_input.lower() for f in FAREWELLS):
            break


if __name__ == "__main__":
    main()
