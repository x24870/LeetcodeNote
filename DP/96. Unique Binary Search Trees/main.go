package main

// time complextiy: O(n^n)
// space complexity: O(n)
func numTrees(n int) int {
	memo := make(map[int]int)
	return dfs(n, memo)
}

func dfs(n int, memo map[int]int) int {
	if n <= 1 {
		return 1
	}

	if v, ok := memo[n]; ok {
		return v
	}

	total := 0
	for i := 1; i <= n; i++ {
		// i is the root of left & right tree
		leftTree := dfs(i-1, memo)
		rightTree := dfs(n-i, memo)
		// there is left*right combinations for i as root
		total += leftTree * rightTree
	}

	memo[n] = total
	return memo[n]
}
