package main

func removeDuplicates(nums []int) int {
	i, j := 0, 0
	for j < len(nums) {
		if i == 0 || nums[i-1] != nums[j] {
			nums[j], nums[i] = nums[i], nums[j]
			i++
			j++
		} else {
			j++
		}
	}

	return i
}
