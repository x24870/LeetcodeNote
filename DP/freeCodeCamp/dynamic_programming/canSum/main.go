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

// m = target, n = len(arr)
// time complexity: O(m*n)
// space complexity: O(m)
func canSumTable(target int, arr []int) bool {
	table := make([]bool, target+1)
	// init table, if target == 0 which means we don't have to take any number to match the target number.
	table[0] = true

	for i := 0; i <= target; i++ {
		if table[i] == true {
			for j := 0; j < len(arr); j++ {
				sum := i + arr[j]
				if sum <= target {
					table[sum] = true
				}
			}
		}
	}

	return table[target]
}

func main() {
	fmt.Println(canSum(7, []int{5, 3, 4, 7})) // true
	fmt.Println(canSum(7, []int{2, 4}))       // false
	// fmt.Println(canSum(300, []int{7, 14}))    // too slow
	fmt.Println("---")

	memo := make(map[int]bool)
	fmt.Println(canSumMemo(7, []int{5, 3, 4, 7}, memo)) // true
	memo = make(map[int]bool)
	fmt.Println(canSumMemo(7, []int{2, 4}, memo)) // false
	memo = make(map[int]bool)
	fmt.Println(canSumMemo(300, []int{7, 14}, memo)) // false
	memo = make(map[int]bool)
	fmt.Println(canSumMemo(700000, []int{7, 14}, memo)) // true
	fmt.Println("---")

	fmt.Println(canSumTable(7, []int{5, 3, 4, 7})) // true
	fmt.Println(canSumTable(7, []int{2, 4}))       // false
	fmt.Println(canSumTable(300, []int{7, 14}))    // false
	fmt.Println(canSumTable(700000, []int{7, 14})) // true
}
