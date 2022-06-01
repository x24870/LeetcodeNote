package main

func min(i, j int) int {
	if i < j {
		return i
	}
	return j
}

func max(i, j int) int {
	if i > j {
		return i
	}
	return j
}

// time complexity: O(n)
// space complexity: O(n)
func trap(height []int) int {
	leftMax := make([]int, len(height))
	leftMax[0] = height[0]
	rightMax := make([]int, len(height))
	rightMax[len(height)-1] = height[len(height)-1]

	// find heighest from left
	for i := 1; i < len(height); i++ {
		leftMax[i] = max(height[i], leftMax[i-1])
	}

	// find heighest from right
	for i := len(height) - 2; i >= 0; i-- {
		rightMax[i] = max(height[i], rightMax[i+1])
	}

	// accumulate all trap in each column
	total := 0
	for i := 0; i < len(height); i++ {
		total += min(leftMax[i], rightMax[i]) - height[i]
	}
	return total
}
