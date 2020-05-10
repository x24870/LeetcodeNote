# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(8)

class Solution:
    def deepestLeavesSum(self, root):
        deepestLeaves = {'depth': 0, 'leaves': []}

        def dfs(node, depth, deepestLeaves):
            if not node: return
            if depth > deepestLeaves['depth']:
                deepestLeaves['depth'] = depth
                deepestLeaves['leaves'] = [node.val]
            elif depth == deepestLeaves['depth']:
                deepestLeaves['leaves'].append(node.val)
            dfs(node.left, depth+1, deepestLeaves)
            dfs(node.right, depth+1, deepestLeaves)

        dfs(root, 0, deepestLeaves)

        return sum(val for val in deepestLeaves['leaves'])

s = Solution()
print(s.deepestLeavesSum(root))