from collections import Counter
from typing import Callable

def get_corrected_msg(messages: list[str], func: Callable) -> str:
    corrected_msg = []
    for msg in zip(*messages):
        count=Counter(msg)
        char=func(count, key=count.get)
        corrected_msg.append(char)
    return "".join(corrected_msg)

def read_messages(filepath: str) -> list[str]:
    with open(filepath, 'r') as f:
        return f.read().splitlines()

if __name__ == "__main__":
    filepath="input.txt"
    messages=read_messages(filepath)

    # First challenge
    corrected_msg=get_corrected_msg(messages, max)
    print(f"First challenge: the original message is {corrected_msg}")

    # Second challenge
    corrected_msg=get_corrected_msg(messages, min)
    print(f"Second challenge: the original message is {corrected_msg}")