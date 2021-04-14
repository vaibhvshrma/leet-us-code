# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nums = self._flatten(nestedList)
        self.ptr = 0

    @staticmethod
    def _flatten(arr):
        if not arr:
            return []
        res = []
        for elem in arr:
            if not elem.isInteger():
                res.extend(NestedIterator._flatten(elem.getList()))
            else:
                res.append(elem.getInteger())
        return res

    def next(self) -> int:
        self.ptr += 1
        return self.nums[self.ptr-1]


    def hasNext(self) -> bool:
        return self.ptr < len(self.nums)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())