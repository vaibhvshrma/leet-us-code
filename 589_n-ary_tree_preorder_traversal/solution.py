"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        res = []
        stack = [root]

        while stack:
            top = stack.pop()
            res.append(top.val)
            for child in reversed(top.children):
                stack.append(child)
        return res
