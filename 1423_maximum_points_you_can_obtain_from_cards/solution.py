class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) <= k:
            return sum(cardPoints)
        res = sum(cardPoints[:k])
        curr_sum = res
        for i in range(k):
            curr_sum += cardPoints[-i-1] - cardPoints[k-i-1]
            res = max(res, curr_sum)
        return res
