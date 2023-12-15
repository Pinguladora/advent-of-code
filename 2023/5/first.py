from pathlib import Path
import logging
from time import perf_counter

# First approach
def align_almanac(lines: list[str]) -> list[int]:
    seeds=lines.pop(0).split()[1:]
    seeds=list(map(int, seeds))
    for line in lines:
        if line in ['\n', '\r\n']: # New category in next line
            next_is_category=True
        elif next_is_category:
            next_is_category=False
            already_mapped=[False]*len(seeds)
        else: # Map values
            dst_range, src_range, length=map(int, line.split())
            for i, seed_num in enumerate(seeds):
                # To be in range the seed number minus the source range 
                # should be lower than the range length
                if not already_mapped[i]:
                    diff=seed_num - src_range
                    if diff == 0 or src_range == seed_num:
                        seeds[i]=dst_range
                        already_mapped[i]=True
                    elif diff>0 and diff<length:
                        seeds[i]=dst_range+diff
                        already_mapped[i]=True
    return seeds
# Better
def align_almanac(lines: list[str]) -> list[int]:
    seeds=lines.pop(0).split()[1:]
    seeds=list(map(int, seeds))
    # already_mapped=(False)*len(seeds)
    already_mapped=set()
    for line in lines:
        if line in ['\n', '\r\n']:
            continue
        elif line.endswith('map:\n'): 
            already_mapped=set() # New category in next line
        else:
            dst_range, src_range, length=map(int, line.split())
            for i, seed_num in enumerate(seeds):
                # To be in range the seed number minus the source range 
                # should be lower than the range length
                if seed_num not in already_mapped:
                    diff=seed_num - src_range
                    print(diff)
                    if diff == 0 or src_range == seed_num:
                        seeds[i]=dst_range
                        already_mapped.add(seed_num)
                    elif diff>0 and diff<length:
                        seeds[i]=dst_range+diff
                        already_mapped.add(seed_num)
            print(already_mapped)
            print(seeds)
    return seeds

def main(filepath: Path) -> int:
    with open(filepath, 'r') as f:
       return min(align_almanac(f.readlines()))


# def align_almanac(filepath: str) -> list[int]:
#     with open(filepath, 'r') as f:
#         # Parse seeds
#         seeds = list(map(int, f.readline().split()[1:]))
        
#         # Initialize mapping and tracking variables
#         category_maps = {}
#         mapped_seeds = set()
#         current_category = None

#         # Process each line
#         for line in f:
#             line = line.strip()
#             if not line:  # Skip empty lines
#                 continue

#             # Check if line indicates a new category
#             if line.endswith('map:'):
#                 current_category = line.split(':')[0]
#                 category_maps[current_category] = {}
#                 mapped_seeds.clear()
#                 continue

#             # Parse mapping line
#             dst_start, src_start, length = map(int, line.split())
#             for i in range(length):
#                 category_maps[current_category][src_start + i] = dst_start + i

#             # Apply mapping to seeds
#             for i, seed in enumerate(seeds):
#                 if seed in category_maps[current_category] and i not in mapped_seeds:
#                     seeds[i] = category_maps[current_category][seed]
#                     mapped_seeds.add(i)

#     return seeds

# def main(filepath: str) -> int:
#     return min(align_almanac(filepath))

if __name__ == "__main__":
    fp=Path("example.txt")
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    st_time=perf_counter()
    logging.info(f"Lowest location is: {main(fp)}")
    end_time=perf_counter()
    logging.info(f"Approximate time of execution: {end_time-st_time} s")