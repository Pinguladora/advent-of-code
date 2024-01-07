<?php

function parseLine($line)
{
    $line = trim($line);
    $parts = explode('x', $line);
    if (count($parts) == 3) {
        return array_map('intval', $parts);
    }
    throw new Exception('Not enough dimensions.');
}

function readFileAndCalc($filePath, $func)
{
    $fileHandler = fopen($filePath, "r");

    if (!$fileHandler) {
        return "Error opening the file! Check it exists and try again";
    }

    $amountNeeded = 0;
    while (($line = fgets($fileHandler)) !== false) {
        list($length, $width, $height) = parseLine($line);
        // $amountNeeded += calcPresentWrapperPaper($length, $width, $height);
        $amountNeeded += $func($length, $width, $height);
    }
    // Close the file handler
    fclose($fileHandler);

    return $amountNeeded;
}

function calcPresentWrapperPaper($length, $width, $height)
{
    $surfaceArea = 2 * $length * $width + 2 * $width * $height + 2 * $height * $length;
    $smallestSide = min($length * $width, $width * $height, $height * $length);

    return $surfaceArea + $smallestSide;

}

function calcTotalPaperNeeded($filePath)
{
    $totalPaperNeeded = readFileAndCalc($filePath, 'calcPresentWrapperPaper');
    echo "Solution: $totalPaperNeeded square feet of wrapping paper is needed\n";
}

calcTotalPaperNeeded('input.txt');

function calcRibbonNeeded($length, $width, $height)
{
    // Find the two smallest dimensions
    $dimensions = [$length, $width, $height];
    sort($dimensions);
    // Sum of the two smallest sides
    $smallestPerimeter = 2 * ($dimensions[0] + $dimensions[1]);
    $cubic_volume = $length * $width * $height;

    return $smallestPerimeter + $cubic_volume;
}
function calcTotalRibbonNeeded($filePath)
{
    $totalRibbonNeeded = readFileAndCalc($filePath, 'calcRibbonNeeded');
    echo "Solution: $totalRibbonNeeded feet of ribbon is needed\n";
}

calcTotalRibbonNeeded('input.txt');

?>