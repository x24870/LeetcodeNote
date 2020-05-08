"""
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
"""
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)


""" 
Solution format
:type root: TreeNode
:rtype: List[int]
"""
class recursiveSolution(object):
    def preorderTraversal(self, root):
        traversalList = []
        self.helper(root, traversalList)
        return traversalList

    def helper(self, root, lst):
        if not root: return
        lst.append(root.val)
        self.helper(root.left, lst)
        self.helper(root.right, lst)

r = recursiveSolution()
print(r.preorderTraversal(root))

class iterativeSolution(object):
    def preorderTraversal(self, root):
        if not root: return
        stack = []
        traversalList = []
        stack.append(root)

        while stack:
            curNode = stack.pop()
            traversalList.append(curNode.val)
            if curNode.right: stack.append(curNode.right)
            if curNode.left: stack.append(curNode.left)

        return traversalList

i = iterativeSolution()
print(i.preorderTraversal(root))