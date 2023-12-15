from time import perf_counter

def main(filepath: str) -> int:
    with open(filepath) as f:
        lines = f.read().strip()
    return max(sum(map(int, group.split('\n'))) for group in lines.split('\n\n'))
        
if __name__ == "__main__":
    st=perf_counter()
    out=main(r"input.txt")
    end=perf_counter()
    print(out)