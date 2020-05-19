# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# First try
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        def dfs(node):
            if not node:
                return 0
            elif node.left and not node.right:
                return dfs(node.left) + 1
            elif node.right and not node.left:
                return dfs(node.right) + 1
            else:
                return min( dfs(node.left), dfs(node.right) ) + 1
        
        return dfs(root)

# Better solution
class Solution:
    def minDepth(self, root):
        if not root: return 0
        if not root.left and not root.right: return 1
            
        l_depth = self.minDepth(root.left)
        r_depth = self.minDepth(root.right)
        if not l_depth: return r_depth + 1
        if not r_depth: return l_depth + 1
        return min(l_depth, r_depth) + 1
