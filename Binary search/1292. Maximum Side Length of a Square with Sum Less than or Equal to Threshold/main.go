package main

// m = len(mat), n = len(mat[0])
// if m > n
// time complexity: O(log(n) * (m*n) * n^2)
// space complexity: O(1)
func maxSideLength(mat [][]int, threshold int) int {
	l, r := 1, min(len(mat), len(mat[0]))
	maxLen := 0

	for l < r {
		mid := l + (r-l+1)/2
		if validSquare(mat, mid, threshold) {
			l = mid
			if maxLen < mid {
				maxLen = mid
			}
		} else {
			r = mid - 1
		}
	}
	return maxLen
}

func validSquare(mat [][]int, length, threshold int) bool {
	// travel the matrix
	for i := 0; i <= len(mat)-length; i++ {
		for j := 0; j <= len(mat[0])-length; j++ {
			if sumValid(mat, i, j, length, threshold) {
				return true
			}
		}
	}

	return false
}

func sumValid(mat [][]int, row, col, length, threshold int) bool {
	total := 0
	for i := 0; i < length; i++ {
		for j := 0; j < length; j++ {
			total += mat[i+row][j+col]
			if total > threshold {
				return false
			}
		}
	}
	return true
}

func min(i, j int) int {
	if i < j {
		return i
	}
	return j
}
