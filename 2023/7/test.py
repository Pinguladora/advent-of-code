from pathlib import Path
import logging
from time import perf_counter
from collections import Counter

weakest_to_strongest = '23456789TJQKA'
ORDER_MAP = {char: i for i, char in enumerate(weakest_to_strongest)}

# Custom sorting function
def sorting_key(counter):
    # Convert Counter to a list of (card, count) tuples, sorted primarily by count (descending) and secondarily by custom card order
    sorted_items = sorted(counter.items(), key=lambda x: (-x[1], -ORDER_MAP[x[0]]))

    # Construct a sorting key that reflects both count and card order for each character
    sorting_key = []
    for card, count in sorted_items:
        sorting_key.extend([-count] + [-ORDER_MAP[char] for char in card])

    return sorting_key

# Example list of Counters
counters = [Counter({'3': 2, '2': 1, 'T': 1, 'K': 1}), Counter({'5': 3, 'T': 1, 'J': 1}), Counter({'K': 2, '7': 2, '6': 1}), Counter({'T': 2, 'J': 2, 'K': 1}), Counter({'Q': 3, 'J': 1, 'A': 1})]

# RTL Code explanation
# Convert Counters to a list of (card, count) tuples
# Then sort by descending count order followed by card labels if they tie
sorted_counters = sorted(counters, key=lambda c: [( -count, -ORDER_MAP[card_label] ) for card_label, count in sorted(c.items(), key=lambda x: (-x[1], -ORDER_MAP[x[0]]))])

print("Order is:", sorted_counters)

# Forgot the actual important part the Poker hands value
def calc_total_bids_winning(lines:list[str]) -> list[int]:
    size=len(lines)
    ranks=[1]*size
    counters={}
    for i, line in enumerate(lines):
        cards, bids=line.rstrip().split(' ')
        ranks[i] = int(bids)
        counters[i]=Counter(cards).items()
    # RTL Read
    # Convert Counters to a list of (card, count) tuples
    # Then sort by descending count order followed by card labels if they tie
    # Returns a list of the original positions
    sorted_counters = sorted(counters, 
                             key=lambda k: [( -count, -ORDER_MAP[card_label]) for card_label, 
                                                      count in sorted(counters[k], key=lambda x: (-x[1], -ORDER_MAP[x[0]]))])
    return [ranks[i] * (size-idx) for idx, i in enumerate(sorted_counters)]

def classify_hand(hand_count: list[tuple[str, int]]) -> tuple[int, int]:
    """Classify the hand and return its type and sorted card labels."""
    # Assign a score to each type of hand and its strength as (score, card_strength)
    # At most there would be 2 groups of cards labels to compose the type of hand
    if hand_count[0][1] == 5:
        res = (10, [ORDER_MAP[hand_count[0][0]]])  # Five of a kind
    elif hand_count[0][1] == 4:
        res = (9, [ORDER_MAP[hand_count[0][0]]])  # Four of a kind
    elif hand_count[0][1] == 3 and hand_count[1][1] == 2:
        res = (8, [ORDER_MAP[hand_count[0][0]]])  # Full house
    elif hand_count[0][1] == 3:
        res = (6, [ORDER_MAP[hand_count[0][0]]])  # Three of a kind
    elif hand_count[0][1] == 2 and hand_count[1][1] == 2:
        res = (5, sorted([ORDER_MAP[hand_count[0][0]], ORDER_MAP[hand_count[1][0]]], reverse=True))  # Two pair
    elif hand_count[0][1] == 2:
        res = (4, [ORDER_MAP[hand_count[0][0]]])  # One pair
    else:
        res = (3, [ORDER_MAP[c[0]] for c in sorted(hand_count, key=lambda x: -ORDER_MAP[x[0]])])  # High card
    # print(hand_count, res)
    return res

def calc_total_bids_winning(lines: list[str]) -> int:
    size=len(lines)
    hands=[()]*size
    counters=[0]*size
    for i, line in enumerate(lines):
        cards, bids=line.split()
        hands[i] = cards, int(bids)
        counters[i] = Counter(cards).most_common()
    # Sort based on hand strength as [(index, (cards, bid) , ...)]
    # sorted_hands = sorted(enumerate(hands), key=lambda x: (classify_hand(counters[x[0]]), x[0]), reverse=True)
    sorted_hands = sorted(enumerate(hands), key=lambda x: classify_hand(counters[x[0]]), reverse=True)
    return [rank*bid for rank, (_, (_, bid)) in enumerate(sorted_hands, 1)]

def main(filepath: Path) -> int:
    with open(filepath, 'r') as f:
       return sum(calc_total_bids_winning(f.readlines()))

if __name__ == "__main__":
    fp=Path("example.txt")
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    st_time=perf_counter()
    logging.info(f"Total winnings are: {main(fp)}")
    end_time=perf_counter()
    logging.info(f"Approximate time of execution: {end_time-st_time} s")
