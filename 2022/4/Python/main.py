
def fully_contains(fmin: int, fmax: int, smin: int, smax: int) -> int:
    return int((fmin <= smin and fmax >= smax) or (smin <= fmin and smax >= fmax))


def overlaps(fmin: int, fmax: int, smin: int, smax: int) -> int:
    return int(fmax >= smin and smax >= fmin)

def main(filepath: str) -> tuple[int, int]:
    fsum, ssum = 0, 0
    with open(filepath, 'rt') as f:
        for line in f.readlines():
            first_pair, second_pair = line.strip().split(',')
            frange_min, frange_max = map(int, first_pair.split('-'))
            srange_min, srange_max = map(int, second_pair.split('-'))
            fsum += fully_contains(frange_min, frange_max, srange_min, srange_max)
            ssum += overlaps(frange_min, frange_max, srange_min, srange_max)
    return fsum, ssum


if __name__ == "__main__":
    filepath = "input.txt"
    fsol, ssol = main(filepath)
    # First challenge
    print(f"First challenge: there are {fsol} pairs which fully contains other")
    
    # Second challenge
    print(f"Second challenge: there are {ssol} pairs which overlaps")