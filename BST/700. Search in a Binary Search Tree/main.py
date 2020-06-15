# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# first try
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        self.ans = None
        def preorder(node):
            if not node: return
            if node.val == val:
                self.ans = node
                return
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return self.ans