package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func convertToIntArray(array []string) ([]int, error) {
	intArray := make([]int, len(array))
	for idx, str := range array {
		num, err := strconv.Atoi(str)
		if err != nil {
			return nil, err
		}
		intArray[idx] = num
	}
	return intArray, nil
}
func parseLine(line string) ([]int, error) {
	line = strings.TrimSpace(line)
	parts := strings.Split(line, "x")
	if len(parts) != 3 {
		return nil, fmt.Errorf("three dimensional string was expected, got %d instead", len(parts))
	}
	return convertToIntArray(parts)

}

func calcPresentWrapperPaper(length int, width int, height int) int {
	bottomTopDim := length * width
	sideDim := width * height
	frontDim := height * length
	surfaceArea := 2*bottomTopDim + 2*sideDim + 2*frontDim
	smallestSide := min(bottomTopDim, sideDim, height*length)
	return surfaceArea + smallestSide
}

func readFileAndCalc(filepath string) (int, int, error) {
	file, err := os.Open(filepath)
	if err != nil {
		fmt.Println("Error opening file", err)
		return 0, 0, err
	}
	defer file.Close()

	totalPaperNeeded := 0  // First challenge
	totalRibbonNeeded := 0 // Second challenge

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		values, err := parseLine(line)
		if err != nil {
			return 0, 0, err
		}
		totalPaperNeeded += calcPresentWrapperPaper(values[0], values[1], values[2])
		totalRibbonNeeded += calcRibbonNeeded(values[0], values[1], values[2])
	}
	return totalPaperNeeded, totalRibbonNeeded, nil
}

func calcRibbonNeeded(length int, width int, height int) int {
	dimensions := []int{length, width, height}
	sort.Ints(dimensions)
	// Sum of the two smallest sides
	smallestPerimeter := 2 * (dimensions[0] + dimensions[1])
	cubicVolume := length * width * height
	return smallestPerimeter + cubicVolume
}

func main() {
	filepath := "input.txt"
	totalPaperNeeded, totalRibbonNeeded, err := readFileAndCalc(filepath)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	fmt.Printf("Challenge 1: %d square feets of wrapping paper needed\n", totalPaperNeeded)
	fmt.Printf("Challenge 2: %d feets of ribbon needed\n", totalRibbonNeeded)
}
