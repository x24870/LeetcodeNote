# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# first try
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def insert_node(node):
            if node.val > val:
                if node.left:
                    insert_node(node.left)
                else:
                    node.left = TreeNode(val)
            else:
                if node.right:
                    insert_node(node.right)
                else:
                    node.right = TreeNode(val)
        
        if root:
            insert_node(root)
        else:
            root = TreeNode(val)
        return root

# This solution is more clear
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

# Iterative solution
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)
        
        node = root
        while True:
            if node.val < val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
            else:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break
        return root