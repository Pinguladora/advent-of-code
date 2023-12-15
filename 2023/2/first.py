from pathlib import Path
import logging
import re
from time import perf_counter

ALLOWED_MAX_LIMITS = {"red": 12, "green": 13, "blue": 14}

# 'Hacky' way using split and \n at the end of line
# def is_game_possible(line: str) -> int:
#     _, game_id, *sets = line.split(' ')
#     res = int(game_id[:-1])
#     for i in range(0, len(sets), 2):
#         num=int(sets[i])
#         # We're using the \n to helps us, so all lines have a separator character at the end
#         color=sets[i+1][:-1]
#         if num > ALLOWED_MAX_LIMITS[color]: # Game is therefore impossible
#             res = 0
#             break
#     return res

def is_game_possible(line: str) -> int:
    game_info = re.match(r"Game (\d+): (.*)", line)
    game_id, sets = game_info.groups()
    game_id = int(game_id)
    sets = re.findall(r"(\d+) (\w+)", sets)
    for num, color in sets:
        if int(num) > ALLOWED_MAX_LIMITS.get(color, 0):
            return 0
    return game_id

def main(filepath: Path) -> int:
    with open(filepath, 'r') as f:
       return sum(map(is_game_possible, f.readlines()))

if __name__ == "__main__":
    fp=Path("input.txt")
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    st_time=perf_counter()
    logging.info(f"Total ID sum is: {main(fp)}")
    end_time=perf_counter()
    logging.info(f"Approximate time of execution: {end_time-st_time} s")
