class Solution:
    @staticmethod
    def lcs(w1, w2):
        m, n = len(w1), len(w2)
        dp = [[0] * (n+1) for i in range(m+1)]

        for r in range(1, m+1):
            for c in range(1, n+1):
                if w1[r-1] == w2[c-1]:
                    dp[r][c] = max(dp[r][c], 1+dp[r-1][c-1])
                dp[r][c] = max(dp[r][c], dp[r-1][c])
                dp[r][c] = max(dp[r][c], dp[r][c-1])
                dp[r][c] = max(dp[r][c], dp[r][c])
        return dp[m][n]

    def minDistance(self, word1: str, word2: str) -> int:
        val = self.lcs(word1, word2)
        return len(word1) + len(word2) - (2*val)
