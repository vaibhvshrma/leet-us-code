class Solution:
    def dfs(self, x, y):
        grid = self.grid
        row, col = len(grid), len(grid[0])
        if not (0 <= x < row and 0 <= y < col):
            return 0
        if grid[x][y] == 0 or grid[x][y] == -1:
            return 0
        nbrs = [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]
        grid[x][y] = -1
        res = sum(self.dfs(i, j) for i, j in nbrs)

        return res + 1

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        return max(self.dfs(i, j) for i in range(len(grid)) for j in range(len(grid[0])))
