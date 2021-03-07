class ListNode:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mod = 997
        self.arr = [None] * self.mod

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucket = key % self.mod
        ptr = self.arr[bucket]
        if not ptr:
            self.arr[bucket] = ListNode(key, value)
            return
        prev_ptr = None
        while ptr:
            if ptr.key == key:
                ptr.val = value
                return
            prev_ptr, ptr = ptr, ptr.next

        prev_ptr.next = ListNode(key, value)


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucket = key % self.mod
        ptr = self.arr[bucket]
        while ptr:
            if ptr.key == key:
                return ptr.val
            ptr = ptr.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.put(key, -1)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)