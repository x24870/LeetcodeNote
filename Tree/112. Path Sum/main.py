# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# First try
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def dfs(node, cur_val):
            if not node: return False
            cur_val += node.val
            if not node.left and not node.right and cur_val == sum:
                return True
            return dfs(node.left, cur_val) or dfs(node.right, cur_val)
            
        return dfs(root, 0)