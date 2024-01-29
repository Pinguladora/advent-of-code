
# A and X are rock
# B and Y are paper
# C and Z are scissor

SHAPE_POINTS={"A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3}
WINNER_MATCHS={"X":"C", "Y":"A", "Z":"B"}

def first_challenge(filepath: str) -> int:
    player_score = 0
    for foe_move, player_move in read_strategy(filepath):
        move_score = SHAPE_POINTS[player_move]
        player_score += move_score
        if WINNER_MATCHS[player_move] == foe_move:  # Player wins
            player_score += 6
        elif move_score == SHAPE_POINTS[foe_move]:  # It's a draw
            player_score += 3
    return player_score

# You can just reverse the WINNER_MATCHS dict
LOSER_MATCHS={"A":"Y", "B":"Z", "C":"X"}
FOE_WINNER_MATCHS={"A":"Z", "B":"X", "C":"Y"}

def second_challenge(filepath: str) -> int:
    player_score = 0
    for foe_move, player_move in read_strategy(filepath):
        if player_move == 'Z':  # Player wins
            player_score += 6 + SHAPE_POINTS[LOSER_MATCHS[foe_move]]
        elif player_move == 'Y':  # It's a draw
            player_score += 3 + SHAPE_POINTS[foe_move]
        else:  # Player loses (X)
            player_score += SHAPE_POINTS[FOE_WINNER_MATCHS[foe_move]]
    return player_score

def read_strategy(filepath: str) -> (str, str):
    with open(filepath, mode='rt') as f:
        for line in f.readlines():
            foe_move, player_move = line.strip().split(" ")
            yield foe_move, player_move


filepath="input.txt"
# First challenge
player_score=first_challenge(filepath)
print(f"First challenge: following the strategy, total score would be {player_score}")
# Second challenge
player_score=second_challenge(filepath)
print(f"Second challenge: following the strategy, total score would be {player_score}")