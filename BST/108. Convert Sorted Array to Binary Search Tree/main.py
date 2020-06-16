# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# peek
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def build(l, r):
            if l > r: return None
            mid = (r - l)//2 + l
            root = TreeNode(nums[mid])
            root.left = build(l, mid-1)
            root.right = build(mid+1, r)
            return root

        return build(0, len(nums)-1)