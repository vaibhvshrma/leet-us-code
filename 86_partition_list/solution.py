# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        l = l_head = ListNode()
        r = r_head = ListNode()
        ptr = head

        while ptr:
            if ptr.val < x:
                l.next = ptr
                l = ptr
            else:
                r.next = ptr
                r = ptr
            ptr = ptr.next
        r.next = None

        l.next = r_head.next
        return l_head.next
