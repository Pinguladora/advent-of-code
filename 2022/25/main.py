import math

def main(filepath: str) -> int:
    digit_dict={"=": -2 , "-": -1, "0": 0, "1": 1, "2": 2}
    sum=0
    with open(filepath, 'r') as f:
        for line in f:
            [sum := sum + digit_dict[char] * math.pow(5, index) for index, char in enumerate(line.rstrip()[::-1])]
    return int(sum)

if __name__ == '__main__':
    out=main(r"input.txt")
    print(out)