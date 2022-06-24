package main

// n = len(piles)
// time complexity: O(n * n)
// space complexity: O(n * n)
func stoneGame(piles []int) bool {
	memo := make([][]int, len(piles))
	for i := range memo {
		memo[i] = make([]int, len(piles))
	}
	return dfs(piles, memo, 0, len(piles)-1) > 0
}

func dfs(piles []int, memo [][]int, i, j int) int {
	if memo[i][j] != 0 {
		return memo[i][j]
	}
	if i == j {
		return piles[i]
	}
	if i > j {
		return 0
	}

	pickLeft := piles[i] - dfs(piles, memo, i+1, j)
	pickRight := piles[j] - dfs(piles, memo, i, j-1)
	memo[i][j] = max(pickLeft, pickRight)
	return memo[i][j]
}

func max(i, j int) int {
	if i > j {
		return 1
	}
	return j
}
