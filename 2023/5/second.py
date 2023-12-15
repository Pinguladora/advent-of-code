from pathlib import Path
import logging
from time import perf_counter
from itertools import chain

def align_almanac(lines: list[str]) -> list[int]:
    seeds=lines.pop(0).split()[1:]
    seeds=list(map(int, seeds))
    size=len(seeds)
    seeds=list((False, num) for num in chain.from_iterable(range(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, size, 2)))
    print(seeds)
    # size=len(seeds)
    for line in lines:
        if line in ['\n', '\r\n']: # New category in next line
            next_is_category=True
        elif next_is_category:
            # category_name, _ = line.split()
            # mappings[category_name]=seeds
            next_is_category=False
            # already_mapped=[False]*size
        else: # Mapping values
            dst_range, src_range, length=map(int, line.split())
            for i, seed_data in enumerate(seeds):
                # To be in range the seed number minus the source range 
                # should be lower than the range length
                if not seed_data[0]:
                    diff=seed_data - src_range
                    if diff == 0 or src_range == seed_data:
                        seeds[i]=dst_range
                        already_mapped[i]=True
                    elif diff>0 and diff<length:
                        seeds[i]=dst_range+diff
                        already_mapped[i]=True
    return seeds

def main(filepath: Path) -> int:
    with open(filepath, 'r') as f:
       return min(align_almanac(f.readlines()))

if __name__ == "__main__":
    fp=Path("example.txt")
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    st_time=perf_counter()
    logging.info(f"Lowest location is: {main(fp)}")
    end_time=perf_counter()
    logging.info(f"Approximate time of execution: {end_time-st_time} s")