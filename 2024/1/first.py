import logging
from pathlib import Path
from time import perf_counter

def calc_distance(a: int, b: int) -> int:
    return abs(a-b)

def main(filepath: Path) -> int:
    left = []
    right = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            leftn, rightn = list(map(int, line.split()))
            left.append(leftn)
            right.append(rightn)
    left.sort()
    right.sort()
    return sum(map(calc_distance, left, right))

def format_result(filename: str, statement: str) -> None:
    fp=Path(filename)
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    st_time=perf_counter()
    logging.info(f"{statement} {main(fp)}")
    end_time=perf_counter()
    logging.info(f"Approximate time of execution: {end_time-st_time} s")

if __name__ == "__main__":
    statement = "The total distance between lists is:"
    format_result("example.txt", statement)
    format_result("input.txt", statement)