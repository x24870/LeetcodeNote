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

# First try
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root: return root
        self.removeLeafNodes(root.left, target)
        self.removeLeafNodes(root.right, target)
        if root.left:
            if self.delete_node(root.left, target):
                root.left = None
        if root.right:
            if self.delete_node(root.right, target):
                root.right = None
        if self.delete_node(root, target):
            return None
        return root

    def delete_node(self, node, target):
        if not node.left and not node.right and node.val == target: return True
        return False

# This solution is more clear
class Solution2:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root: return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        return None if not root.left and not root.right and root.val == target else root


input = [1,2,3,2,None,2,4]
root = TreeGenerator.get_bin_tree(input)
TreeHelper.print_tree(root)

s = Solution2()
root = s.removeLeafNodes(root, 2)
TreeHelper.print_tree(root)
