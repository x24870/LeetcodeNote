"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class RecursiveSolution:
    def preorder(self, root):
        traversalList = []
        self.helper(root, traversalList)
        return traversalList

    def helper(self, root, lst):
        if not root: return
        lst.append(root.val)
        for c in root.children:
            self.helper(c, lst)
        

class IterativeSolution:
    def preorder(self, root):
        if not root: return
        traversalList = []
        stack = []
        stack.append(root)

        while stack:
            curNode = stack.pop()
            traversalList.append(curNode.val)
            for c in reversed(curNode.children):
                stack.append(c)

        return traversalList