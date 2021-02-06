import heapq
import math
from typing import List

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        mx_heap = [-elem * (1 + (elem & 1)) for elem in nums]
        heapq.heapify(mx_heap)
        min_val = -max(mx_heap)
        res = math.inf
        while True:
            max_val = -heapq.heappop(mx_heap)
            res = min(res, max_val - min_val)
            if max_val & 1:
                return res
            val = max_val >> 1
            min_val = min(min_val, val)
            heapq.heappush(mx_heap, -val)

if __name__ == '__main__':
    nums = [1,2,3,4]
    res = Solution().minimumDeviation(nums)
    print(res)