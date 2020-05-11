# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# First Try
# class Solution:
#     def isSymmetric(self, root):
#         if not root: return True

#         def dfs(left, right):
#             if not left and not right: return True
#             if not left or not right: return False
#             return all((
#                 left.val == right.val,
#                 dfs(left.left, right.right),
#                 dfs(left.right, right.left)
#             ))

#         return dfs(root.left, root.right)

# This solution is more clear
class Solution:
    def isSymmetric(self, root):
        def dfs(left, right):
            if not left and not right: return True
            if not left or not right: return False
            return all((
                left.val == right.val,
                dfs(left.left, right.right),
                dfs(left.right, right.left)
            ))

        return dfs(root, root)