import math

SNAFU_TO_DECIMAL={"=": -2 , "-": -1, "0": 0, "1": 1, "2": 2}

def decimal_to_snafu(num: int) -> str:
    if num == 0:
        return '0'
    
    snafu = list(SNAFU_TO_DECIMAL.keys())
    snafu_num = []
    while num != 0:
        num, remainder = divmod(num, 5)
        # SNAFU's range (-2 to 2), 5 values
        if remainder > 2:
            remainder -= 5
            num += 1
        elif remainder < -2:
            remainder += 5
            num -= 1
        # Shift from [-2,-1,0,1,2] to [0,1,2,3,4] for index access
        snafu_num.insert(0, snafu[remainder + 2])
    return ''.join(snafu_num)

def snafu_to_decimal(num: str) -> int:
    return sum(SNAFU_TO_DECIMAL[char] * math.pow(5, index) for index, char in enumerate(num[::-1]))

def main(filepath: str) -> int:
    decimal_sum=0
    with open(filepath, 'rt') as f:
        [decimal_sum := decimal_sum + snafu_to_decimal(line.rstrip()) for line in f]
    decimal_sum = int(decimal_sum)
    return decimal_to_snafu(decimal_sum)

if __name__ == '__main__':
    fp="input.txt"
    solution=main(fp)
    print(f"The SNAFU number needed to supply to Bob console is {solution}")