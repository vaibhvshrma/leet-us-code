# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        min_heap = [(lists[list_idx].val, list_idx) for list_idx in range(len(lists)) if lists[list_idx]]
        heapq.heapify(min_heap)
        ptr = res = ListNode()
        
        while min_heap:
            top = heapq.heappop(min_heap)
            val, list_idx = top
            ptr.next = ListNode(val)
            ptr = ptr.next
            lists[list_idx] = lists[list_idx].next
            if lists[list_idx]:
                heapq.heappush(min_heap, (lists[list_idx].val, list_idx))
            
        return res.next
