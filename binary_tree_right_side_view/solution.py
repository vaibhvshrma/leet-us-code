class Solution:
    """
    Explore all nodes in-order. Since we explore left before right,
    for every level, the right most element will be visited last.
    Save one value per level in a level:val map.
    """

    def inorder(self, root, level):
        if not root:
            return
        self.res_map[level] = root.val
        self.inorder(root.left, level + 1)
        self.inorder(root.right, level + 1)

    def rightSideView(self, root: TreeNode) -> List[int]:
        self.res_map = {}
        self.inorder(root, 0)
        return [self.res_map[key] for key in sorted(self.res_map.keys())]
