# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    This solution is the one I originally made and does not
    use a global variable but is not worth the pain
    """

    def helper(self, root, additional=0):
        if not root:
            return 0

        right_tree_sum = self.helper(root.right, additional)
        left_tree_sum = self.helper(root.left, root.val + right_tree_sum + additional)
        val = root.val
        root.val += right_tree_sum + additional
        return val + left_tree_sum + right_tree_sum

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.helper(root)
        return root


class IdealSolution:
    """
    This is the LeetCode squeaky clean solution
    A reverse in-order traversal. Genius.
    """

    def __init__(self) -> None:
        self.total = 0

    def convertBST(self, root):
        if not root:
            return
        self.convertBST(root.right)
        self.total += root.val
        root.val = self.total
        self.convertBST(root.left)
        return root
