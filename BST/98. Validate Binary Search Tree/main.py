# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# first try
# inorder traversal all nodes, then check if the list is ascending
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            stack.append(node.val)
            dfs(node.right)

        dfs(root)
        for i in range(len(stack)-1):
            if stack[i] >= stack[i+1]:
                return False
        return True

# Define upper bound and lower bound
from math import inf
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower_bound, upper_bound):
            if not node: return True
            if not (lower_bound < node.val < upper_bound): return False
            return helper(node.left, lower_bound, node.val) and helper(node.right, node.val, upper_bound)

        return helper(root, -inf, inf)