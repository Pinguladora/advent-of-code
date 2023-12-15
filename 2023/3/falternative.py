import re
from pathlib import Path
# import string

# There is no given set of symbols for the input so we suppose standard punctuation
# PUNTUACTION_SYMBOLS=frozenset(string.punctuation.replace('.', '*'))

# def sum_part_numbers(engine_schematic: list[str], maxtrix_size: int) -> int:
#     symbol_pattern=re.compile(r'[^\w\s.]')
#     num_pattern=re.compile(r'(\d+)')
#     sum = 0

#     def find_adjacent_numbers(line: str, prev_line: str, next_line: str) -> int:
#         sum = 0
#         # print(prev_line)
#         # print(current_line)
#         # print(next_line, '\n')
#         for symbol_match in symbol_pattern.finditer(line):
#             symbol_start_idx = symbol_match.start()-1 # For prev line and its diagonal
#             symbol_end_idx = symbol_match.end()+1 # For next line and its diagonal
#             # Check current line
#             ## Check left and right of the number group
#             left=num_pattern.search(line[symbol_start_idx])
#             right=num_pattern.search(line[symbol_end_idx-1])
#             # print(left, right, '\n')
#             if left:
#                 sum += int(left.group())
#             if right:
#                 sum += int(right.group())
#             # print(sum)
#             # for i in num_pattern.finditer(line):
#             #     if abs(i.start() - symbol_start_idx) <= 1 or abs(i.end() - 1 - symbol_start_idx) <= 1:
#             #         sum += int(i.group())
#             #         # Avoid adding the same number twice as it might adjacent to multiple symbols in the same line
#             #         break  

#             # Check previous and next line
#             # for i in num_pattern.findall(prev_line[symbol_start_idx-maxtrix_size:symbol_end_idx-maxtrix_size]):
#             #     sum += int(i)
#             # print(num_pattern.findall(prev_line))
#             # for i in num_pattern.findall(next_line[maxtrix_size+symbol_start_idx:maxtrix_size+symbol_end_idx]):
#             #     sum += int(i)
#             for adjacent_line in [prev_line, next_line]:
#                 if adjacent_line:
#                     for j in num_pattern.finditer(adjacent_line):
#                         if symbol_start_idx >= j.start() and symbol_start_idx < j.end():
#                             sum += int(j.group())
#                             # Avoid adding the same number twice as it might adjacent to multiple symbols in the same line
#                             break
#         return sum

#     for i in range(0, maxtrix_size, 2):
#         current_line=engine_schematic[i].strip()
#         prev_line=engine_schematic[i-1].strip() if i> 0 else None
#         next_line=engine_schematic[i+1].strip() if i + 1 < maxtrix_size else None # Range is already exclusive

#         # Sum numbers adjacent to symbols in the current and next line
#         sum += find_adjacent_numbers(current_line, prev_line, next_line)
#         if next_line:
#             sum += find_adjacent_numbers(next_line, current_line, engine_schematic[i+2].strip() if i + 2 < maxtrix_size else None)
#     return sum

# def main(filepath: Path) -> int:
#     with open(filepath, 'r') as f:
#        lines=f.readlines()
#        maxtrix_size=len(lines) # Input is a square matrix / grid
#        return sum_part_numbers(lines, maxtrix_size)

# if __name__ == "__main__":
#     fp = Path("input.txt")
#     print(f"Engine schematic sum is: {main(fp)}")

def sum_gear_ratios(engine_schematic: str, matrix_size: int) -> int:
    gear_sum = 0
    for row in range(matrix_size):
        for col in range(matrix_size):
            if engine_schematic[row * matrix_size + col] == '*':
                # Find adjacent part numbers
                adjacent_nums = []
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        adj_row, adj_col = row + dy, col + dx
                        if 0 <= adj_row < matrix_size and 0 <= adj_col < matrix_size:
                            char = engine_schematic[adj_row * matrix_size + adj_col]
                            if char.isdigit():
                                # Trace the whole number
                                number = char
                                # Trace left
                                l = adj_col - 1
                                while l >= 0 and engine_schematic[adj_row * matrix_size + l].isdigit():
                                    number = engine_schematic[adj_row * matrix_size + l] + number
                                    l -= 1
                                # Trace right
                                r = adj_col + 1
                                while r < matrix_size and engine_schematic[adj_row * matrix_size + r].isdigit():
                                    number += engine_schematic[adj_row * matrix_size + r]
                                    r += 1
                                number = int(number)
                                if number not in adjacent_nums:
                                    adjacent_nums.append(number)

                # Calculate gear ratio if exactly two part numbers are found
                if len(adjacent_nums) == 2:
                    gear_sum += adjacent_nums[0] * adjacent_nums[1]

    return gear_sum

class SchematicsReader:
    '''yields frames of three lines in the input file'''
    def __enter__(self):
        self._fh = open('input.txt', 'r')
        return self
    def __exit__(self, *args, **kwargs):
        self._fh.close()
    def __iter__(self):
        fh = self._fh
        lines = [fh.readline(), fh.readline()]
        yield ['.'*len(lines[0])] + lines
        for line in fh:
            lines.append(line)
            yield lines
            lines.pop(0)
        yield lines + ['.'*len(line)]

# P A R T  1
re_number = re.compile('(\d+)')

def is_symbol(line, i):
    return line[i] != '.' and not line[i].isdigit()

with SchematicsReader() as lines:
    part_number_sum = 0
    for (previous, current, next) in lines:
        for match in re_number.finditer(current):
            start = max(0, match.start() - 1)
            stop = min(match.end(), len(current)-2)
            if is_symbol(current, start) or is_symbol(current, stop):
                part_number_sum += int(match.group())
                continue
            for i in range(start, stop+1):
                if is_symbol(previous, i) or is_symbol(next, i):
                    part_number_sum += int(match.group())
                    break
    print(f'Solution 1: {part_number_sum}')
    
# P A R T  2
re_gear = re.compile('(\*)')
with SchematicsReader() as lines:
    gear_ratio_sum = 0
    for (previous, current, next) in lines:
        for match in re_gear.finditer(current):
            adjacent_numbers = []
            for line in [previous, next]:
                for num_match in re_number.finditer(line):
                    if num_match.start()-1 <= match.start() <= num_match.end():
                        adjacent_numbers.append(int(num_match.group()))
            for num_match in re_number.finditer(current):
                if num_match.end() == match.start() or num_match.start() == match.end():
                    adjacent_numbers.append(int(num_match.group()))
            if len(adjacent_numbers) == 2:
                gear_ratio_sum += adjacent_numbers[0] * adjacent_numbers[1]
    
    print(f'Solution 2: {gear_ratio_sum}')

# def main(filepath: Path) -> int:
#     with open(filepath, 'r') as f:
#        lines=f.readlines()
#        maxtrix_size=len(lines) # Input is a square matrix / grid
#        engine_schematic=''.join(lines).replace('\n','')
#        return sum_gear_ratios(engine_schematic, maxtrix_size)

if __name__ == "__main__":
    fp = Path("input.txt")
    # print(f"Engine schematic sum is: {main(fp)}")
