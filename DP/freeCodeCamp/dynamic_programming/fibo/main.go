package main

import "fmt"

// without memo
// time: O(2^n)
// space: O(n)

// with memo
// time: O(n)
// space: O(n)
func fibo(num int, memo map[int]int) int {
	if m, ok := memo[num]; ok {
		return m
	}

	if num < 2 {
		return num
	}

	memo[num] = fibo(num-1, memo) + fibo(num-2, memo)
	return memo[num]
}

func main() {
	memo := make(map[int]int)
	fmt.Println(fibo(50, memo))
}
