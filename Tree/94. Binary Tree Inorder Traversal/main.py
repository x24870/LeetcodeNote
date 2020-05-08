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
class RecursiveSolution(object):
    def inorderTraversal(self, root):
        traversalList = []
        self.helper(root, traversalList)
        return traversalList

    def helper(self, root, lst):
        if not root: return
        self.helper(root.left, lst)
        lst.append(root.val)
        self.helper(root.right, lst)

r = RecursiveSolution()
print(r.inorderTraversal(root))

class IterativeSolution(object):
    def inorderTraversal(self, root):
        traversalList = []
        stack = []
        if not root: return
        
        curNode = root
        while stack or curNode:
            while curNode:
                stack.append(curNode)
                curNode = curNode.left
            curNode = stack.pop()
            traversalList.append(curNode.val)
            curNode = curNode.right

        return traversalList

i = IterativeSolution()
print(i.inorderTraversal(root))