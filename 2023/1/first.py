import logging
from pathlib import Path
from time import perf_counter

def find_first_and_last_digits(line: str) -> int:
    i_flag = False
    j_flag = False
    for i, j in zip(line, reversed(line)):
        if i.isdigit() and not i_flag:
            i_hold = i
            i_flag = True
        if j.isdigit() and not j_flag:
            j_hold = j
            j_flag = True
        if i_flag and j_flag:
            return int(i_hold+j_hold) 

def main(filepath: Path) -> int:
    with open(filepath, 'rt') as f:
       return sum(map(find_first_and_last_digits, map(str.strip, f.readlines())))

if __name__ == "__main__":
    fp=Path("input.txt")
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    st_time=perf_counter()
    logging.info(f"Total sum is: {main(fp)}")
    end_time=perf_counter()
    logging.info(f"Approximate time of execution: {end_time-st_time} s")