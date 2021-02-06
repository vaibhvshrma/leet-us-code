# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_pointer = head
        if not odd_pointer:
            return head

        even_pointer = even_head = head.next
        fast_pointer = even_pointer.next if even_pointer else None

        while fast_pointer:
            odd_pointer.next = fast_pointer
            even_pointer.next = fast_pointer.next

            odd_pointer = odd_pointer.next
            even_pointer = even_pointer.next

            fast_pointer = fast_pointer.next.next if fast_pointer.next else None

        odd_pointer.next = even_head

        return head