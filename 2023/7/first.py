from pathlib import Path
import logging
from time import perf_counter
from collections import Counter

# def calc_total_bids_winning(lines: list[str]) -> int:
#     size=len(lines)
#     hands = [0]*size
#     for i, line in enumerate(lines):
#         cards, bid = line.split()
#         type_of_hand=HAND_TYPES.index(sorted([v for _,v in Counter(cards).items()], reverse=True))
#         hands[i] = (type_of_hand, list(map(ORDER_MAP.get, cards)), int(bid))
#     hands.sort(reverse=True)
#     return [rank * hand[-1] for rank, hand in enumerate(hands, start=1)]

ORDER_MAP = {char: i for i, char in enumerate('AKQJT98765432')}
HAND_TYPES = [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]

def process_hand(hand: str, bid: str) -> tuple[int, list[int], int]:
    """Process each hand and return a tuple for sorting."""
    type_of_hand = HAND_TYPES.index(sorted([v for _, v in Counter(hand).items()], reverse=True))
    return (type_of_hand, [ORDER_MAP.get(card) for card in hand], int(bid))

def calc_total_bids_winning(lines: list[str]) -> list[int]:
    hands = [process_hand(*line.split()) for line in lines]
    hands.sort(reverse=True)
    return (rank * hand[-1] for rank, hand in enumerate(hands, start=1))

def main(filepath: Path) -> int:
    with open(filepath, 'r') as f:
       return sum(calc_total_bids_winning(f.readlines()))

if __name__ == "__main__":
    fp=Path("input.txt")
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    st_time=perf_counter()
    logging.info(f"Total winnings are: {main(fp)}")
    end_time=perf_counter()
    logging.info(f"Approximate time of execution: {end_time-st_time} s")