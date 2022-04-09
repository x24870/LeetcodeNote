package main

import "fmt"

func canSum(target int, arr []int) bool {
	if target == 0 {
		return true
	}
	if target < 0 {
		return false
	}

	for i := 0; i < len(arr); i++ {
		if canSum(target-arr[i], arr) == true {
			return true
		}
	}

	return false
}

func canSumMemo(target int, arr []int, memo map[int]bool) bool {
	if cache, ok := memo[target]; ok == true {
		return cache
	}

	if target == 0 {
		return true
	}
	if target < 0 {
		return false
	}

	for i := 0; i < len(arr); i++ {
		reminder := target - arr[i]
		if canSumMemo(reminder, arr, memo) == true {
			memo[reminder] = true
			return true
		}
	}

	memo[target] = false
	return false
}

func main() {
	fmt.Println(canSum(7, []int{5, 3, 4, 7})) // true
	fmt.Println(canSum(7, []int{2, 4}))       // false
	// fmt.Println(canSum(300, []int{7, 14}))    // too slow

	memo := make(map[int]bool)
	fmt.Println(canSumMemo(7, []int{5, 3, 4, 7}, memo)) // true
	fmt.Println(canSumMemo(7, []int{2, 4}, memo))       // false
	fmt.Println(canSumMemo(300, []int{7, 14}, memo))    // false
	fmt.Println(canSumMemo(700000, []int{7, 14}, memo)) // true
}
