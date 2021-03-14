# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, root, lo, hi):
        if not root:
            return True
        if root.val <= lo or root.val >= hi:
            return False
        
        return self.helper(root.right, root.val, hi) and self.helper(root.left, lo, root.val) 
        
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, -math.inf, math.inf)
