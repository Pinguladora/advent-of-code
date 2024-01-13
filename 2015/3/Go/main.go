package main

import (
	"fmt"
	"os"
)

type IntTuple struct {
	X int
	Y int
}

func firstChallenge(instructions string, movesMap map[rune]IntTuple) int {
	x, y := 0, 0
	// Initialize 'set' of tuples with starting position (0,0)
	// housesVisited := make(map[IntTuple]bool)
	housesVisited := map[IntTuple]bool{
		{0, 0}: true,
	}
	for _, direction := range instructions {
		move := movesMap[direction]
		x += move.X
		y += move.Y
		housesVisited[IntTuple{x, y}] = true
	}
	return len(housesVisited)
}

func unionOfSets(set1, set2 map[IntTuple]bool) map[IntTuple]bool {
	// Pre-allocate the result map with the larger size of the two sets
	maxSize := len(set1)
	if len(set2) > maxSize {
		maxSize = len(set2)
	}
	res := make(map[IntTuple]bool, maxSize)

	for k := range set1 {
		res[k] = true
	}
	for k := range set2 {
		res[k] = true
	}
	return res
}

func secondChallenge(instructions string, movesMap map[rune]IntTuple) int {
	sx, sy := 0, 0
	housesVisitedBySanta := map[IntTuple]bool{
		{0, 0}: true,
	}
	rx, ry := 0, 0
	housesVisitedByRoboSanta := map[IntTuple]bool{
		{0, 0}: true,
	}
	for i, direction := range instructions {
		move := movesMap[direction]
		if i%2 == 0 {
			sx += move.X
			sy += move.Y
			housesVisitedBySanta[IntTuple{sx, sy}] = true
		} else {
			rx += move.X
			ry += move.Y
			housesVisitedByRoboSanta[IntTuple{rx, ry}] = true
		}

	}
	res := unionOfSets(housesVisitedBySanta, housesVisitedByRoboSanta)
	return len(res)
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
	movesMap := map[rune]IntTuple{
		'^': {0, 1},
		'v': {0, -1},
		'<': {-1, 0},
		'>': {1, 0},
	}
	content, err := readFileContents(filepath)
	if err != nil {
		fmt.Printf("Unable to read the file %s: %s\n", filepath, err)
		return
	}
	housesWithPresentF := firstChallenge(content, movesMap)
	fmt.Printf("Challenge 1: At least %d houses receive 1 present\n", housesWithPresentF)

	housesWithPresentS := secondChallenge(content, movesMap)
	fmt.Printf("Challenge 2: At least %d houses receive 1 present\n", housesWithPresentS)
}
