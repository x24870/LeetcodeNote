class IterativeSolution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return
        
        level = 0
        levelSize = 0
        queue = []
        levelGroup = []
        queue.append(root)
        
        while queue:
            if len(levelGroup) <= level:
                levelGroup.append([])
            levelSize = len(queue)
            
            while levelSize:
                root = queue.pop(0)
                levelGroup[level].append(root.val)
                for child in root.children:
                    queue.append(child)
                levelSize -= 1
            level +=1
            
        return levelGroup


class RecursiveSolution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        levelList = []
        self.helper(root, 0, levelList)
        return levelList
    
    def helper(self, root, level, levelList):
        if not root: return
        if len(levelList) <= level: levelList.append([])
        levelList[level].append(root.val)
        for child in root.children:
            self.helper(child, level+1, levelList)