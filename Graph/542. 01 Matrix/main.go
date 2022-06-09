package main

// bfs: expand from those cell which values are 0
func updateMatrix(mat [][]int) [][]int {
	// top, bottom, left, right
	dirs := [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}

	// create a matrix, initailze all value to -1
	// -1 represent this cell is not been traversed
	ret := make([][]int, len(mat))
	for i := range ret {
		ret[i] = make([]int, len(mat[0]))
		for j := range ret[i] {
			ret[i][j] = -1
		}
	}

	q := [][]int{}
	// push all cell with value 0 to queue
	for i := range mat {
		for j := range mat[0] {
			if mat[i][j] == 0 {
				q = append(q, []int{i, j})
				ret[i][j] = 0
			}
		}
	}

	// distance to 0
	dist := 1
	// bfs travers the matrix
	for len(q) != 0 {
		size := len(q)
		// deal with current distance level cells
		for i := 0; i < size; i++ {
			// pop
			cell := q[0]
			q = q[1:]
			// traverse four directions
			for _, dir := range dirs {
				x := cell[1] + dir[1]
				y := cell[0] + dir[0]
				// check the cell is valid and not been traversed
				if x >= 0 && x < len(mat[0]) && y >= 0 && y < len(mat) && ret[y][x] == -1 {
					ret[y][x] = dist
					q = append(q, []int{y, x})
				}
			}
		}
		// move to next distance level
		dist++
	}

	return ret
}
