package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// n = number of nodes
// time complexity: O(n)
// space complexity: O(n)
func maxPathSum(root *TreeNode) int {
	maxSum := root.Val
	pathSum(root, &maxSum)
	return maxSum
}

// dfs traverse the tree
func pathSum(root *TreeNode, maxSum *int) int {
	if root == nil {
		return 0
	}

	lSum := pathSum(root.Left, maxSum)
	rSum := pathSum(root.Right, maxSum)
	// find max sum base on each case
	curMax := max(lSum+root.Val, rSum+root.Val, lSum+rSum+root.Val, root.Val)
	if curMax > *maxSum {
		*maxSum = curMax
	}

	// return max of current node
	return max(lSum+root.Val, rSum+root.Val, root.Val)
}

func max(nums ...int) int {
	max := nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i] > max {
			max = nums[i]
		}
	}
	return max
}
