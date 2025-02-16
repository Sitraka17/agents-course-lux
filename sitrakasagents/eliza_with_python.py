import re
import random

# Predefined patterns and responses
reflections = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

psychobabble = [
    [r'I need (.*)',
     ["Why do you need {0}?",
      "Would it really help you to get {0}?",
      "Are you sure you need {0}?"]],

    [r'Why don\'t you (.*)',
     ["Do you really think I don't {0}?",
      "Perhaps eventually I will {0}.",
      "Do you want me to {0}?"]],

    [r'Why can\'t I (.*)',
     ["Do you think you should be able to {0}?",
      "If you could {0}, what would you do?",
      "I don't know — why can't you {0}?",
      "Have you really tried?"]],

    [r'I can\'t (.*)',
     ["How do you know you can't {0}?",
      "Perhaps you could {0} if you tried.",
      "What would it take for you to {0}?"]],

    [r'I am (.*)',
     ["How long have you been {0}?",
      "Do you enjoy being {0}?",
      "Why do you tell me you're {0}?",
      "Why do you think you're {0}?"]],

    [r'Hello(.*)',
     ["Hello... I'm glad you could drop by today.",
      "Hi there... how are you today?",
      "Hello, how are you feeling today?"]],

    [r'(.*) sorry (.*)',
     ["There are many times when no apology is needed.",
      "What feelings do you have when you apologize?"]],

    [r'Quit',
     ["Thank you for talking with me.",
      "Good-bye.",
      "Thank you, have a good day!"]],

    [r'(.*)',
     ["Please tell me more.",
      "Let's change focus a bit... Tell me about your family.",
      "Can you elaborate on that?",
      "Why do you say that {0}?",
      "I see. Can you say more?",
      "Interesting. Can you explain further?",
      "Do you feel strongly about discussing this?"]]
]

def reflect(fragment):
    """Reflects pronouns for the conversation."""
    words = fragment.lower().split()
    for i, word in enumerate(words):
        if word in reflections:
            words[i] = reflections[word]
    return ' '.join(words)

def analyze(statement):
    """Matches user's statement with a pattern and returns a response."""
    for pattern, responses in psychobabble:
        match = re.match(pattern, statement.rstrip(".!?"), re.IGNORECASE)
        if match:
            response = random.choice(responses)
            return response.format(*[reflect(g) for g in match.groups()])
    return "I'm not sure I understand you fully."

def eliza_chat():
    """Runs the ELIZA chatbot."""
    print("ELIZA: Hello. How can I help you today?")
    while True:
        statement = input("You: ")
        if statement.lower() in ["quit", "exit", "bye"]:
            print("ELIZA: Goodbye! Take care.")
            break
        response = analyze(statement)
        print(f"ELIZA: {response}")

# Run the chatbot
if __name__ == "__main__":
    eliza_chat()
