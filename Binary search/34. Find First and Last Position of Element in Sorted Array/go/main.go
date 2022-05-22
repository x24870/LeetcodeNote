package main

// func searchRange(nums []int, target int) []int {
// 	if len(nums) == 0 || nums[0] > target || nums[len(nums)-1] < target {
// 		return []int{-1, -1}
// 	}

// 	for i, v := range nums {
// 		if v == target {
// 			start := i
// 			end := i
// 			for end+1 < len(nums) && nums[end+1] == target {
// 				end++
// 			}
// 			return []int{start, end}
// 		}
// 	}

// 	return []int{-1, -1}
// }

// binary search
func searchRange(nums []int, target int) []int {
	if len(nums) == 0 || nums[0] > target || nums[len(nums)-1] < target {
		return []int{-1, -1}
	}

	start, end := -1, -1
	// find start
	if nums[0] == target {
		start = 0
	} else {
		left, right := 0, len(nums)-1
		for left <= right {
			mid := (left + right) / 2
			if nums[mid] == target && nums[mid-1] < target {
				start = mid
				break
			} else if nums[mid] < target {
				left = mid + 1
			} else {
				right = mid - 1
			}
		}
	}

	// find end
	if nums[len(nums)-1] == target {
		end = len(nums) - 1
	} else {
		left, right := 0, len(nums)-1
		for left <= right {
			mid := (left + right) / 2
			if nums[mid] == target && nums[mid+1] > target {
				end = mid
				break
			} else if nums[mid] > target {
				right = mid - 1
			} else {
				left = mid + 1
			}
		}
	}

	return []int{start, end}
}
