# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# first try
# Go through all nodes, then find the K-th smallest val
# Time complexity: O(n)
# Spaces complexity: O(n)
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.traversal_list = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            self.traversal_list.append(node.val)
            inorder(node.right)
        inorder(root)
        return self.traversal_list[k-1]

# Time complexity: O(n)
# Spaces complexity: O(h)
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        def inorder(node):
            if not node: return -1
            x = inorder(node.left)
            if x != -1:
                return x
                
            if self.k == 1:
                return node.val

            self.k -= 1
            return inorder(node.right)
        
        return inorder(root)