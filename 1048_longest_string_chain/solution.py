class Solution:
    # ~2600ms, find solution2 for better approach
    @staticmethod
    def is_greater(a: str, b: str) -> bool:
        # a > b
        if not len(a) == len(b) + 1:
            return False
        for i in range(len(a)):
            if a[:i] + a[i+1:] == b:
                return True
        return False

    def longestStrChain(self, words: List[str]) -> int:
        dp = [1] * len(words)
        words.sort(key=lambda x: len(x))

        for i in range(1, len(words)):
            for j in range(i-1, -1, -1):
                if len(words[j]) < len(words[i]) - 1:
                    break
                if self.is_greater(words[i], words[j]):
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)
