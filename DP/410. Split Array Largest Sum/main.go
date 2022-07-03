package main

import "math"

type key struct {
	length int
	split  int
}

// n = len(nums)
// time complexity: O(n*m*n)
// space complexity: O(n*n)
func splitArray(nums []int, m int) int {
	presum := make([]int, len(nums))
	presum[0] = nums[0]
	for i := 1; i < len(nums); i++ {
		presum[i] = presum[i-1] + nums[i]
	}
	memo := make(map[key]int)
	return dfs(presum, len(nums), m, memo)
}

func dfs(nums []int, length, split int, memo map[key]int) int {
	if length < split {
		return -1
	}
	if split == 1 {
		return nums[length-1]
	}
	if v, ok := memo[key{length, split}]; ok {
		return v
	}

	res := make([]int, 0, length)
	for i := 0; i < length-1; i++ {
		ret := dfs(nums, i+1, split-1, memo)
		if ret == -1 {
			continue
		}
		right := nums[length-1] - nums[i]
		res = append(res, larger(right, ret))
	}

	memo[key{length, split}] = min(res)
	return memo[key{length, split}]
}

func larger(i, j int) int {
	if i > j {
		return i
	}
	return j
}

func min(nums []int) int {
	min := math.MaxInt
	for _, v := range nums {
		if min > v {
			min = v
		}
	}
	return min
}
