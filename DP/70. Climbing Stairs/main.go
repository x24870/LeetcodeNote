package main

// time complexity: O(n)
// space complexity: O(n)
func climbStairs(n int) int {
	memo := make(map[int]int)
	return dfs(memo, n)
}

func dfs(memo map[int]int, n int) int {
	if v, ok := memo[n]; ok {
		return v
	}

	if n < 0 {
		return 0
	} else if n <= 2 {
		return n
	}

	memo[n] = dfs(memo, n-1) + dfs(memo, n-2)
	return memo[n]
}
