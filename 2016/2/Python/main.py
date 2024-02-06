
KEYPAD = {'1': (0, 0), '2': (1, 0), '3': (0, 1),
            '4': (0, 1), '5': (1, 1), '6': (2, 1),
            '7': (0, 2), '8': (1, 2), '9': (2, 2)}

def get_bathroom_code(start: str, instructions: str) -> str:
    reverse_keypad = {v: k for k, v in KEYPAD.items()}
    
    x, y = KEYPAD[start]
    code = []
    for instruction in instructions:
        for move in instruction:
            if move == 'U':
                y = max(y - 1, 0)
            elif move == 'D':
                y = min(y + 1, 2)
            elif move == 'L':
                x = max(x - 1, 0)
            elif move == 'R':
                x = min(x + 1, 2)
        code.append(reverse_keypad[(x, y)])
    return "".join(code)

CROSS_KEYPAD = {
            '1': {'D': '3'},
            '2': {'R': '3', 'D': '6'},
            '3': {'U': '1', 'D': '7', 'L': '2', 'R': '4'},
            '4': {'L': '3', 'D': '8'},
            '5': {'R': '6'},
            '6': {'U': '2', 'D': 'A', 'L': '5', 'R': '7'},
            '7': {'U': '3', 'D': 'B', 'L': '6', 'R': '8'},
            '8': {'U': '4', 'D': 'C', 'L': '7', 'R': '9'},
            '9': {'L': '8'},
            'A': {'U': '6', 'R': 'B'},
            'B': {'U': '7', 'D': 'D', 'L': 'A', 'R': 'C'},
            'C': {'U': '8', 'L': 'B'},
            'D': {'U': 'B'}
        }

def get_bathroom_code_crossgrid(start: str, instructions: str) -> str:
    position = start
    code = []
    for instruction in instructions:
        for move in instruction:
            # Update position if move is possible
            if move in CROSS_KEYPAD[position]:
                position = CROSS_KEYPAD[position][move]
        code.append(position)
    return "".join(code)

def read_instructions(filepath: str) -> list[str]:
    with open(filepath, 'rt') as f:
        return f.read().splitlines()


if __name__ == "__main__":
    filepath = "input.txt"
    instructions=read_instructions(filepath)
    # First challenge
    bathroom_code = get_bathroom_code("5", instructions)
    print(f"First challenge: the bathroom code is {bathroom_code}")

    # Second challenge
    bathroom_code = get_bathroom_code_crossgrid("5", instructions)
    print(f"Second challenge: the bathroom code is {bathroom_code}")