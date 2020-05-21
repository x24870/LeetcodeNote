# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# First try
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def subtree_has_one(node):
            if not node: return False
            if node.val: return True
            return subtree_has_one(node.left) or subtree_has_one(node.right)
        
        def dfs(node):
            if not node: return

            if not subtree_has_one(node.left):
                node.left = None
            else:
                dfs(node.left)

            if not subtree_has_one(node.right):
                node.right = None
            else:
                dfs(node.right)

        dfs(root)
        return root

# This solution is more clear
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        return root if root.val or root.left or root.right else None
        