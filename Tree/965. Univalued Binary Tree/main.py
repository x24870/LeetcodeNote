# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# First try
class Solution:
    def isUnivalTree(self, root):
        def dfs(node, parent_val):
            if not node: return True
            if node.val != parent_val: return False
            return dfs(node.left, node.val) and dfs(node.right, node.val)

        return dfs(root, root.val)

# Traversal all nodes, then check if all nodes values in traversal list are same
class Solution:
    def isUnivalTree(self, root):
        traversal_lst = []
        def dfs(node, lst):
            if not node: return
            lst.append(node.val)
            dfs(node.left, lst)
            dfs(node.right, lst)

        dfs(root, traversal_lst)

        return len(set(traversal_lst)) == 1