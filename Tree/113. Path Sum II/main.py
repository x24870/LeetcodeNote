from copy import deepcopy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# First try
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        traversal_lst = []

        def dfs(node, lst, cur_val):
            if not node: return
            cur_val += node.val
            lst.append(node.val)
            if not node.left and not node.right and cur_val == sum:
                traversal_lst.append(lst)
                return
            r_lst = deepcopy(lst)
            dfs(node.left, lst, cur_val)
            dfs(node.right, r_lst, cur_val)

        dfs(root, [], 0)
        return traversal_lst

# Better solution, deepcopy cost so many time and memory
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []

        def dfs(node, cur_val, stack):
            if not node: return
            cur_val += node.val

            if not node.left and not node.right and cur_val == sum:
                stack.append(node.val)
                ans.append(stack[:])
                return

            stack.append(node.val)
            if node.left:
                dfs(node.left, cur_val, stack)
                stack.pop()
            if node.right:
                dfs(node.right, cur_val, stack)
                stack.pop()
            
        dfs(root, 0, [])
        return ans