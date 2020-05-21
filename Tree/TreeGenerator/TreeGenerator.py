# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeGenerator:
    def get_bin_tree(lst):
        # Input is a list
        # Return a root of a binary tree
        root = TreeNode(lst.pop(0))
        cur_level_lst = [root]
        next_level_lst = []

        while lst:
            for node in cur_level_lst:
                if node.val != None:
                    node.left = TreeNode(lst.pop(0))
                    node.right = TreeNode(lst.pop(0))
                    next_level_lst.append(node.left)
                    next_level_lst.append(node.right)
                else:
                    node = None
            cur_level_lst = next_level_lst
            next_level_lst = []
                    
        return root
                

r = TreeGenerator.get_bin_tree([0, 1, 2, None, 3, 4, None])
print(r.val)
print(r.left.val)
print(r.right.val)
print(r.left.left.val)
print(r.left.right.val)
print(r.right.left.val)
print(r.right.right.val)