# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#peek
# idea:
# 1. search tree to find the node
# 2. there are few case to be handle
#     a. the node is leaf -> delete the node
#     b. the node has left sub tree -> delete the node then connect left sub tree to parent
#     c. the node has right sub tree -> delete the node then connect right sub tree to parent
#     d. the node has right and left sub tree
#        -> find most left node in right sub tree
#        -> switch value
#        -> delete the most left node of right sub tree

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return None
        if root.val == key:
            if root.left and root.right:
                # find most left node of right sub tree
                most_left = root.right
                while most_left.left: most_left = most_left.left
                # modify node val and delete the most left node
                root.val = most_left.val
                root.right = self.deleteNode(root.right, most_left.val)
            elif root.left or root.right:
                return root.left if root.left else root.right
            else:
                return None
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
            
        return root
        

# solution 2
# Just different with step 'd'
# delete the node the replace by the most left node of right sub tree
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return None
        if root.val == key:
            if root.left and root.right:
                # find most left node and it's parent
                most_left = most_left_parent = root.right
                while most_left.left:
                    most_left_parent = most_left
                    most_left = most_left.left

                most_left.left = node.left
                if most_left != most_left_parent:
                    most_left_parent.left = most_left.right
                    most_left.right = node.right
                return most_left
            elif root.left or root.right:
                return root.left if root.left else root.right
            else:
                return None
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
            
        return root