import logging
from pathlib import Path
from time import perf_counter

def calc_similarity_score(left: list[str], right: dict[str,int]) -> int:
    total = 0
    for l in left:
        if l in right:
            total+=int(l)*right[l]
    return total

def main(filepath: Path) -> int:
    left = []
    right = dict()
    with open(filepath, 'r') as f:
        for line in f.readlines():
            leftn, rightn = line.split()
            left.append(leftn)
            right.setdefault(rightn,0)
            right[rightn]+=1
    return calc_similarity_score(left, right)

def format_result(filename: str, statement: str) -> None:
    fp=Path(filename)
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    st_time=perf_counter()
    logging.info(f"{statement} {main(fp)}")
    end_time=perf_counter()
    logging.info(f"Approximate time of execution: {end_time-st_time} s")

if __name__ == "__main__":
    statement = "The similarity score is:"
    format_result("example.txt", statement)
    format_result("input.txt", statement)