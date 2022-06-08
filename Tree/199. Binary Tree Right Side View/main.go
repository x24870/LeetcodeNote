package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// n = number of nodes
// time complexity: O(n)
// space complexity: O(n)
func rightSideView(root *TreeNode) []int {
	if root == nil {
		return nil
	}

	q := []*TreeNode{}
	ret := []int{}

	q = append(q, root)

	for len(q) != 0 {
		size := len(q)
		for i := 0; i < size; i++ {
			// push child to the queue
			node := q[0]
			if node.Left != nil {
				q = append(q, node.Left)
			}
			if node.Right != nil {
				q = append(q, node.Right)
			}

			// pop
			q = q[1:]

			// get right most node of current level
			if i == size-1 {
				ret = append(ret, node.Val)
			}
		}
	}

	return ret
}
