<?php

// Slowest
// No parallel implementation because of DLL needed not compatible for either Windows and PHP 8.3.1
function lowestNumberMd5Hash($secretKey, $predicate){
    $i=0;
    while (1) {
        $hash = md5("$secretKey$i");
        if (str_starts_with($hash, $predicate)) {
            return $i;
        }
        $i++;
    }
}

// Smart parallel
// Fastest
// As the predicate repeats digits increasing just the number of them, 
// it should at the very least start from last iteration of the previous predicate
// Recommended Linux, WSL2 would do the trick
// Also PHP dev and previous releases of PHP
use parallel\Runtime;
use parallel\Future;

function lowestNumberMd5HashParallel($secretKey, $predicate, $numThreads, $startFrom = 0) {
    $futures = [];
    $runtime = [];

    // Create runtimes for each thread
    for ($i = 0; $i < $numThreads; $i++) {
        $runtime[$i] = new Runtime();
    }

    // Distribute the work across multiple threads
    for ($i = 0; $i < $numThreads; $i++) {
        $futures[$i] = $runtime[$i]->run(function($args) {
            [$secretKey, $predicate, $start, $step] = $args;
            $i = $start;
            while (true) {
                $hash = md5($secretKey . $i);
                if (str_starts_with($hash, $predicate)) {
                    return $i;
                }
                $i += $step;
            }
        }, [[$secretKey, $predicate, $i + $startFrom, $numThreads]]);
    }

    // Wait for the results and find the lowest number
    $result = PHP_INT_MAX;
    foreach ($futures as $future) {
        $value = $future->value();
        if ($value < $result) {
            $result = $value;
        }
    }

    return $result;
}

function main(){
    $secretKey = "iwrupvqb";
    $predicate = "00000";
    // First challenge
    $res = lowestNumberMd5Hash($secretKey, $predicate);
    // $res = lowestNumberMd5HashParallel($secretKey, $predicate, 4);
    echo "Challenge 1: Lowest number found for $predicate: $res\n";
    // Second challenge
    $predicate = "000000";
    $res = lowestNumberMd5Hash($secretKey, $predicate);
    // $res = lowestNumberMd5HashParallel($secretKey, $predicate, $res);
    echo "Challenge 2: lowest number found for $predicate: $res\n";


}

main();
