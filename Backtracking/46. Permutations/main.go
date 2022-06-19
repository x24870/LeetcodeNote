package main

// n = len(nums)
// time complexity: O(n*n)
// space compleixty: O(n)
func permute(nums []int) [][]int {
	rets := [][]int{}
	visited := make([]bool, len(nums))
	dfs(&rets, &visited, []int{}, nums)
	return rets
}

func dfs(rets *[][]int, visited *[]bool, cur, nums []int) {
	if len(cur) == len(nums) {
		(*rets) = append((*rets), cur)
		return
	}

	for i := 0; i < len(nums); i++ {
		if (*visited)[i] {
			continue
		}
		(*visited)[i] = true
		dfs(rets, visited, append(cur, nums[i]), nums)
		(*visited)[i] = false
	}
}
