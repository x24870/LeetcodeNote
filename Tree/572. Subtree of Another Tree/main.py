# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# First try
class Solution:
    def isSubtree(self, s, t):
        self.s = s
        self.t = t
        self.found_match = False

        self.dfs(s)

        return self.found_match

    def match_tree(self, s_node, t_node):
        if not s_node and not t_node: return True
        if s_node and not t_node: return False
        if t_node and not s_node: return False
        if s_node.val != t_node.val: return False

        return self.match_tree(s_node.left, t_node.left) and self.match_tree(s_node.right, t_node.right)
        

    def dfs(self, node):
        if self.found_match: return
        if not node: return
        if node.val == self.t.val:
            self.found_match =  self.match_tree(node, self.t)
        self.dfs(node.left)
        self.dfs(node.right)

## Preorder Traversal String
# Output a string of preorder traversal result
# Then check if the subtree string in the main tree string
class Solution:
    def isSubtree(self, s, t):
        def dfs(node, is_left):
            if not node:
                if is_left:
                    return 'LN'
                else:
                    return 'RN'
            
            return '#' + str(node.val) + dfs(node.left, True) + dfs(node.right, False)

        s_pre_traversal_string = dfs(s, True)
        t_pre_traversal_string = dfs(t, True)

        if t_pre_traversal_string in s_pre_traversal_string: return True
        return False
