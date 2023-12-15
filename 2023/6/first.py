from pathlib import Path
import logging
from time import perf_counter
from operator import mul
from functools import reduce

# For both
# Upper and lower limits doesn't matter as they are always 0

# For even race times we know:
# Graph looks like -> ...___-___...
# Peak distance is in t/2
# res[index] += 1

# Graph looks like -> ...___--___...
# For odd race times we know:
# Peak distances are in t/2 and t/2+1
# res[index] += 2
 
# Naive approach
def get_num_ways_to_beat_record(lines: list[str]) -> list[int]:
    _, race_times_data=lines[0].split(":")
    _, distances_data=lines[1].split(":")

    # If no argument is given split treats any number of whitespace as a single separator
    race_times=race_times_data.strip().split() 
    distance_records=distances_data.strip().split()

    race_times = list(map(int,race_times))
    distance_records = list(map(int,distance_records))
    
    res=[0]*len(race_times)
    for index, time in enumerate(race_times):
        k=time//2
        for i_speed, j_speed in zip(range(0,k), range(k,time)):
            remaining_time=time-i_speed
            current_record=distance_records[index]
            if i_speed*remaining_time>current_record:
                res[index] += 1
            remaining_time=time-j_speed
            if remaining_time*j_speed>current_record: 
                res[index] += 1
    return res

# Best approach
def get_num_ways_to_beat_record(lines: list[str]) -> list[int]:
    _, race_times_data=lines[0].split(":")
    _, distances_data=lines[1].split(":")

    # If no argument is given split treats any number of whitespace as a single separator
    race_times=race_times_data.strip().split() 
    distance_records=distances_data.strip().split()

    race_times = list(map(int,race_times))
    distance_records = list(map(int,distance_records))
    
    res=[0]*len(race_times)
    for index, time in enumerate(race_times):
        current_record=distance_records[index]
        mid_point = time // 2 # Middle point

        for t in range(mid_point + 1):  # Iterate up to the midpoint
            remaining_time = time - t
            if t * remaining_time > current_record:
                # Race graph is symmetric, therefore it mirrors in both sides
                # So we can add 2 if time is odd (mirror is not possible) 
                # Otherwise 1 if it's even (mirror duplicates in the middle point)
                res[index] += 2 if t != mid_point or time % 2 != 0 else 1
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