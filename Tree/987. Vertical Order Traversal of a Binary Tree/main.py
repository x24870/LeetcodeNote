import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''
    def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':
    '''
    def verticalTraversal(self, root):
        # A dict contains dicts, first key for x, second key for y
        # 'defaultdict' is convenient for creating a default key and value if the key does not exist
        locationDict = collections.defaultdict(
            lambda: collections.defaultdict(list)
        )
        
        # y+1 is convenient for latter sort the dict
        def dfs(node, x=0, y=0):
            if not node: return
            locationDict[x][y].append(node.val)
            dfs(node.left, x-1, y+1)
            dfs(node.right, x+1, y+1)

        dfs(root)

        ans = []
        # iterate the dict from left to right
        #                  from top to bottom
        for x in sorted(locationDict):
            # This list contains the node values at same x cordinate(vertical)
            vertical_group = []
            for y in sorted(locationDict[x]):
                # In the same location, the smaller value is reported first
                # So we have to sort the list
                vertical_group.extend(sorted(locationDict[x][y]))
            ans.append(vertical_group)
        
        return ans