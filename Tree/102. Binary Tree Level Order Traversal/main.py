# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution format
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
# First try
class Solution:
    def levelOrder(self, root):
        level_order_lst = []

        def dfs(node, depth, lst):
            if not node: return
            if len(lst) <= depth:
                lst.append([])

            lst[depth].append(node.val)

            dfs(node.left, depth+1, lst)
            dfs(node.right, depth+1, lst)

        dfs(root, 0, level_order_lst)
        return level_order_lst

# Using queue (BFS)
class Solution:
    def levelOrder(self, root):
        if not root: return
        level_order_lst = []
        cur_q = [root]
        next_q = []
        
        while cur_q:
            level_order_lst.append([])
            for node in cur_q:
                if node.left: next_q.append(node.left)
                if node.right: next_q.append(node.right)
                level_order_lst[-1].append(node.val)
            cur_q = next_q
            next_q = []

        return level_order_lst
                