import re
# Seems like LCM but it's not! You can't LCM times as that is what you are searching for
# and you can't apply to cycles lengths either as you need to account for disk starting
# positions and ticks and additionaly to the capsule travel time

PATTERN=re.compile(r"\d+")

def find_capsule_drop_time(disc_data: list[tuple[int]]) -> int:
    time = 0
    while True: 
        time +=1
        if all([(start_pos+time+i+1) % positions == 0 
                   for i, (_, positions, _, start_pos) in enumerate(disc_data)]):
            break
    return time
    
def read_disc_info(filepath: str) -> list[tuple[int]]:
    disc_data = []
    with open(filepath, 'rt') as f:
        for line in f:
            disc_values=re.findall(PATTERN, line.rstrip())
            disc_data.append(tuple(map(int, disc_values)))
    return disc_data

if __name__ == "__main__":
    filepath="input.txt"

    disc_data=read_disc_info(filepath)

    # First challenge
    drop_time=find_capsule_drop_time(disc_data)
    print(f"First challenge: the first time you can press the button to get a capsule is {drop_time}")
    
    # Second challenge
    disc_data.append((-1, 11, 0, 0))
    drop_time=find_capsule_drop_time(disc_data)
    print(f"Second challenge: the first time you can press the button to get a capsule is {drop_time}")