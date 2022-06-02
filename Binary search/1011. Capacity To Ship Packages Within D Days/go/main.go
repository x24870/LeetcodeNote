package main

// time complexity: O(logN)
// space complexity: O(1)
func shipWithinDays(weights []int, days int) int {
	l, r := Max(weights), Sum(weights)
	minW := r

	for l < r {
		mid := l + (r-l)/2
		spent := spentDay(weights, mid, days)
		if spent == -1 {
			l = mid + 1
		} else {
			if minW > mid {
				minW = mid
			}
			r = mid
		}
	}

	return minW
}

func spentDay(weights []int, limitW int, limitDay int) int {
	day := 1
	load := 0
	for _, v := range weights {
		if load+v > limitW {
			day++
			load = v
			if day > limitDay {
				return -1
			}
		} else {
			load += v
		}
	}

	return day
}

func Max(s []int) int {
	m := -1
	for _, v := range s {
		if v > m {
			m = v
		}
	}
	return m
}

func Sum(s []int) int {
	total := 0
	for _, v := range s {
		total += v
	}
	return total
}
