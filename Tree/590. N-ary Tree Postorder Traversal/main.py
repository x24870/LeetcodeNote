"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class RecursiveSolution:
    def postorder(self, root):
        traversalList = []
        self.dfs(root, traversalList)
        return traversalList

    def dfs(self, root, lst):
        if not root: return

        if root.children:
            for c in root.children:
                self.dfs(c, lst)
        lst.append(root.val)

class IterativeSolution:
    def postorder(self, root):
        if not root: return
        rev_traversalList = []
        stack = [root]

        while stack:
            root = stack.pop()
            rev_traversalList.append(root.val)
            if root.children:
                for c in root.children:
                    stack.append(c)

        return reversed(rev_traversalList)

