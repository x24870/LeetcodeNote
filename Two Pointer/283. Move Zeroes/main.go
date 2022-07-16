package main

// time complexity: O(n)
// space complexity: O(1)
func moveZeroes(nums []int) {
	idx0, idx1 := 0, 0

	for idx1 < len(nums) && idx0 < len(nums) {
		if nums[idx1] == 0 {
			idx1++
			continue
		}

		if nums[idx0] != 0 {
			idx0++
			continue
		}

		if idx1 > idx0 {
			nums[idx0], nums[idx1] = nums[idx1], nums[idx0]
		} else {
			idx1 = idx0 + 1
		}
	}

}
