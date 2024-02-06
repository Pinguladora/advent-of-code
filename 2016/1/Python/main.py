# Classic Manhattan distance problem

def update_direction(current_direction: int, turn: str) -> int:
    if turn == "R":
        current_direction = (current_direction + 1) % 4 # As there are 4 directions
    else:  # turn == "L"
        current_direction = (current_direction - 1) % 4
    return current_direction

def calc_hq_distance(moves: list[str]) -> int:
    position = [0, 0]
    # 0: North, 1: East, 2: South, 3: West
    direction = 0
    
    for move in moves:
        move = move.strip()
        turn_direction, blocks = move[0], int(move[1:])
        direction = update_direction(direction, turn_direction)
        
        if direction == 0:  # North
            position[1] += blocks
        elif direction == 1:  # East
            position[0] += blocks
        elif direction == 2:  # South
            position[1] -= blocks
        else:  # West
            position[0] -= blocks
    return abs(position[0]) + abs(position[1])

def calc_hq_real_distance(moves: list[str]) -> int:
    position = (0, 0)
    visisted_positions = {position}
    # 0: North, 1: East, 2: South, 3: West
    direction = 0
    
    for move in moves:
        move = move.strip()
        turn_direction, blocks = move[0], int(move[1:])
        direction = update_direction(direction, turn_direction)
        for _ in range(blocks):
            if direction == 0:  # North
                position = (position[0], position[1] + 1)
            elif direction == 1:  # East
                position = (position[0]+ 1, position[1])
            elif direction == 2:  # South
                position = (position[0], position[1]-1)
            else:  # West
                position = (position[0]-1, position[1])

            if position in visisted_positions:
                return abs(position[0]) + abs(position[1])
            visisted_positions.add(position)

def read_instructions(filepath: str) -> list[str]:
    with open(filepath, 'rt') as f:
        return f.read().split(',')

if __name__ == "__main__":
    filepath="input.txt"
    moves=read_instructions(filepath)
    # First challenge
    distance=calc_hq_distance(moves)
    print(f"Easter Bunny HQ is {distance} blocks away")

    # Second challenge
    distance=calc_hq_real_distance(moves)
    print(f"Easter Bunny HQ is {distance} blocks away")