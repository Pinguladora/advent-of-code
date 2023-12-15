from pathlib import Path
import logging
from time import perf_counter
from itertools import cycle

from math import gcd

# This is a naive and inefficient implementation which would take hours even days
def calc_steps_required(lines: list[str]) -> int:
    instructions=lines.pop(0).strip()
    lines.pop(0) # Remove empty line
    binary_tree: dict[str, tuple(str, str)]={}
    for line in lines:
        root, _ , left_node, right_node = line.strip().split()
        binary_tree[root] = left_node[1:4], right_node[:3]
    # Starting positions
    current_nodes=[k for k in binary_tree if k.endswith('A')]
    steps=0
    for direction in cycle(instructions):
        steps+=1
        current_nodes: list[str] = [binary_tree[i][0] if direction == 'L' else binary_tree[i][1] for i in current_nodes]
        if all(i.endswith('Z') for i in current_nodes):
            break
    return steps

def lcm(a: int, b: int) -> int:
    return abs(a*b) // gcd(a, b)

def calc_lcm_cycle_lengths(lengths: list[int]) -> int:
    current_lcm = lengths[0]
    for length in lengths[1:]:
        current_lcm = lcm(current_lcm, length)
    return current_lcm

# Better approach using LCM with the cycle length (steps) of each Ghost route
# until they reach an XXZ
def calc_steps_required(lines: list[str]) -> int:
    instructions=lines.pop(0).strip()
    lines.pop(0) # Remove empty line
    binary_tree: dict[str, tuple(str, str)]={}
    for line in lines:
        root, _ , left_node, right_node = line.strip().split()
        binary_tree[root] = left_node[1:4], right_node[:3]
    # Starting positions
    current_nodes=[k for k in binary_tree if k.endswith('A')]
    instructions_size=len(instructions)
    cycle_lengths=[0]*len(current_nodes)
    for i, start_node in enumerate(current_nodes):
        current_node = start_node
        steps = 0
        while not current_node.endswith('Z'):
            current_node = binary_tree[current_node][0 if instructions[steps % instructions_size] == 'L' else 1]
            steps += 1
        cycle_lengths[i]=steps
    return calc_lcm_cycle_lengths(cycle_lengths)

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