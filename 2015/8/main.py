from pathlib import Path
from ast import literal_eval

def calc_chars_code_literal(line: str) -> int:
    # Equivalent to len(rf"'{line}'") if line is defined as variable
    return len(line)

def calc_chars_memory(line: str) -> int:
    return len(literal_eval(line))

def first_challenge(line: str) -> int:
    return calc_chars_code_literal(line) - calc_chars_memory(line)

def encode_string(line: str) -> int:
    transformed = line.replace("\\", "\\\\").replace("\"", "\\\"")
    # Add external double quotes
    return len(f"\"{transformed}\"")

def second_challenge(line: str) -> int:
    return encode_string(line) - calc_chars_code_literal(line)

def main(file_path: Path) -> None:
    first_total = 0
    second_total = 0
    with open(file_path, mode='rt') as f:
        for line in f:
            line=line.strip()
            first_total += first_challenge(line)
            second_total += second_challenge(line)

    print(f"First challenge: the number of characters is {first_total}")
    print(f"Second challenge: the number of characters is {second_total}")

if __name__ == "__main__":
    file_path = "input.txt"
    main(file_path)