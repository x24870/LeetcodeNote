package main

// top down: exceed limit time
func minimumTotalTopDown(triangle [][]int) int {
	min := 10000

	dfs(&min, 0, triangle[0][0], 1, triangle)

	return min
}

func dfs(min *int, idx, curVal, depth int, triangle [][]int) {
	if depth >= len(triangle) {
		if *min > curVal {
			*min = curVal
		}
		return
	}

	dfs(min, idx, curVal+triangle[depth][idx], depth+1, triangle)
	dfs(min, idx+1, curVal+triangle[depth][idx+1], depth+1, triangle)
}

// bottom up
// m = 1 + 2 + 3 + ... n
// time complexity: O(m)
// space complexity: O(1)
func minimumTotal(triangle [][]int) int {
	for i := len(triangle) - 2; i >= 0; i-- {
		for j := 0; j < len(triangle[i]); j++ {
			triangle[i][j] += Min(triangle[i+1][j], triangle[i+1][j+1])
		}
	}

	return triangle[0][0]
}

func Min(i, j int) int {
	if i < j {
		return i
	}
	return j
}
