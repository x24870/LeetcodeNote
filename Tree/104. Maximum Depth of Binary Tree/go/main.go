package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// DFS solution
func maxDepth(root *TreeNode) int {
	return dfs(root)
}

func dfs(root *TreeNode) int {
	if root == nil {
		return 0
	}

	return max(dfs(root.Left), dfs(root.Right)) + 1
}

func max(i, j int) int {
	if i > j {
		return i
	}
	return j
}

// BFS solution
func maxDepthBFS(root *TreeNode) int {
	return bfs(root)
}

func bfs(root *TreeNode) int {
	if root == nil {
		return 0
	}

	q := []*TreeNode{}
	depth := 0

	q = append(q, root)

	for len(q) != 0 {
		size := len(q)
		// pop the nodes in current level
		for i := 0; i < size; i++ {
			node := q[0]
			q = q[1:]
			// push child nodes
			if node.Left != nil {
				q = append(q, node.Left)
			}
			if node.Right != nil {
				q = append(q, node.Right)
			}
		}
		depth++
	}

	return depth
}
