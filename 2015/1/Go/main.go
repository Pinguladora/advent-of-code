package main

import (
	"errors"
	"fmt"
	"os"
)

func calcFloor(content string) int {
	floor := 0
	// Standard loop wont work unless converted to a rune array, as strings are byte sequences,
	// thing like "a£c" contains 4 bytes not 3
	// A for-range loop will work too
	runeContent := []rune(content)
	for i := 0; i < len(runeContent); i++ {
		if content[i] == '(' {
			floor++
		} else {
			floor--
		}
	}
	return floor
}

func calcBasementEnteringPos(content string) (*int, error) {
	floor := 0
	var pos *int
	var val int

	for idx, char := range content {
		if char == '(' {
			floor++
		} else if char == ')' {
			floor--
		}
		if floor == -1 {
			val = idx + 1
			pos = &val
			return pos, nil
		}
	}
	return nil, errors.New("unable to enter basement")
}

func readFileContents(filepath string) (string, error) {
	content, err := os.ReadFile(filepath)
	if err != nil {
		return "", err
	}
	return string(content), nil
}

func main() {
	filepath := "input.txt"
	content, err := readFileContents(filepath)
	if err != nil {
		fmt.Printf("Unable to read the file %s: %s\n", filepath, err)
		return
	}
	// First challenge
	floor := calcFloor(content)
	fmt.Printf("The floor Stanta needs to reach is %d\n", floor)
	// Second challenge
	basementPos, err := calcBasementEnteringPos(content)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Printf("The position of the character to enter the basement is: %d\n", *basementPos)

	}
}
