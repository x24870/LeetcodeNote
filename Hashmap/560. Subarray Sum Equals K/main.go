// time complexity: O(n)
// space complexity: O(n)
func subarraySum(nums []int, k int) int {
	// init a map
	// key: sum of 0 - current index
	// value: how many times the value ocurred
	m := make(map[int]int)

	// the sum is 0 occured at least once
	// which means take no element from the array
	m[0] = 1

	curSum := 0
	ret := 0
	for _, v := range nums {
		curSum += v

		// if [current_sum - k] in the map, which means there is a subarray match the target
		occur, ok := m[curSum-k]
		if ok {
			ret += occur
		}

		// memorize current sum occured
		m[curSum] += 1
	}

	return ret
}