package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}

	return areSymmetric(root.Left, root.Right)
}

func areSymmetric(left *TreeNode, right *TreeNode) bool {
	if left == nil && right == nil {
		return true
	}

	if (left == nil && right != nil) ||
		(left != nil && right == nil) ||
		(left.Val != right.Val) {
		return false
	}

	return areSymmetric(left.Left, right.Right) && areSymmetric(left.Right, right.Left)
}
