# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# peek solution

# Time complex O(nlogn)
class Solution:
    def isBalanced(self, root):
        if not root: return True
        if abs(self.height(root.left) - self.height(root.right)) > 1 \
            or not self.isBalanced(root.left) \
            or not self.isBalanced(root.right):
            return False
        return True

    def height(self, node):
        if not node: return 0
        left_depth = self.height(node.left)
        right_depth = self.height(node.right)
        return max(left_depth, right_depth) + 1

# Time complex O(n)
class Solution:
    def isBalanced(self, root):
        self.balanced = True

        def height(node):
            if not node or not self.balanced: return 0
            left_h = height(node.left)
            right_h = height(node.right)
            if abs(left_h - right_h) > 1:
                self.balanced = False
                # return 0  #I think the solution if more clear without this 'return'
            return max(left_h, right_h) + 1

        height(root)

        return self.balanced