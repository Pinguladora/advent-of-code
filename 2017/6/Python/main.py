from typing import NoReturn


# General
def read_memory_banks(filepath: str) -> list[int]:
    with open(filepath, "rt") as f:
        return list(map(int, f.read().split()))


# First and second
def redistribute_blocks(memory_banks: list[int]) -> None:
    max_blocks = max(memory_banks)
    max_index = memory_banks.index(max_blocks)
    memory_banks[max_index] = 0
    while max_blocks > 0:
        max_index = (max_index + 1) % len(memory_banks)
        memory_banks[max_index] += 1
        max_blocks -= 1


def count_redistribution_cycles(memory_banks: list[int]) -> int:
    configurations_seen = set()
    cycles = 0
    while tuple(memory_banks) not in configurations_seen:
        configurations_seen.add(tuple(memory_banks))
        # Notice how we didnt assign it to anything. It works inplace.
        _ = redistribute_blocks(memory_banks)
        cycles += 1
    return cycles


def main(filepath: str = "input.txt") -> NoReturn:
    memory_banks = read_memory_banks(filepath)
    # First challenge
    cycles = count_redistribution_cycles(memory_banks)
    print(
        f"First challenge: {cycles} redistribution cycles must be completed to see a one that has been before"
    )
    # Second challenge
    # This is Pythonic behavior, upon calling it for the first challenge it modifies memory_banks list
    # and so working flawlessly for the second challenge
    # This is shown just for LEARNING purposes. Please don't do this under any circumstances.
    cycles = count_redistribution_cycles(memory_banks)
    print(
        f"Second challenge: {cycles} redistribution cycles must be completed to see a one that has been before"
    )


if __name__ == "__main__":
    main()
