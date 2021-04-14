# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        l, r = ListNode(), ListNode()
        l_head, r_head = l, r
        ptr = head
        while ptr:
            if ptr.val < x:
                l.next = ptr
                l = ptr
            else:
                r.next = ptr
                r = ptr
            nxt = ptr.next
            ptr.next = None
            ptr = nxt

        l.next = r_head.next
        return l_head.next
