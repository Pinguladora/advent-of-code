from pathlib import Path
import logging
from time import perf_counter
from operator import mul
from functools import reduce

# Naive approach
def get_num_ways_to_beat_record(lines: list[str]) -> list[int]:
    _, race_time_data=lines[0].split(":")
    _, distances_data=lines[1].split(":")

    race_time=race_time_data.strip().split()
    distance_record=distances_data.strip().split()

    race_time = int(''.join(race_time))
    current_record = int(''.join(distance_record))
    
    res=[0]
    k=race_time//2
    for i_speed, j_speed in zip(range(0,k), range(k,race_time)):
        remaining_time=race_time-i_speed
        if i_speed*remaining_time>current_record:
            res[0] += 1
        remaining_time=race_time-j_speed
        if remaining_time*j_speed>current_record: 
            res[0] += 1
    return res

# Best approach, around 2 times faster
def get_num_ways_to_beat_record(lines: list[str]) -> list[int]:
    _, race_time_data=lines[0].split(":")
    _, distance_data=lines[1].split(":")

    # If no argument is given split treats any number of whitespace as a single separator
    race_time=race_time_data.strip().split()
    distance_record=distance_data.strip().split()

    race_time = int(''.join(race_time))
    current_record = int(''.join(distance_record))
    
    res=[0]
    mid_point=race_time // 2
    for t in range(mid_point + 1):  # Iterate up to the midpoint
        remaining_time = race_time - t
        if t * remaining_time > current_record:
            # Race graph is symmetric, therefore it mirrors in both sides
            # So we can add 2 if time is odd (mirror is not possible) 
            # Otherwise 1 if it's even (mirror duplicates in the middle point)
            res[0] += 2 if t != mid_point or race_time % 2 != 0 else 1
    return res

def main(filepath: Path) -> int:
    with open(filepath, 'r') as f:
       return reduce(mul, get_num_ways_to_beat_record(f.readlines()))

if __name__ == "__main__":
    fp=Path("input.txt")
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    st_time=perf_counter()
    logging.info(f"Result is: {main(fp)}")
    end_time=perf_counter()
    logging.info(f"Approximate time of execution: {end_time-st_time} s")