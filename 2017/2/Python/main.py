from typing import NoReturn


# General
def read_spreadsheet(filename: str):
    with open(filename, "rt") as f:
        return [list(map(int, line.split())) for line in f]


# First
def calc_checksum(spreadsheet: list[list[int]]) -> int:
    return sum(max(r) - min(r) for r in spreadsheet)


# Second
def calc_row_sum(spreadsheet: list[list[int]]) -> int:
    total_sum = 0
    for row in spreadsheet:
        total_sum += sum(x // y for x in row for y in row if x % y == 0 and x != y)
    return total_sum


def main(filepath: str = "input.txt") -> NoReturn:
    spreadsheet = read_spreadsheet(filepath)

    # First challenge
    checksum = calc_checksum(spreadsheet)
    print(f"The cheksum of the spreadsheet is {checksum}")

    # Second challenge
    res_sum = calc_row_sum(spreadsheet)
    print(f"The sum of each row is {res_sum}")


if __name__ == "__main__":
    main()
