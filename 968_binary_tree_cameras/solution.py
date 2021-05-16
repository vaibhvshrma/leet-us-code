# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, parent=None):
        if not root:
            return
        self.dfs(root.left, root)
        self.dfs(root.right, root)

        if (
            (parent is None and root not in self.covered)
             or root.left not in self.covered
             or root.right not in self.covered
        ):
            self.ans += 1
            self.covered.update({root, root.left, root.right, parent})


    def minCameraCover(self, root: TreeNode) -> int:
        self.ans = 0
        self.covered = {None}
        self.dfs(root)
        return self.ans
