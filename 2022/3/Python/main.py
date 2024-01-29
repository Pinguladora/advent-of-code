import string

def split_in_chunks(string: str, parts: int) -> tuple[set, ...]:
    str_size=len(string)
    chunk_size=str_size // parts
    chunks = [set(string[i:i + chunk_size]) for i in range(0, str_size, chunk_size)]
    # Adjust the last chunk if required
    if str_size % parts != 0:
        chunks[-1].update(string[parts * chunk_size:])
    return chunks

def first_challenge(rucksacks: list[str]) -> int:
    return sum(get_priority(*split_in_chunks(rucksack.strip(), 2)) for rucksack in rucksacks)

def second_challenge(rucksacks: list[str], n:int) -> int:
    priority_sum=0
    num_rucksacks=len(rucksacks)
    for trio in range(0, num_rucksacks, n):
        rucksacks_group=(set(i.strip()) for i in rucksacks[trio:trio+n])
        priority_sum += get_priority(*rucksacks_group)
    return priority_sum


def get_priority(*items_groups: tuple[set, ...]) ->int:
    item=set.intersection(*items_groups).pop()
    return string.ascii_letters.index(item)+1

def read_file(filepath: str) -> list[str]:
    with open(filepath, 'rt') as f:
        return f.readlines()

if __name__ == '__main__':
    filepath = "input.txt"
    rucksacks = read_file(filepath)

    # First challenge
    priority_sum=first_challenge(rucksacks)
    print(f"First challenge: the sum of priorities is {priority_sum}")

    # Second challenge
    priority_sum=second_challenge(rucksacks, 3)
    print(f"Second challenge: the sum of priorities is {priority_sum}")
