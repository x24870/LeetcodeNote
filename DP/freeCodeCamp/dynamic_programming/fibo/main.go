package main

import "fmt"

// without memo
// time: O(2^n)
// space: O(n)
func fibo(num int) int {
	if num < 2 {
		return num
	}
	return fibo(num-2) + fibo(num-1)
}

// with memo
// time: O(n)
// space: O(n)
func fiboMemo(num int, memo map[int]int) int {
	if m, ok := memo[num]; ok {
		return m
	}

	if num < 2 {
		return num
	}

	memo[num] = fiboMemo(num-1, memo) + fiboMemo(num-2, memo)
	return memo[num]
}

// tabulation
// time complexity: O(n)
// space complexity: O(n)
func fiboTable(num int) int {
	// initialize fibo[0]
	s := make([]int, num+1)
	// initialize fibo[1]
	s[1] = 1

	for i := 0; i < len(s); i++ {
		if (i + 1) < len(s) {
			s[i+1] += s[i]
		}
		if (i + 2) < len(s) {
			s[i+2] += s[i]
		}
	}
	return s[num]
}

func main() {
	fmt.Println(fibo(20)) // 6765
	memo := make(map[int]int)
	fmt.Println(fiboMemo(20, memo)) // 6765
	fmt.Println(fiboMemo(50, memo)) // 12586269025

	fmt.Println(fiboTable(20))
}
