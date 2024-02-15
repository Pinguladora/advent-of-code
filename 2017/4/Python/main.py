from typing import NoReturn


# General
def read_passphrases(filepath: str) -> list[list[str]]:
    with open(filepath, "rt") as f:
        return [line.split() for line in f.readlines()]


# First
def check_duplicates(passphrases: list[list[str]]) -> int:
    return sum(1 for p in passphrases if len(set(p)) == len(p))


# Second
def check_for_anagrams(passphrases: list[list[str]]) -> int:
    valid = 0
    for p in passphrases:
        ordered = tuple(tuple(sorted(word)) for word in p)
        if len(ordered) == len(set(ordered)):
            valid += 1
    return valid


def main(filepath: str = "input.txt") -> NoReturn:
    passphrases = read_passphrases(filepath)

    # First challenge
    valid_passphrases = check_duplicates(passphrases)
    print(f"First challenge: there are {valid_passphrases} valid passphrases")

    # Second challenge
    valid_passphrases = check_for_anagrams(passphrases)
    print(f"Second challenge: there are {valid_passphrases} valid passphrases")


if __name__ == "__main__":
    main()
