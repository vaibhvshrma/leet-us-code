from typing import List

class Solution:
    def kadanes_algo(self, arr):
        if not arr:
            return 0
        max_so_far = arr[0]
        sm = 0
        for i in arr:
            sm += i
            max_so_far = max(max_so_far, sm)
            if sm < 0:
                sm = 0

        return max_so_far

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        mx = sum(A) + self.kadanes_algo([-i for i in A])
        mx_sum = self.kadanes_algo(A)
        if not mx:
            return mx_sum
        mx = max(
            self.kadanes_algo(A),
            mx
        )
        return mx