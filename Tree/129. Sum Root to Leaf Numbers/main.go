package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sumNumbers(root *TreeNode) int {
	total := 0
	dfs(root, 0, &total)
	return total
}

func dfs(root *TreeNode, parentNum int, total *int) {
	if root == nil {
		return
	}

	curNum := parentNum*10 + root.Val
	if root.Left == nil && root.Right == nil {
		*total += curNum
	}

	if root.Left != nil {
		dfs(root.Left, curNum, total)
	}

	if root.Right != nil {
		dfs(root.Right, curNum, total)
	}
}
