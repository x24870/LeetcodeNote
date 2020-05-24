import sys, os
SCRIPT_DIR = os.path.join(__file__, '..', '..')
print(SCRIPT_DIR)
sys.path.append(os.path.normpath(SCRIPT_DIR))
from TreeHelper import TreeHelper
from TreeHelper import TreeGenerator

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# peek
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root: return 0
        def dfs(node, remain):
            if not node: return 0
            cur_val = remain - node.val
            return (1 if cur_val==0 else 0) + dfs(node.left, cur_val) + dfs(node.right, cur_val)

        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

