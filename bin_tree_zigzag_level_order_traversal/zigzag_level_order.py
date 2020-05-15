# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        st1 = deque()
        st2 = deque()
        res = []

        # depth of tree starting at 0
        odd = False

        st1.append(root)
        res.append([root.val])

        while st1 or st2:
            subres = []
            if odd:
                # insert left first
                while st1:
                    x = st1.pop()
                    if x.left:
                        st2.append(x.left)
                        subres.append(x.left.val)
                    if x.right:
                        st2.append(x.right)
                        subres.append(x.right.val)
                odd = True
            else:
                while st2:
                    # insert right first
                    x = st2.pop()
                    if x.right:
                        st1.append(x.right)
                        subres.append(x.right.val)
                    if x.left:
                        st1.append(x.left)
                        subres.append(x.left.val)
                odd = False
            
            if subres:
                res.append(subres)

        return res