package main

// time complexity: O(n)
// space complexity: O(1)
func maxArea(height []int) int {
	left, right := 0, len(height)-1
	max := 0

	for left < right {
		unit := 0
		if height[left] < height[right] {
			unit = height[left]
		} else {
			unit = height[right]
		}

		capacity := unit * (right - left)
		if max < capacity {
			max = capacity
		}

		if height[left] < height[right] {
			left++
		} else {
			right--
		}
	}

	return max
}
