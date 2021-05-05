import math
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        INF = math.inf
        n = len(nums)
        if n == 1:
            return 0
        dp = [INF] * n
        for i in range(n-2, -1, -1):
            if i + nums[i] + 1 >= n:
                dp[i] = 0
            for j in range(1, nums[i]+1):
                if i+j >= n:
                    break
                dp[i] = min(dp[i], dp[i+j])
            dp[i] += 1
        return dp[0]
