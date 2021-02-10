# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """
    Uses O(n) extra space
    There exists an inter-weaving solution without using
    extra space
    """
    def copyRandomList(self, head: 'Node') -> 'Node':
        copy_ptr = copy_head = Node(0)
        orig_ptr = head
        idx = 0
        orig_node_to_idx_map = {None: None}
        copy_idx_to_node_map = {None: None}
        while orig_ptr:
            copy_ptr.next = Node(orig_ptr.val)
            orig_node_to_idx_map[orig_ptr] = idx
            copy_ptr = copy_ptr.next
            copy_idx_to_node_map[idx] = copy_ptr
            orig_ptr = orig_ptr.next
            idx += 1

        orig_ptr = head
        copy_ptr = copy_head.next

        while orig_ptr:
            idx = orig_node_to_idx_map[orig_ptr.random]
            copy_ptr.random = copy_idx_to_node_map[idx]
            orig_ptr = orig_ptr.next
            copy_ptr = copy_ptr.next

        return copy_head.next
