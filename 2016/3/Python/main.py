def is_triangle(triangle: list[int]) -> bool:
    a, b, c = sorted(triangle)
    return True if a+b>c else False

#  Challenge 1
def calc_possible_triangles_by_rows(triangles: list[list[int]]) -> int:
    return sum(1 for t in triangles if is_triangle(t))

# Challenge 2
def calc_possible_triangles_by_cols(triangles: list[list[int]]) -> int:
    return sum(1 for col in zip(*triangles) for sides in range(0, len(col),3) if is_triangle(col[sides:sides+3]))

def read_input(filepath: str) -> list[list[int]]:
    with open(filepath, 'rt') as f:
        return [list(map(int, line.split())) for line in f]

if __name__ == "__main__":
    filepath="input.txt"
    triangle_list=read_input(filepath)
    
    # First challenge
    possible_triangles=calc_possible_triangles_by_rows(triangle_list)
    print(f"First challenge: there are {possible_triangles} possible triangles")

    # Second challenge
    possible_triangles=calc_possible_triangles_by_cols(triangle_list)
    print(f"Second challenge: there are {possible_triangles} possible triangles")