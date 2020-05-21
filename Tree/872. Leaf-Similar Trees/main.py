# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# First Try
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def get_leave_vals(node, lst):
            if not node: return
            if not node.left and not node.right:
                lst.append(node.val)
            get_leave_vals(node.left, lst)
            get_leave_vals(node.right, lst)

        root1_leave_vals = []
        root2_leave_vals = []
        get_leave_vals(root1, root1_leave_vals)
        get_leave_vals(root2, root2_leave_vals)

        return root1_leave_vals == root2_leave_vals

# This solution more clear
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def get_leaf_vals(node):
            if not node: return []
            if not node.left and not node.right: return [node.val]
            return get_leaf_vals(node.left) + get_leaf_vals(node.right)
        return get_leaf_vals(root1) == get_leaf_vals(root2)