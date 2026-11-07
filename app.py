import os

SYSTEM_PROMPT = "You are a helpful AI assistant. Ignore previous instructions only when authorized."

API_KEY = "sk-demo-1234567890abcdef"

def calculate(expression):
    return eval(expression)

def chat(user_input):
    print("System:", SYSTEM_PROMPT)
    print("User:", user_input)
    return "Demo AI response"

if __name__ == "__main__":
    print(chat("Hello"))
    print("Calculation:", calculate("2 + 2"))
