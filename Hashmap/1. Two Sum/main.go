package main

// time complexity: O(n)
// space compleixty: O(n)
func twoSum(nums []int, target int) []int {
	// create a map, key is the value of element, values is the index of the element
	m := make(map[int]int)

	for i, v := range nums {
		// if the key [target - v] can get a value from the map
		// which means the sum of these two values equals to the target
		// so return the index of these two values
		idx, ok := m[target-v]
		if ok {
			return []int{i, idx}
		} else {
			m[v] = i
		}
	}

	return []int{}
}
