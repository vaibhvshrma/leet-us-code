class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        res = 0
        coins.sort()
        for c in coins:
            if c <= res+1:
                res += c
            else:
                break
        return res + 1
