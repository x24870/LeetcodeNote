package main

// n = len(piles)
// time complexity: O(n * n)
// space complexity: O(n * n)
type Pair struct {
	i int
	j int
}

func stoneGame(piles []int) bool {
	memo := make(map[Pair]int)
	return dfs(piles, memo, Pair{0, len(piles) - 1}) > 0
}

func dfs(piles []int, memo map[Pair]int, pair Pair) int {
	if v, ok := memo[pair]; ok {
		return v
	}
	if pair.i == pair.j {
		return piles[pair.i]
	}
	if pair.i > pair.j {
		return 0
	}

	pickLeft := piles[pair.i] - dfs(piles, memo, Pair{pair.i + 1, pair.j})
	pickRight := piles[pair.j] - dfs(piles, memo, Pair{pair.i, pair.j - 1})
	memo[pair] = max(pickLeft, pickRight)
	return memo[pair]
}

func max(i, j int) int {
	if i > j {
		return 1
	}
	return j
}
