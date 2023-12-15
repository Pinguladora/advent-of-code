from pathlib import Path
import logging
from time import perf_counter

def replace_spelled_numbers(line: str) -> str:
    digits_to_int = {
        "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    # Address overlaps by duplicating first and last characters
    _ = [line := line.replace(word, f"{word[0]}{digits_to_int[word]}{word[-1]}") for word in digits_to_int]
    # A more readable way of doing this
    # for word in digits_to_int:
    #     line = line.replace(word, f"{word[0]}{digits_to_int[word]}{word[-1]}")
    return line

def find_first_and_last_real_digits(line: str) -> int:
    parsed_line = replace_spelled_numbers(line)
    digits = [d for d in parsed_line if d.isdigit()]

    logging.debug(f"Original Line: {line}")
    logging.debug(f"Transformed Line: {parsed_line}")
    logging.debug(f"Digits Found: {digits}")

    if digits:
        return int(int(digits[0] + digits[-1]))
    return 0

def main(filepath: Path) -> int:
    with open(filepath, 'rt') as f:
       return sum(map(find_first_and_last_real_digits, map(str.strip, f.readlines())))

if __name__ == "__main__":
    fp=Path("input.txt")
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    st_time=perf_counter()
    logging.info(f"Total sum is: {main(fp)}")
    end_time=perf_counter()
    logging.info(f"Approximate time of execution: {end_time-st_time} s")