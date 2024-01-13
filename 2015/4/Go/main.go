package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"strings"
	"sync"
	"sync/atomic"
)

func lowestNumberMd5Hash(secretKey string, predicate string) int64 {
	numGoroutines := 20
	var wg sync.WaitGroup
	found := make(chan bool)
	minNumber := int64(^uint64(0) >> 1) // Max int64 value

	for i := 0; i < numGoroutines; i++ {
		wg.Add(1)
		go func(start int) {
			defer wg.Done()
			for j := start; ; j += numGoroutines {
				select {
				case <-found:
					return
				default:
					data := fmt.Sprintf("%s%d", secretKey, j)
					hash := md5.Sum([]byte(data))
					hashStr := hex.EncodeToString(hash[:])

					if strings.HasPrefix(hashStr, predicate) {
						currentMin := atomic.LoadInt64(&minNumber)
						if int64(j) < currentMin {
							atomic.StoreInt64(&minNumber, int64(j))
						}
						found <- true
						return
					}
				}
			}
		}(i)
	}

	wg.Wait()
	return minNumber
}

func main() {
	secretKey := "iwrupvqb"
	// First challenge
	predicate := "00000"
	fmt.Printf("Lowest number found for %s: %d\n", predicate, lowestNumberMd5Hash(secretKey, predicate))
	// Second challenge
	predicate = "000000"
	fmt.Printf("Lowest number found for %s: %d\n", predicate, lowestNumberMd5Hash(secretKey, predicate))

}
