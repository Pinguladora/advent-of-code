from typing import NoReturn


# General
def read_sequence(filename: str) -> str:
    with open(filename, "rt") as f:
        return f.read()


# First
def solve_captcha(sequence: str) -> list[str]:
    size = len(sequence)
    seq = "".join([sequence, sequence[0]])  # Create circular list
    return sum(int(seq[i]) for i in range(size) if seq[i] == seq[i + 1])


# First
def solve_captcha_halfway_around(sequence: str) -> list[str]:
    size = len(sequence)
    offset = size // 2
    seq = "".join([sequence, sequence[:offset]])  # Create circular list
    return sum(int(seq[i]) for i in range(size) if seq[i] == seq[i + offset])


def main(filepath: str = "input.txt") -> NoReturn:
    seq = read_sequence(filepath)
    # First challenge
    sol = solve_captcha(seq)
    print(f"First challenge: the solution to the captcha is {sol}")
    # Second challenge
    sol = solve_captcha_halfway_around(seq)
    print(f"Second challenge: the solution to the captcha is {sol}")


if __name__ == "__main__":
    main()
