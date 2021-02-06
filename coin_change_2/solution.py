from typing import List

class Solution:
    def rec_change(self, fc: int, amount: int):
        if amount == 0:
            return 1
        if  fc < 0 or amount < 0:
            return 0
        if self.dp[fc][amount] != -1:
            return self.dp[fc][amount]

        res = self.rec_change(fc, amount-self.coins[fc])
        res += self.rec_change(fc-1, amount)
        self.dp[fc][amount] = res
        return res

    def change(self, amount: int, coins: List[int]) -> int:
        self.coins = coins
        self.coins.sort()
        self.dp = [[-1]*(amount+1) for i in range(len(coins))]
        import sys; sys.setrecursionlimit(10000)
        self.rec_change(len(coins)-1, amount)
        print(self.dp)
        return self.dp[-1][-1]

if __name__ == "__main__":
    Solution().change(5, [1,2,5])