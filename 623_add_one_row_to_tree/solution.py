# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, depth):
        if not root:
            return
        if depth == self.depth-1:
            root.left = TreeNode(self.val, left=root.left)
            root.right = TreeNode(self.val, right=root.right)
            return
        self.helper(root.left, depth+1)
        self.helper(root.right, depth+1)
        
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            return TreeNode(v, left=root)
        
        self.val = v
        self.depth = d
        self.helper(root, 1)
        return root
