import logging
from pathlib import Path
from time import perf_counter

def sum_num_scratchcard(game_id: int, scratchcard: str, scratchcard_count: dict) -> dict:
    winning_numbers, taken_numbers = scratchcard.strip().split('|')
    winning_numbers = winning_numbers.split(' ')[2:]
    winning_numbers = list(filter(None, winning_numbers))
    taken_numbers=taken_numbers.split(' ')[1:]
    taken_numbers = list(filter(None, taken_numbers))
    n_matches=sum(1 for number in winning_numbers if number in taken_numbers)
    # We don't want a meaningless iteration (sum 0) so we start from 1
    for i in range(1, n_matches+1): 
        pos=game_id+i
        # Old value plus or zero if new plus the number of cards from the current game
        scratchcard_count[pos]=scratchcard_count.get(pos,0)+scratchcard_count[game_id]
    return scratchcard_count

def main(filepath: Path) -> int:
    with open(filepath, 'r') as f:
        original_lines=f.readlines()
        scratchcard_count = {}
        for i, line in enumerate(original_lines):
            # i plus one to align with Game IDs starting from 1
            scratchcard_count[i+1]=scratchcard_count.get(i+1,0)+1
            scratchcard_count.update(sum_num_scratchcard(i+1, line, scratchcard_count))
        return sum(scratchcard_count.values())

if __name__ == "__main__":
    fp=Path("input.txt")
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    st_time=perf_counter()
    logging.info(f"Total scratchcard count is: {main(fp)}")
    end_time=perf_counter()
    logging.info(f"Approximate time of execution: {end_time-st_time} s")