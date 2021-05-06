# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    @staticmethod
    def get_size(head):
        n = 0
        while head:
            head = head.next
            n += 1
        return n

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        n = self.get_size(head)

        def get_bst(start, end):
            nonlocal head

            if start > end:
                return

            mid = (start + end) // 2
            left = get_bst(start, mid-1)

            # simulating inorder traversal which is sorted
            # hence building tree from that traversal by incrementing
            # and thus linearly traversing sorted list
            # i.e. instead of printing from tree we are rebuilding tree from
            # output
            root = TreeNode(head.val)
            head = head.next

            root.left = left
            root.right = get_bst(mid+1, end)

            return root

        return get_bst(0, n-1)
