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
        self.lvl[level].append(root.val)
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)

    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.lvl = collections.defaultdict(list)
        self.dfs(root, 0)
        return sum(self.lvl[max(self.lvl.keys())])
