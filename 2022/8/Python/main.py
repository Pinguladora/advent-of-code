# You can solve in at least 4 ways:
# 1. Classic matrix grid approach, compare each digit with adjancent cols and rows. Not efficient.
# 2. Matrix substraction approach, substract inner rows and columns from the edges. If it results
# in a positive number then the tree is visible. More efficient, complex.
# 3. Ray tracing algorithm, im not even gonna explain it. Too complex, might work but is an overkill.
# 4. Dynamic programming approach (the one we are doing)
# Matrices which store maximun height seen so far for each row and column till reaching the grid
# Determine visibility by comparing heights

def count_visible_trees(grid: list[list[int]]) -> int:
    # We suppose grids are at the very least regulars (a matrix for simplicity)
    rows, cols = len(grid), len(grid[0])
    # Matrices for each direction
    top, bottom, left, right = [[[0] * cols for _ in range(rows)] for _ in range(4)]
    # Populate the matrices
    for r in range(rows):
        for c in range(cols):
            top[r][c] = max(top[r - 1][c], grid[r][c]) if r > 0 else grid[r][c]
            left[r][c] = max(left[r][c - 1], grid[r][c]) if c > 0 else grid[r][c]

    for r in range(rows - 1, -1, -1):
        for c in range(cols - 1, -1, -1):
            bottom[r][c] = max(bottom[r + 1][c], grid[r][c]) if r < rows - 1 else grid[r][c]
            right[r][c] = max(right[r][c + 1], grid[r][c]) if c < cols - 1 else grid[r][c]

    # Count visible trees
    visible_trees = (rows + cols) * 2 - 4  # Perimeter trees excluding corners to avoid counting them twice
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            # From the highest ones, check if it's taller than the shortest one
            if grid[r][c] > min(top[r - 1][c], bottom[r + 1][c], left[r][c - 1], right[r][c + 1]):
                visible_trees += 1

    return visible_trees

def max_scenic_score(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    highest_score = 0

    def view_distance(r: int, c: int, dr: int, dc: int) -> int:
        distance = 0
        tree_height = grid[r][c]
        r += dr
        c += dc
        while 0 <= r < rows and 0 <= c < cols:
            distance += 1
            if grid[r][c] >= tree_height:
                break
            r += dr
            c += dc
        return distance

    for r in range(rows):
        for c in range(cols):
            up = view_distance(r, c, -1, 0)
            down = view_distance(r, c, 1, 0)
            left = view_distance(r, c, 0, -1)
            right = view_distance(r, c, 0, 1)
            score = up*down*left*right
            highest_score = max(highest_score, score)
    return highest_score

def generate_tree_grid(filepath: str) -> list[list[int]]:
    with open(filepath, "rt") as f:
        return [list(map(int, line.strip())) for line in f]

if __name__ == "__main__":
    filepath = "input.txt"

    grid=generate_tree_grid(filepath)

    # First challenge
    visible_trees=count_visible_trees(grid)
    print(f"{visible_trees} trees are visible from outside the grid")

    # Second challenge
    scenic_score=max_scenic_score(grid)
    print(f"{scenic_score} is the highest scenic score possible")