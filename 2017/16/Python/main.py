from typing import NoReturn
from string import ascii_lowercase


# General
def read_dance_moves(filepath: str) -> list[str]:
    with open(filepath, "rt") as f:
        return f.read().split(",")


def apply_move(program: str, move: str) -> str:
    dance_mv = move[1:]
    if move.startswith("s"):  # Spin
        size = int(dance_mv)
        program = program[-size:] + program[:-size]
    elif move.startswith("x"):  # Exchange
        a, b = list(map(int, dance_mv.split("/")))
        program = swap_string(program, a, b)
    else:  # Partner
        a, b = dance_mv.split("/")
        program = swap_string(program, program.index(a), program.index(b))
    return program


def dance(program: str, moves: list[str]) -> str:
    _ = [program := apply_move(program, m) for m in moves]
    return program


# First
def swap_string(s: str, a: str, b: str) -> str:
    ls = list(s)
    ls[a], ls[b] = ls[b], ls[a]
    return "".join(ls)


# Second
# The trick here is to find if there is a cycle in which the ouput
# is the same as the original input
def dance_x_times(original: str, program: str, times: int, moves: list[str]) -> str:
    for i in range(times):
        program = dance(program, moves)
        if program == original:
            program = original
            round = i + 1  # accounts for the closed range
            off = times % round
            _ = [program := dance(program, moves) for _ in range(off)]
            break
    return program


def main(filepath: str = "input.txt") -> NoReturn:
    moves = read_dance_moves(filepath)
    program = ascii_lowercase[:16]

    # First challenge
    solution = dance(program, moves)
    print(f"First challenge: the order after their dance is {solution}")

    # Second challenge
    times = 1_000_000_000
    solution = dance_x_times(program, program, times, moves)
    print(f"Second challenge: the order after their billions dances is {solution}")


if __name__ == "__main__":
    main()
