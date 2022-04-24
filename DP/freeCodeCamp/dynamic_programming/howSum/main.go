package main

import "fmt"

// m = target, n = len(arr)
// time complexity: O(n^m * m)
// space complexity: O:(m) // because we just return the first found array, so it would be just m
func howSum(target int, arr []int) []int {
	if target == 0 {
		return []int{}
	}
	if target < 0 {
		return nil
	}

	for _, num := range arr {
		reminder := target - num
		res := howSum(reminder, arr)
		if res != nil {
			res = append(res, num)
			return res
		}
	}

	return nil
}

// time complexity: O(n*m * m)
// space complexity: O:(m*m)
func howSumMemo(target int, arr []int, memo map[int][]int) []int {
	if memo[target] != nil {
		return memo[target]
	}
	if target == 0 {
		return []int{}
	}
	if target < 0 {
		return nil
	}

	for _, num := range arr {
		reminder := target - num
		res := howSumMemo(reminder, arr, memo)
		if res != nil {
			memo[target] = append(res, num) // here takes m time space
			return memo[target]
		}
	}

	memo[target] = nil
	return memo[target]
}

func main() {
	fmt.Println(howSum(7, []int{5, 3, 4, 7})) // [3, 4]
	fmt.Println(howSum(8, []int{2, 3, 5}))    // [2, 2, 2, 2]
	fmt.Println(howSum(7, []int{2, 4}))       // []

	fmt.Println(howSum(7, []int{5, 3, 4, 7}))     // [3, 4]
	fmt.Println(howSum(8, []int{2, 3, 5}))        // [2, 2, 2, 2]
	fmt.Println(howSum(7, []int{2, 4}))           // []
	fmt.Println(howSum(100, []int{10, 2, 4, 25})) // [10, 10...]
}
