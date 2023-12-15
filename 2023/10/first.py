from pathlib import Path
import logging
from time import perf_counter

def parse_input(input: str) -> tuple[dict[tuple[int,int], str], tuple[int,int]]:
    grid = {}
    start_pos = (-1,-1)
    for y, line in enumerate(input.split()):
        for x, char in enumerate(line):
            if char != '.':
                grid[(x, y)] = char
            if char == 'S':
                start_pos = (x, y)
    return grid, start_pos

def get_neighbors(pos: tuple[int, int], grid: dict[tuple[int,int],str]):
    x, y = pos
    pipe = grid.get(pos)
    neighbors = []

    # Check for special case where the pipe is 'S'
    if pipe == 'S':
        # Check for vertical connection, like '|'
        if (x, y-1) in grid and (x, y+1) in grid:
            neighbors.extend([(x, y-1), (x, y+1)])
        # Check for horizontal connection, like '-'
        elif (x-1, y) in grid and (x+1, y) in grid:
            neighbors.extend([(x-1, y), (x+1, y)])
        # Check for 'L', 'J', '7', 'F' type connections based on neighbors
        elif (x+1, y) in grid and (x, y-1) in grid: # acts like 'L'
            neighbors.extend([(x, y-1), (x+1, y)])
        elif (x-1, y) in grid and (x, y-1) in grid: # acts like 'J'
            neighbors.extend([(x, y-1), (x-1, y)])
        elif (x-1, y) in grid and (x, y+1) in grid: # acts like '7'
            neighbors.extend([(x, y+1), (x-1, y)])
        elif (x+1, y) in grid and (x, y+1) in grid: # acts like 'F'
            neighbors.extend([(x, y+1), (x+1, y)])
    else:
        if pipe in "|":
            neighbors.extend([(x, y-1), (x, y+1)])
        if pipe in "-":
            neighbors.extend([(x-1, y), (x+1, y)])
        if pipe == 'L':
            neighbors.extend([(x, y-1), (x+1, y)])
        if pipe == 'J':
            neighbors.extend([(x, y-1), (x-1, y)])
        if pipe == '7':
            neighbors.extend([(x, y+1), (x-1, y)])
        if pipe == 'F':
            neighbors.extend([(x, y+1), (x+1, y)])

    return (n for n in neighbors if n in grid)

# Traverse the loop starting from 'S'
def find_farthest_point(grid: dict[tuple[int,int],str], 
                        start_pos: tuple[int, int]) -> int:
    visited = set()
    queue = [(start_pos, 0)]
    max_distance = 0

    while queue:
        current_pos, distance = queue.pop(0)
        if current_pos not in visited:
            visited.add(current_pos)
            max_distance = max(max_distance, distance)
            for neighbor in get_neighbors(current_pos, grid):
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))

    return max_distance

def main(filepath: Path):
    with open(filepath, 'r') as f:
        grid, start_pos = parse_input(f.read())
    return find_farthest_point(grid, start_pos)

if __name__ == '__main__':
    fp=Path("input.txt")
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    st_time=perf_counter()
    logging.info(f"Farthest point from start is {main(fp)} steps away")
    end_time=perf_counter()
    logging.info(f"Approximate time of execution: {end_time-st_time} s")