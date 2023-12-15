import math
from pathlib import Path
import logging
import re
from time import perf_counter

# 'Hacky' way using split and \n at the end of line
# def calc_min_set_power(line: str) -> int:
#     _, _, *sets = line.split(' ')
#     color_maxs={}
#     for i in range(0, len(sets), 2):
#         num=int(sets[i])
#         # We're using the \n to helps us, so all lines have a 'separator' character at the end
#         color=sets[i+1][:-1]
#         color_maxs.update({color: max(num, color_maxs.get(color, 0))})
#     res = 1
#     for color in color_maxs:
#         res *= color_maxs[color]
#     return res

def calc_min_set_power(line: str) -> int:
    game_info = re.match(r"Game (\d+): (.*)", line)
    sets = re.findall(r"(\d+) (\w+)", game_info.group(2))
    color_maxs = {}
    for num, color in sets:
        num = int(num)
        color_maxs[color] = max(num, color_maxs.get(color, 0))
    return math.prod(color_maxs.values()) if color_maxs else 0 # Functools reduce can be used too

def main(filepath: Path) -> int:
    with open(filepath, 'r') as f:
       return sum(map(calc_min_set_power, f.readlines()))

if __name__ == "__main__":
    fp=Path("input.txt")
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    st_time=perf_counter()
    logging.info(f"Total powers sum is: {main(fp)}")
    end_time=perf_counter()
    logging.info(f"Approximate time of execution: {end_time-st_time} s")