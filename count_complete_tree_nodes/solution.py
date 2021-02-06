# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec_sol(self, lo, hi):
        

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        depth = -1
        ptr = root
        while ptr:
            ptr = ptr.left
            depth += 1

        if depth == 0:
            return 1

        lo = 1 << depth
        hi = 1 << (depth+1) - 1
