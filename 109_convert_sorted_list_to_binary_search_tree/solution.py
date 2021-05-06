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
    def get_middle_node(head):
        if not head:
            return

        slow, fast = head, head.next
        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next.next if fast.next else None
        return prev, slow

    @staticmethod
    def get_bst(head: ListNode) -> TreeNode:
        if not head:
            return
        prev_mid_node, mid_node = Solution.get_middle_node(head)

        if not prev_mid_node:
            left = None
        else:
            left = head
            prev_mid_node.next = None

        return TreeNode(
            val=mid_node.val,
            left=Solution.get_bst(left),
            right=Solution.get_bst(mid_node.next),
        )

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        return self.get_bst(head)
