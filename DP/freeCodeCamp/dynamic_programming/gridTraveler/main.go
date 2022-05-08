package main

import (
	"fmt"
	"strconv"
)

// without memo
// time: O(2^(n+m))
// space: O(n+m)
func gridTravel(n int, m int) int {
	if n <= 0 || m <= 0 {
		return 0
	}

	if n == 1 || m == 1 {
		return 1
	}

	return gridTravel(n-1, m) + gridTravel(n, m-1)
}

// without memo
// time: O(n*m)
// space: O(n+m)
func gridTravelWithMemo(m int, n int, memo map[string]int) int {
	if n <= 0 || m <= 0 {
		return 0
	}

	if n == 1 || m == 1 {
		return 1
	}

	dimension := fmt.Sprintf("%v,%v", strconv.Itoa(m), strconv.Itoa(n))
	if cache, ok := memo[dimension]; ok == true {
		return cache
	}

	memo[dimension] = gridTravelWithMemo(n-1, m, memo) + gridTravelWithMemo(n, m-1, memo)

	return memo[dimension]
}

func gridTravelTable(m int, n int) int {
	// create a 2D array
	table := make([][]int, m+1)
	for i := range table {
		table[i] = make([]int, n+1)
	}

	// init starter grid
	table[1][1] = 1

	// iterate the grid map
	for i := 0; i <= m; i++ {
		for j := 0; j <= n; j++ {
			cur := table[i][j]
			if j < n {
				table[i][j+1] += cur // right grid
			}
			if i < m {
				table[i+1][j] += cur // bottom grid
			}

		}
	}

	return table[m][n]
}

func main() {
	fmt.Println(gridTravel(2, 3)) //3
	fmt.Println(gridTravel(3, 2)) //3
	fmt.Println(gridTravel(3, 3)) //6
	// fmt.Println(gridTravel(18, 18)) // 2333606220 very slow

	memo := make(map[string]int)
	fmt.Println(gridTravelWithMemo(2, 3, memo))   //3
	fmt.Println(gridTravelWithMemo(3, 2, memo))   //3
	fmt.Println(gridTravelWithMemo(3, 3, memo))   //6
	fmt.Println(gridTravelWithMemo(18, 18, memo)) // 2333606220 way faster

	fmt.Println(gridTravelTable(2, 3))   //3
	fmt.Println(gridTravelTable(3, 2))   //3
	fmt.Println(gridTravelTable(3, 3))   //6
	fmt.Println(gridTravelTable(18, 18)) // 2333606220 way faster
}
