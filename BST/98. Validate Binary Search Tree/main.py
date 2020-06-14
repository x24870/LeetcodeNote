# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# first try
# inorder traversal all nodes, then check if the list is ascending
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        def dfs(node):
            if not node: return node
            if node.left:
                dfs(node.left)
            stack.append(node.val)
            if node.right:
                dfs(node.right)

        dfs(root)
        print(stack)
        for i in range(len(stack)-1):
            if stack[i] >= stack[i+1]:
                return False
        return True

