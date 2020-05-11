# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# First Try
# class Solution:
#     def maxDepth(self, root):
#         def dfs(node, depth):
#             if not node: return depth
#             depth += 1
#             depth_l = dfs(node.left, depth)
#             depth_r = dfs(node.right, depth)
#             return max(depth_l, depth_r)

#         return dfs(root, 0)

# This solution is more clear
class Solution:
    def maxDepth(self, root):
        if not root: return 0
        depth_l = self.maxDepth(root.left)
        depth_r = self.maxDepth(root.right)
        return max(depth_l, depth_r) + 1