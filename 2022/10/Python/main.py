CYCLES_TO_CHECK = [20, 60, 100, 140, 180, 220]

def read_instructions(filepath: str) -> list[str]:
    with open(filepath, "rt") as f:
        return f.readlines()

# Dirty approach 
def calc_signal_strength(instructions: list[str]) -> int:
    x = 1
    cycle = 1
    signal_strength = [cycle]*CYCLES_TO_CHECK[-1]
    while cycle < CYCLES_TO_CHECK[-1]:
        for instruction in instructions:
            op, *value = instruction.split()
            if op == "noop":
                cycle +=1
                signal_strength[cycle-1:cycle] = x, x 
            else:
                cycle +=2
                x += int(value[0])
                signal_strength[cycle-2:cycle] = x, x 
    return sum(signal_strength[i-2]*i for i in CYCLES_TO_CHECK)

# A cleaner approach
def calc_signal_strength(instructions: list[str]) -> int:
    x = 1
    cycle = 1
    signal_strength_sum  = 0
    max_cycle = CYCLES_TO_CHECK[-1]
    for instruction in instructions:
        op, *value = instruction.split()
        if op == "noop":
            cycle += 1
        else:
            value = int(value[0])
            # Increment cycle first as the addx takes two cycles
            cycle += 1
            if cycle in CYCLES_TO_CHECK:
                signal_strength_sum += x * cycle
            cycle += 1
            x += value
        if cycle in CYCLES_TO_CHECK:
            signal_strength_sum += x * cycle
        if cycle > max_cycle:
            break
    return signal_strength_sum

if __name__ == "__main__":
    filepath = "input.txt"
    instructions=read_instructions(filepath)

    # First challenge
    signal_strength=calc_signal_strength(instructions)
    print(f"The sum of the six signal strengths is {signal_strength}")