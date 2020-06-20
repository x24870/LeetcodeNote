# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# First try, my idea:
# 1. inorder traversal (or any type of traversal)
# 2. store mode in hashmap (we can return the result in any order)
# 3. return mode in the hashmap
from collections import defaultdict
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def init_val():
            return 0

        def inorder(node):
            if not node: return
            inorder(node.left)
            self.modes[node.val] += 1
            inorder(node.right)

        if not root: return []
        
        self.modes = defaultdict(init_val)
        inorder(root)
        max_mode_num = max(self.modes.values())
        ans = []
        for key in self.modes:
            if self.modes[key] == max_mode_num:
                ans.append(key)

        return ans
