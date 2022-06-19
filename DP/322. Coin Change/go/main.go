package main

import "math"

// Top Down - recursion
// m = amount, n = len(coins)
// time complexity: O(n*m)
// space complexity: O(m)
func coinChangeRecursive(coins []int, amount int) int {
	if amount == 0 {
		return 0
	}
	memo := make([]int, amount)

	dfs(&memo, coins, amount)

	return memo[amount-1]
}

func dfs(memo *[]int, coins []int, amount int) int {
	if amount == 0 {
		return 0
	}
	if amount < 0 {
		return -1
	}
	if (*memo)[amount-1] != 0 {
		return (*memo)[amount-1]
	}

	min := math.MaxInt
	for _, c := range coins {
		ret := dfs(memo, coins, amount-c)
		if ret != -1 && min > ret {
			min = ret
		}
	}

	if min == math.MaxInt {
		(*memo)[amount-1] = -1
	} else {
		(*memo)[amount-1] = min + 1
	}
	return (*memo)[amount-1]
}

// buttom up - tabulation
// m = amount, n = len(coins)
// time complexity: O(m*n)
// space complexity: O(m)
func coinChange(coins []int, amount int) int {
	if amount == 0 {
		return 0
	}
	table := make([]int, amount+1)
	for i := range table {
		table[i] = -1
	}
	table[0] = 0

	for i := 0; i < len(table); i++ {
		if table[i] == -1 {
			continue
		}
		for _, c := range coins {
			cur := i + c
			if cur < len(table) {
				if table[cur] == -1 || table[cur] > table[i]+1 {
					table[cur] = table[i] + 1
				}
			}
		}
	}

	if table[len(table)-1] == 0 {
		return -1
	}
	return table[len(table)-1]
}
