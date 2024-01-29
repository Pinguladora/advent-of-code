from time import perf_counter

def elf_with_most_calories(groups_sum: list[int]) -> int:
    return max(groups_sum)

def top_three_elves_calories(groups_sum: list[int]) -> int:
    groups_sum.sort(reverse=True)
    return sum(groups_sum[:3])

def sum_per_group(items: str) -> list[int]:
    return [sum(map(int, group.split('\n'))) for group in items.split('\n\n')]

def read_file(filepath: str) -> str:
    with open(filepath) as f:
        return f.read().strip()

if __name__ == "__main__":
    filepath = "input.txt"
    items=read_file(filepath)
    sums=sum_per_group(items)

    # First challennge
    st=perf_counter()
    out=elf_with_most_calories(sums)
    end=perf_counter()
    print(f"The elf with most calories is carrying: {out} calories")
    print("Execution time:", end-st)

    # Second challenge
    st=perf_counter()
    out=top_three_elves_calories(sums)
    end=perf_counter()
    print(f"The top three elves with most calories are carrying: {out} calories")
    print("Execution time:", end-st)