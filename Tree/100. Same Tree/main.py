# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# First Try
# class Solution:
#     def isSameTree(self, p: TreeNode, q: TreeNode):
#         if not p and not q: return True
#         if not p or not q: return False
#         if p.val != q.val: return False
#         if not self.isSameTree(p.left, q.left): return False
#         if not self.isSameTree(p.right, q.right): return False
#         return True

# This solution more clear
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode):
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        return all(( p.val == q.val,
                    self.isSameTree(p.left, q.left),
                    self.isSameTree(p.right, q.right)
                    ))
