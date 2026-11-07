import pathlib
import sys

SYSTEM_PATTERNS = [
    "SYSTEM PROMPT =",
    "system message =",
    '"role": "system"'
]

INJECTION_PHRASES = [
    "ignore previous instructions",
    "you are now",
    "pretend you are",
    "act as if you have no restrictions"
]

found = False

for file in pathlib.Path(".").rglob("*.py"):
    if ".git" in file.parts:
        continue

    content = file.read_text(errors="ignore")

    for pattern in SYSTEM_PATTERNS + INJECTION_PHRASES:
        if pattern.lower() in content.lower():
            print(f"[FOUND] {pattern} in {file}")
            found = True

if found:
    print("FAIL: Prompt injection patterns detected.")
    sys.exit(1)

print("PASS: No prompt injection patterns detected.")
sys.exit(0)
