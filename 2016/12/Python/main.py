class Instruction:
    instruction: str
    fregister: str | int
    srgister: str | int

    def __init__(self, instruction: str, fregister: str, sregister: str = None):
        self.instruction = instruction
        self.fregister = int(fregister) if fregister and fregister.lstrip('-+').isdigit() else fregister
        self.sregister = int(sregister) if sregister and sregister.lstrip('-+').isdigit() else sregister

def process_instruction(inst: Instruction, registers: dict[str, str]) -> int:
    instruction = inst.instruction
    if instruction == "cpy":
        registers[inst.sregister]=registers.get(inst.fregister, inst.fregister)
    elif instruction == "inc":
        registers[inst.fregister]+=1
    elif instruction == "dec":
        registers[inst.fregister]-=1
    return registers

def exec_instructions(instructions: list[Instruction], registers: dict[str, str]) -> dict[str, str]:
    i=0
    size=len(instructions)
    while 0 <= i < size:
        current_instruction=instructions[i]
        if current_instruction.instruction == "jnz":
            check_register = current_instruction.fregister
            check_value = registers.get(check_register, check_register)
            if check_value != 0:
                i += registers.get(current_instruction.sregister, current_instruction.sregister)
                continue
        registers = process_instruction(current_instruction, registers)
        i+=1
    return registers

def parse_instruction_line(line: str) -> Instruction:
    line=line.rstrip()
    inst, *vals = line.split()
    return Instruction(inst.strip(), *vals)

def read_assembunny(filepath: str) -> list[Instruction]:
    with open(filepath, 'rt') as f:
        return [parse_instruction_line(line) for line in f]

if __name__ == "__main__":
    filepath="input.txt"
    instructions=read_assembunny(filepath)

    # First challenge
    registers={"a": 0, "b":0, "c":0, "d":0}
    sol=exec_instructions(instructions, registers)
    print(f'First challenge: the value left in register a is {sol["a"]}')

    # Second challenge
    registers["c"]=1
    sol=exec_instructions(instructions, registers)
    print(f'Second challenge: the value left in register a is {sol["a"]}')
    