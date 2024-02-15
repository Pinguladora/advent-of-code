from typing import NoReturn, Generator


# General
def is_valid_pair(a: int, b: int) -> int:
    return 1 if (a & 0xFFFF) == (b & 0xFFFF) else 0


def read_generators_start(filepath: str) -> tuple[int, int]:
    with open(filepath, "rt") as f:
        return tuple(int(line.split()[-1]) for line in f)


# First
def count_pairs(
    iterations: int,
    gen_a: int,
    gen_b: int,
) -> int:
    return sum(
        is_valid_pair(
            (gen_a := (gen_a * 16807) % 2_147_483_647),
            (gen_b := (gen_b * 48271) % 2_147_483_647),
        )
        for _ in range(iterations + 1)
    )


# Second
def count_pairs_by_multiples(
    iterations: int,
    gen_a: int,
    gen_b: int,
    mod_a: int,
    mod_b: int,
) -> int:
    def generator(gen_st: int, factor: int, criteria: int) -> Generator[int, int, int]:
        val = gen_st
        while True:
            val = (val * factor) % 2_147_483_647
            if val % criteria == 0:
                yield val

    gen_a = generator(gen_a, 16807, mod_a)
    gen_b = generator(gen_b, 48271, mod_b)

    return sum(is_valid_pair(next(gen_a), next(gen_b)) for _ in range(iterations + 1))


def main(filepath: str = "input.txt") -> NoReturn:
    gen_a, gen_b = read_generators_start(filepath)
    # First challenge
    iterations = 40_000_000
    pairs = count_pairs(iterations, gen_a, gen_b)
    print(f"First challenge: the judge's final pair count is {pairs}")

    # Second challenge
    iterations = 5_000_000
    mod_a, mod_b = 4, 8
    pairs = count_pairs_by_multiples(iterations, gen_a, gen_b, mod_a, mod_b)
    print(f"Second challenge: the judge's final pair count is {pairs}")


if __name__ == "__main__":
    main()
