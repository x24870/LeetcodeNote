# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# first try
# Inorder traversal all nodes, then find the minimum difference
from math import inf
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        stack = []
        def dfs(node):
            if not node: return
            if node.left:
                dfs(node.left)
            stack.append(node.val)
            if node.right:
                dfs(node.right)

        dfs(root)
        min = inf
        for i in range(len(stack) - 1):
            diff = abs(stack[i] - stack[i+1])
            if min > diff: min = diff
        return min

# Better solution: space complexity is constant
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.min_diff = inf
        self.prev_val = -inf
        def inorder(node):
            if not node: return
            inorder(node.left)

            self.min_diff = min(self.min_diff, (node.val - self.prev_val) )

            self.prev_val = node.val
            inorder(node.right)
            
        inorder(root)
        return self.min_diff