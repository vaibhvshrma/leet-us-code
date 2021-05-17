class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # ~160ms O(N)
        dp = {}
        words.sort(key=len)

        for word in words:
            res = 0
            for i in range(len(word)):
                sub_word = word[:i] + word[i+1:]
                res = max(res, dp.get(sub_word, 0))
            dp[word] = res + 1
        return max(dp.values())
