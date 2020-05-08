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
    def postorderTraversal(self, root):
        traversalList = []
        self.helper(root, traversalList)
        return traversalList

    def helper(self, root, lst):
        if not root: return
        self.helper(root.left, lst)
        self.helper(root.right, lst)
        lst.append(root.val)

r = RecursiveSolution()
print(r.postorderTraversal(root))

class RecursiveSolution2(object):
    # devide and conquer
    def postorderTraversal(self, root):
        if not root: return []
        leftList = self.postorderTraversal(root.left)
        rightList = self.postorderTraversal(root.right)
        leftList.extend(rightList)
        leftList.append(root.val)
        return leftList

r2 = RecursiveSolution2()
print(r2.postorderTraversal(root))

class IterativeSolution(object):
    def postorderTraversal(self, root):
        if not root: return
        traversalList = []
        stack = []
        stack.append(root)

        while stack:
            curNode = stack.pop()
            traversalList.insert(0, curNode.val)
            if curNode.left: stack.append(curNode.left)
            if curNode.right: stack.append(curNode.right)

        return traversalList


i = IterativeSolution()
print(i.postorderTraversal(root))