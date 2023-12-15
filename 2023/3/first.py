from pathlib import Path
import logging
from time import perf_counter
import re

def sum_part_numbers(engine_schematic: str, maxtrix_size: int) -> int:
    symbol_pattern=re.compile(r'[^\w\s.]')
    num_pattern=re.compile(r'(\d+)')
    sum = 0
    for i in num_pattern.finditer(engine_schematic):
        try:
            logging.debug(f"Num {i.group()} with span: {i.span()}")
            num_start_idx=i.start()-1 # For prev line and its diagonal
            num_end_idx=i.end()+1 # For next line and its diagonal
            # Check left and right of the number group
            # Same as making a step with end-start-1 or the len of the number group
            # engine_schematic[num_start_idx:num_end_idx+1]
            if symbol_pattern.search(engine_schematic[num_start_idx]) or symbol_pattern.search(engine_schematic[num_end_idx-1]):
                sum += int(i.group())
                continue 
            # Check previous and next line to the number group
            prev_line=engine_schematic[num_start_idx-maxtrix_size:num_end_idx-maxtrix_size]
            next_line=engine_schematic[maxtrix_size+num_start_idx:maxtrix_size+num_end_idx]
            if symbol_pattern.search(prev_line) or symbol_pattern.search(next_line):
                sum += int(i.group())               
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
       return sum_part_numbers(engine_schematic, maxtrix_size)

if __name__ == "__main__":
    fp=Path("input.txt")
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    st_time=perf_counter()
    logging.info(f"Engine schematic sum is: {main(fp)}")
    end_time=perf_counter()
    logging.info(f"Approximate time of execution: {end_time-st_time} s")