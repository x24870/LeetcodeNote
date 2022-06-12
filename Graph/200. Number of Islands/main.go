package main

func numIslands(grid [][]byte) int {
	count := 0

	// iterate the grids
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == '1' {
				count++
				dfs(grid, i, j)
			}
		}
	}

	return count
}

func dfs(grid [][]byte, i, j int) {
	// memorize this gird, two methods
	// 1. use a map
	// 2. turn this grid to 0, so this grid will not be traverse again
	grid[i][j] = '0'

	// traverse four directions
	dirs := [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	for _, dir := range dirs {
		x := j + dir[1]
		y := i + dir[0]
		if y >= 0 && y < len(grid) && x >= 0 && x < len(grid[0]) && grid[y][x] == '1' {
			dfs(grid, y, x)
		}
	}
}
