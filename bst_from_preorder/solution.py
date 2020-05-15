# Definition for a binary tree node.
from typing import List
import sys

sys.setrecursionlimit(1000)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lower_bound(self, arr, key):
        lo, hi = 0, len(arr)-1

        while lo < hi:
            mid = lo + (hi-lo)//2

            if arr[mid] >= key:
                hi = mid
            else:
                lo = mid+1

        if arr[lo] < key:
            return len(arr)

        return lo

    def bst_from_preorder_rec(self, preorder: List[int]):
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        split = self.lower_bound(preorder[1:], root.val)+1
        root.left = self.bst_from_preorder_rec(preorder[1:split])
        root.right = self.bst_from_preorder_rec(preorder[split:])

        return root

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.bst_from_preorder_rec(preorder)

# if __name__ == '__main__':
#     arr = list(map(int,
#             input().strip()[1:-1].split(',')
#         ))
#     Solution().bstFromPreorder(arr)