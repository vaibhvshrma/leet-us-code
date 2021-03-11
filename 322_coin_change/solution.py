class Solution:
    def rec_change(self, amount):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if self.dp[amount] != -1:
            return self.dp[amount]

        res = self.INF
        for coin in self.coins:
            if coin > amount:
                break
            moves = self.rec_change(amount-coin)
            if moves != -1:
                res = min(res, moves+1)

        self.dp[amount] = res
        return self.dp[amount]


    def coinChange(self, coins: List[int], amount: int) -> int:
        self.INF = amount+10
        self.coins = sorted(coins)
        self.dp = [-1] * (amount+2)
        res = self.rec_change(amount)
        return res if res <= amount else -1
