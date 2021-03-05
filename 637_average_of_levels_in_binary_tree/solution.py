# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, level):
        if not root:
            return
        self.levels[level].append(root.val)
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)
        
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        self.levels = defaultdict(list)
        self.dfs(root, 0)
        return [sum(self.levels[i])/len(self.levels[i]) for i in sorted(self.levels.keys())]
