import os
import ast

SYSTEM_MESSAGE = os.environ.get("AI_SYSTEM_PROMPT", "You are a helpful assistant.")

def calculate(expression):
    return ast.literal_eval(expression)

def chat(user_input):
    print("System:", SYSTEM_MESSAGE)
    print("User:", user_input)
    return "Demo AI response"

if __name__ == "__main__":
    print(chat("Hello"))
    print("Calculation:", calculate("2"))
