# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        k_node = None
        ptr_k = head
        
        for i in range(k-1):
            ptr_k = ptr_k.next
        
        k_node = ptr_k
        back_k_node = head
        
        while ptr_k.next:
            ptr_k = ptr_k.next
            back_k_node = back_k_node.next
            
        k_node.val, back_k_node.val = back_k_node.val, k_node.val
        
        return head
