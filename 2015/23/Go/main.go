package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type InstructionLine struct {
	instruction string
	register    string
	offset      int
}

func parseLine(line string) (InstructionLine, error) {
	line = strings.TrimSpace(strings.ReplaceAll(line, ",", ""))
	parts := strings.Split(line, " ")
	instr := InstructionLine{instruction: parts[0]}
	// Jmp instruction is different
	var offset string = "0"
	if parts[0] == "jmp" {
		offset = parts[1]
	} else { // Any other instruction
		instr.register = parts[1]
		if len(parts) == 3 {
			offset = parts[2]
		}
	}
	parsedOffset, err := strconv.Atoi(offset)
	if err != nil {
		return InstructionLine{}, fmt.Errorf("error parsing offset %s: %v", offset, err)
	}
	instr.offset = parsedOffset
	return instr, nil
}

func applyInstruction(line InstructionLine, registerVal int, position int) (int, int) {
	switch line.instruction {
	case "hlf":
		registerVal /= 2
	case "tpl":
		registerVal *= 3
	case "inc":
		registerVal++
	case "jie":
		if registerVal%2 == 0 {
			position += line.offset
			return registerVal, position
		}
	case "jio":
		if registerVal == 1 {
			position += line.offset
			return registerVal, position
		}
	}
	position++
	return registerVal, position
}

func execInstructions(instructions []InstructionLine, registers map[string]int) map[string]int {
	i := 0
	for i >= 0 && i < len(instructions) {
		currentInstruction := instructions[i]
		if currentInstruction.instruction == "jmp" {
			i += currentInstruction.offset
			continue
		}
		registers[currentInstruction.register], i = applyInstruction(currentInstruction,
			registers[currentInstruction.register], i)
	}
	return registers
}

func readFile(filepath string) ([]InstructionLine, error) {
	file, err := os.Open(filepath)
	if err != nil {
		return nil, fmt.Errorf("opening file %s: %v", filepath, err)
	}
	defer file.Close()

	var instructions = []InstructionLine{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		parsed, err := parseLine(scanner.Text())
		if err != nil {
			return nil, fmt.Errorf("unable to parse line %v", err)
		}
		instructions = append(instructions, parsed)
	}
	if err := scanner.Err(); err != nil {
		return nil, fmt.Errorf("scanning file %s: %v", filepath, err)
	}
	return instructions, nil
}

func main() {
	filepath := "input.txt"
	registers := make(map[string]int, 2)
	instructions, err := readFile(filepath)
	if err != nil {
		fmt.Printf("Unable to read the file %s:\n %v\n", filepath, err)
		return
	}
	registers["a"], registers["b"] = 0, 0
	registers = execInstructions(instructions, registers)
	fmt.Println("First challenge: the value for register b is", registers["b"])

	registers["a"], registers["b"] = 1, 0
	registers = execInstructions(instructions, registers)
	fmt.Println("Second challenge: the value for register b is", registers["b"])
}
