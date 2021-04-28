class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1] :
            return 0

        r, c = len(obstacleGrid), len(obstacleGrid[0])
        try:
            first_obstacle = obstacleGrid[0].index(1)
            dp = ([1] * first_obstacle) + ([0] * (c-first_obstacle))
        except ValueError:
            dp = [1] * c


        for i in range(1, r):
            if obstacleGrid[i][0] == 1:
                dp[0] = 0
            for j in range(1, c):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                    continue

                if obstacleGrid[i-1][j] == 1:
                    dp[j] = 0

                if obstacleGrid[i][j-1] == 0:
                    dp[j] += dp[j-1]
        return dp[-1]
