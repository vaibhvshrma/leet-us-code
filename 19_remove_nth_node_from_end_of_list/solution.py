# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ahead = behind = head

        for i in range(n):
            ahead = ahead.next

        if ahead is None:
            return head.next

        while ahead.next is not None:
            ahead = ahead.next
            behind = behind.next

        # remove node
        behind.next = behind.next.next

        return head
