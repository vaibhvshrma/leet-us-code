# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        queue = [root]

        while queue:
            level = []
            tmp = []
            for node in queue:
                if node:
                    level.append(node.val)
                    tmp.extend([node.left, node.right])
            if level:
                res.append(level)
            queue = tmp

        return res
