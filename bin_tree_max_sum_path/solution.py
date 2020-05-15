# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        right = self.right.val if self.right else ''
        left = self.left.val if self.left else ''

        return (f'{self.val}'
                f'\n/     \\'
                f'\n{left}     {right}'
                )

    def __repr__(self):
        return self.__str__()


class Solution:
    def max_path_sum_rec(self, root: TreeNode, sum_so_far: int) -> int:
        if root is None:
            return 0

        new_sum = sum_so_far + root.val
        def add(x, y): return x + y
        if new_sum < 0:
            # chain is not continued
            self.ans = max(self.ans, root.val)
            lms = self.max_path_sum_rec(root.left, 0)
            rms = self.max_path_sum_rec(root.right, 0)

            pvt = root.val + lms + rms
            self.ans = max(self.ans, pvt)
            return root.val + max(lms, rms)

        left_max_sum = self.max_path_sum_rec(root.left, new_sum)
        right_max_sum = self.max_path_sum_rec(root.right, new_sum)

        left_max_sum = max(left_max_sum, 0)
        right_max_sum = max(right_max_sum, 0)

        # see if this point is pivot
        pivot_sum = root.val + left_max_sum + right_max_sum
        self.ans = max(self.ans, pivot_sum)

        return root.val + max(left_max_sum, right_max_sum)

    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = root.val
        sys.setrecursionlimit(10000)
        self.max_path_sum_rec(root, 0)
        return self.ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(-2)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(1)
    root.left.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(-3)
    root.right.left = TreeNode(-2)

    import ipdb
    ipdb.set_trace()

    print(Solution().maxPathSum(root))
