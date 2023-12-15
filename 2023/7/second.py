from pathlib import Path
import logging
from time import perf_counter
from collections import Counter

# ORDER_MAP = {char: i for i, char in enumerate('AKQT98765432J')}
# J is now the weakest
ORDER_MAP = {char: i for i, char in enumerate('AKQT98765432J')}  
HAND_TYPES = [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]

# def process_hand(hand: str, bid: str) -> tuple[int, list[int], int]:
#     """Process each hand and return a tuple for sorting."""
#     count=Counter(hand)
#     most_common_card=count.most_common(1)
#     if most_common_card[0][0] == 'J' and most_common_card[0][1] == 5:
#         search = [5]
#     else:
#         if count['J']:
#             count[most_common_card[0]]+=count.pop('J')
#         search=sorted([v for _, v in count.items()], reverse=True)
#     return (HAND_TYPES.index(search), [ORDER_MAP.get(card) for card in hand], int(bid))

def calc_total_bids_winning_with_jokers(lines: list[str]) -> list[int]:
    hands = [process_hand(*line.split()) for line in lines]
    hands.sort(reverse=True)
    return (rank * hand[-1] for rank, hand in enumerate(hands, start=1))

def process_hand(hand: str, bid: str) -> tuple[int, list[int], int]:
    count = Counter(hand)
    joker_count = count['J']

    # Special case: All cards are jokers
    if joker_count == len(hand):
        return (HAND_TYPES.index([5]), [ORDER_MAP['J']] * joker_count, int(bid))

    # Remove jokers for now
    if joker_count:
        del count['J']

    # Find the best use of jokers
    best_hand = None
    best_hand_type = None
    for card, num in count.items():
        temp_count = count.copy()
        temp_count[card] += joker_count
        temp_hand_type = sorted(temp_count.values(), reverse=True)
        if not best_hand_type or HAND_TYPES.index(temp_hand_type) > HAND_TYPES.index(best_hand_type):
            best_hand = temp_hand_type
            best_hand_type = temp_hand_type

    # If jokers don't make a better hand, augment the count of the most common card
    if not best_hand:
        most_common_card, most_common_num = count.most_common(1)[0]
        count[most_common_card] += joker_count
        best_hand = sorted(count.values(), reverse=True)

    return (HAND_TYPES.index(best_hand), [ORDER_MAP.get(card) for card in hand], int(bid))

def main(filepath: Path) -> int:
    with open(filepath, 'r') as f:
       return sum(calc_total_bids_winning_with_jokers(f.readlines()))

if __name__ == "__main__":
    fp=Path("input.txt")
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    st_time=perf_counter()
    logging.info(f"Total winnings are: {main(fp)}")
    end_time=perf_counter()
    logging.info(f"Approximate time of execution: {end_time-st_time} s")
