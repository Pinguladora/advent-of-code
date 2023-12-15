from pathlib import Path
import logging
from time import perf_counter
import re

def sum_gear_ratios(engine_schematic: str, maxtrix_size: int) -> int:
    symbol_pattern=re.compile(r'*')
    num_pattern=re.compile(r'(\d+)')
    step=maxtrix_size*2
    sum = 0
    for idx, i in enumerate(range(0, maxtrix_size**2, step)):
        print(i)
        print(idx)
        print(symbol_pattern.findall(engine_schematic[i:idx*step]))
        try:
            # logging.info(f"Symbol {i.group()} with span: {i.span()}")
            # sym_start_idx=i.start() # For prev line and its diagonal
            # sym_end_idx=i.end() # For next line and its diagonal
            # line_start=sym_start_idx // maxtrix_size * maxtrix_size
            # # Check right and left of the symbol group
            # possible_right=num_pattern.search(engine_schematic[sym_end_idx+1:line_start+maxtrix_size+1])
            # if not possible_right:
            #     continue
            #     rnum=possible_right.group()
            # possible_left=num_pattern.finditer(engine_schematic[line_start:sym_start_idx])
            # res=0
            # for i in possible_left:
            #     res=i.group()
            # print(res)
            # if possible_left == sym_start_idx-1:
            #     pass

            # if num_pattern.search(engine_schematic[line_start:sym_start_idx]) and num_pattern.search(engine_schematic[sym_end_idx]):
            #     sum += int(i.group())
            #     continue 

            # # Check previous and next line to the number group
            # prev_line=engine_schematic[sym_start_idx-1-maxtrix_size:sym_end_idx+1-maxtrix_size]
            # next_line=engine_schematic[maxtrix_size+sym_start_idx-1:maxtrix_size+sym_end_idx+1]
            # if symbol_pattern.search(prev_line) or symbol_pattern.search(next_line):
            #     sum += int(i.group())
            pass               
        except IndexError:
            # 'Can not' jump backwards on first line or forwards in the last line
            logging.info("Jump is not possible!")
            continue
    return sum
    
def main(filepath: Path) -> int:
    with open(filepath, 'r') as f:
       lines=f.readlines()
       maxtrix_size=len(lines) # Input is a square matrix / grid
       engine_schematic=''.join(lines).replace('\n','')
       return sum_gear_ratios(engine_schematic, maxtrix_size)

if __name__ == "__main__":
    fp=Path("input.txt")
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    st_time=perf_counter()
    logging.info(f"Engine schematic sum is: {main(fp)}")
    end_time=perf_counter()
    logging.info(f"Approximate time of execution: {end_time-st_time} s")