from typing import NoReturn


# General
def read_offsets(filepath: str) -> list[int]:
    with open(filepath, "rt") as f:
        return list(map(int, f))


# First
def calc_steps_required(offsets: list[int]) -> int:
    offsets_cp = list(offsets)
    size = len(offsets_cp)
    steps, cursor = 0, 0
    # Check if cursor is out of bounds, considering only forward exit
    while cursor < size:
        # Same as if cursor >= size: break
        jmp = cursor + offsets_cp[cursor]
        offsets_cp[cursor] += 1
        cursor = jmp
        steps += 1
    return steps


# Second
def calc_steps_required_with_decrease(offsets: list[int]) -> int:
    offsets_cp = list(offsets)
    size = len(offsets_cp)
    steps, cursor = 0, 0
    while cursor < size:
        jmp = cursor + offsets_cp[cursor]
        offsets_cp[cursor] += 1 if offsets_cp[cursor] < 3 else -1
        cursor = jmp
        steps += 1
    return steps


def main(filepath: str = "input.txt") -> NoReturn:
    offsets = read_offsets(filepath)

    # First challenge
    steps = calc_steps_required(offsets)
    print(f"First challenge: it takes {steps} steps to reach the exit")

    # Second challenge
    steps = calc_steps_required_with_decrease(offsets)
    print(f"Second challenge: it takes {steps} steps to reach the exit")


if __name__ == "__main__":
    main()
