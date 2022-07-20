package main

func subsets(nums []int) [][]int {
	ans := [][]int{}
	dfs(nums, []int{}, 0, &ans)
	return ans
}

func dfs(nums, cur []int, idx int, ans *[][]int) {
	if idx == len(nums) {
		s := make([]int, len(cur))
		copy(s, cur)
		(*ans) = append((*ans), s)
		return
	}

	// not take nums[idx]
	dfs(nums, cur, idx+1, ans)

	// take nums[idx]
	cur = append(cur, nums[idx])
	dfs(nums, cur, idx+1, ans)
	cur = cur[:len(cur)-1]
}
