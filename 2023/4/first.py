import logging
from pathlib import Path
from time import perf_counter

def obtain_points(scratchcard: str) -> int:
    winning_numbers, taken_numbers = scratchcard.strip().split('|')
    winning_numbers = winning_numbers.split(' ')[2:]
    winning_numbers = list(filter(None, winning_numbers))
    taken_numbers=taken_numbers.split(' ')[1:]
    taken_numbers = list(filter(None, taken_numbers))
    n_matches=sum(1 for number in winning_numbers if number in taken_numbers)
    res=n_matches # Assume one match or no match at all
    if n_matches >=2: # 2**(n-1)
        res=2**(n_matches-1)
    return res

def main(filepath: Path) -> int:
    with open(filepath, 'r') as f:
       return sum(map(obtain_points, f.readlines()))

if __name__ == "__main__":
    fp=Path("input.txt")
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    st_time=perf_counter()
    logging.info(f"Total point sum is: {main(fp)}")
    end_time=perf_counter()
    logging.info(f"Approximate time of execution: {end_time-st_time} s")