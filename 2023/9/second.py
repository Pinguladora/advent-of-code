from pathlib import Path
from time import perf_counter
import logging

def extrapolate_values(history: str) -> int:
    history=history.strip().split()
    history: list[int]=list(map(int, history))
    sequences=[history]
    seq=history
    while any(seq) != 0:
        # Find the difference but backwards
        seq=[seq[i-1]-seq[i] for i in range(1, len(seq))]
        sequences.append(seq)
    return sum(seq[0] for seq in sequences)

# Summarized and a bit faster
def extrapolate_values(history: str) -> int:
    history=history.strip().split()
    history: list[int]=list(map(int, history))
    seq=history
    res=history[0]
    while any(seq) != 0:
        # Find the difference but backwards
        seq=[seq[i-1]-seq[i] for i in range(1, len(seq))]
        res+=seq[0]
    return res

def main(filepath: Path) -> int:
    with open(filepath, 'r') as f:
       return sum(map(extrapolate_values, f.readlines()))

if __name__ == "__main__":
    fp=Path("input.txt")
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    st_time=perf_counter()
    logging.info(f"Total sum of extrapolated values is: {main(fp)}")
    end_time=perf_counter()
    logging.info(f"Approximate time of execution: {end_time-st_time} s")