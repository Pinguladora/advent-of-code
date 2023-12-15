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

def get_loop_boundary(grid, start_pos):
    visited = set()
    boundary = []
    current_pos = start_pos

    while True:
        visited.add(current_pos)
        boundary.append(current_pos)
        neighbors = list(get_neighbors(current_pos, grid))

        # Find the next tile in the loop that hasn't been visited
        next_pos = next((n for n in neighbors if n not in visited and grid.get(n) != '.'), None)
        if next_pos is None:  # If no unvisited neighbors, loop is complete
            break

        current_pos = next_pos

    return boundary

def is_inside_loop(boundary, x, y):
    intersections = 0
    for i in range(len(boundary)):
        x1, y1 = boundary[i]
        x2, y2 = boundary[(i + 1) % len(boundary)]

        if y1 == y2 and y == y1:  # Horizontal segment at the same y level
            if min(x1, x2) <= x <= max(x1, x2):
                return True

        if y > min(y1, y2) and y <= max(y1, y2):
            intersect_x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < intersect_x:
                intersections += 1

    return intersections % 2 == 1

def count_enclosed_tiles(grid):
    start_pos = next(pos for pos, pipe in grid.items() if pipe == 'S')
    boundary = get_loop_boundary(grid, start_pos)
    max_x = max(x for x, _ in grid.keys())
    max_y = max(y for _, y in grid.keys())

    enclosed_tiles = 0
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if is_inside_loop(boundary, x, y) and grid.get((x, y), '.') == '.':
                enclosed_tiles += 1

    return enclosed_tiles


def main(filepath: Path):
    with open(filepath, 'r') as f:
        grid, _ = parse_input(f.read())
    # boundary = get_loop_boundary(grid, next(pos for pos, pipe in grid.items() if pipe == 'S'))
    return count_enclosed_tiles(grid)

if __name__ == '__main__':
    fp=Path("example2.txt")
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    st_time=perf_counter()
    logging.info(f"There are {main(fp)} enclosed tiles")
    end_time=perf_counter()
    logging.info(f"Approximate time of execution: {end_time-st_time} s")