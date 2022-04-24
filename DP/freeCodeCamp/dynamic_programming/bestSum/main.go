package main

import "fmt"

// m = target, n = len(arr)
// time complexity: O(n^m*m)
// space complexity: O(m*m) // m stacks * append witch has lenghth m
func bestSum(target int, arr []int) []int {
	if target == 0 {
		return []int{}
	}
	if target < 0 {
		return nil
	}

	var shortest []int // not init, it's a nil pointer
	for _, num := range arr {
		reminder := target - num
		res := bestSum(reminder, arr)
		if res != nil {
			res = append(res, num) // append current number
			if shortest == nil || len(shortest) > len(res) {
				shortest = res
			}
		}
	}

	return shortest
}

// time complexity: O(n*m *m)
// space complexity: O(m*m) // m
func bestSumMemo(target int, arr []int, memo map[int][]int) []int {
	if val, ok := memo[target]; ok == true {
		return val
	}
	if target == 0 {
		return []int{}
	}
	if target < 0 {
		return nil
	}

	var shortest []int
	for _, num := range arr {
		reminder := target - num
		res := bestSumMemo(reminder, arr, memo)
		if res != nil {
			res = append(res, num)
			if shortest == nil || len(shortest) > len(res) {
				shortest = res
			}
		}
	}

	memo[target] = shortest
	return shortest
}

func main() {
	fmt.Println(bestSum(7, []int{5, 3, 4, 7})) // [7]
	fmt.Println(bestSum(8, []int{2, 3, 5}))    // [3, 5]
	fmt.Println(bestSum(8, []int{1, 4, 5}))    // [4, 4]
	fmt.Println(bestSum(7, []int{2, 4}))       // []
	// fmt.Println(bestSum(100, []int{1, 2, 5, 25})) // [25, 25, 25, 25] slow

	memo := make(map[int][]int)
	fmt.Println(bestSumMemo(7, []int{5, 3, 4, 7}, memo)) // [7]
	memo = make(map[int][]int)
	fmt.Println(bestSumMemo(8, []int{2, 3, 5}, memo)) // [3, 5]
	memo = make(map[int][]int)
	fmt.Println(bestSumMemo(8, []int{1, 4, 5}, memo)) // [4, 4]
	memo = make(map[int][]int)
	fmt.Println(bestSumMemo(7, []int{2, 4}, memo)) // []
	memo = make(map[int][]int)
	fmt.Println(bestSumMemo(100, []int{1, 2, 5, 25}, memo)) // [25, 25, 25, 25]
}
