from pathlib import Path
import logging
from time import perf_counter
from itertools import cycle

# Problem revolves around a binary tree but can be tackled using a dictionary
# class BinaryTree:
#     def __init__(self, data = None, left = None, right = None):
#         self.left: str | BinaryTree = left
#         self.data: str | BinaryTree = data
#         self.right: str | BinaryTree = right

#     def __str__(self) -> str:
#         return f"{self.data}: ({self.left}, {self.right})"
    
def calc_steps_required(lines: list[str]) -> int:
    instructions=lines.pop(0).strip()
    lines.pop(0) # Remove empty line
    binary_tree={}
    for line in lines:
        root, _ , left_node, right_node = line.strip().split()
        binary_tree[root] = left_node[1:4], right_node[:3]
    # Starting position
    current_node=binary_tree['AAA']
    steps=0
    for direction in cycle(instructions):
        steps+=1
        next_node = current_node[0] if direction == 'L' else current_node[1]
        if next_node == 'ZZZ':
            # Finish!
            break
        current_node = binary_tree[next_node]
    return steps

# More idiomatic approach
def calc_steps_required(lines: list[str]) -> int:
    instructions=lines.pop(0).strip()
    lines.pop(0) # Remove empty line
    binary_tree={}
    for line in lines:
        root, _ , left_node, right_node = line.strip().split()
        binary_tree[root] = left_node[1:4], right_node[:3]
    instructions_size=len(instructions)
    current_node = 'AAA'
    steps = 0
    while current_node != 'ZZZ':
        current_node = binary_tree[current_node][0 if instructions[steps % instructions_size] == 'L' else 1]
        steps += 1
    return steps

def main(filepath: Path) -> int:
    with open(filepath, 'r') as f:
       return calc_steps_required(f.readlines())

if __name__ == "__main__":
    fp=Path("input.txt")
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    st_time=perf_counter()
    logging.info(f"Total steps required are: {main(fp)}")
    end_time=perf_counter()
    logging.info(f"Approximate time of execution: {end_time-st_time} s")