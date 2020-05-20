# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        traversal_lst = []

        def dfs(node, depth, lst):
            if not node: return
            if len(lst) <= depth:
                lst.append([])
            lst[depth].append(node.val)
            dfs(node.left, depth+1, lst)
            dfs(node.right, depth+1, lst)

        dfs(root, 0, traversal_lst)
        return reversed(traversal_lst)