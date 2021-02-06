class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # Cell = namedtuple('Cell', ['neg', 'pref'])
        n = len(dungeon)
        m = len(dungeon[0])
        dp = [[0]*m for i in range(n)]
        
        # dp[0][0] = Cell(0 if dungeon[0][0] > 0 else dungeon[0][0], dungeon[0][0])
        last = dungeon[-1][-1]
        dp[-1][-1] = abs(last) + 1 if last < 0 else 1
        
        for i in range(n-2, -1, -1):
            dp[i][-1] = dp[i+1][-1] - dungeon[i][-1]
            if dp[i][-1] <= 0:
                dp[i][-1] = 1

        for i in range(m-2, -1, -1):
            dp[-1][i] = dp[-1][i+1] - dungeon[-1][i]
            if dp[-1][i] <= 0:
                dp[-1][i] = 1

        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                dp[i][j] = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                if dp[i][j] <= 0:
                    dp[i][j] = 1

        for i in dp:  print(i)
        
        return (dp[0][0])
