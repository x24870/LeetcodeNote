# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# peek
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.first = None
        self.second = None
        def inorder(node):
            if node:
                inorder(node.left)
                if self.prev and node.val < self.prev.val:
                    if not self.first: self.first = self.prev
                    self.second = node
                self.prev = node
                inorder(node.right)

        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val