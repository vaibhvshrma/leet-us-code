# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # need a counter which can be unique element for each heap node so that it never gets
        # to comparing ListNode object which fails. In our own implementation of ListNode class
        # we can implement __lt__ method so that exceptions do not happen
        min_heap = [(lst_head.val, i, lst_head) for i, lst_head in enumerate(lists) if lst_head]
        heapq.heapify(min_heap)
        ptr = res = ListNode()
        cntr = len(lists)
        while min_heap:
            val, _, node = min_heap[0]
            ptr.next = node
            ptr = ptr.next
            if node.next:
                heapq.heapreplace(min_heap, (node.next.val, cntr, node.next))
            else:
                heapq.heappop(min_heap)
            cntr += 1
        return res.next
