# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# first try
# Brute force
# Time complexity: O(n)
# Space complexity: O(h), because recursion
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.second_min = float('inf')
        def preorder(node):
            if node.left:
                if node.left.val != node.val and self.second_min > node.left.val:
                    self.second_min = node.left.val 
                preorder(node.left)
            if node.right:
                if node.right.val != node.val and self.second_min > node.right.val:
                    self.second_min = node.right.val
                preorder(node.right)
                    
        preorder(root)
        return -1 if self.second_min == float('inf') else self.second_min

# This solution is more clear and faster
# Time complexity: O(n)
# Space complexity: O(h), because recursion
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.ans = float('inf')

        def dfs(node):
            if node:
                if root.val < node.val < self.ans:
                    self.ans = node.val
                else:
                    dfs(node.left)
                    dfs(node.right)
                    
        dfs(root)
        return -1 if self.ans == float('inf') else self.ans