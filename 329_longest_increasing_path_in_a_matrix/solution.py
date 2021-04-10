class Solution:
    @functools.cache
    def lip(self, i, j):
        if not self.is_in_bounds(i, j):
            return 0

        self.set_processing(i, j, True)
        res = 1
        nbrs = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]

        for x, y in nbrs:
            if (
                self.is_in_bounds(x, y)
                and not self.is_processing(x, y)
                and self.val(x, y) < self.val(i, j)
            ):
                res = max(res, 1+self.lip(x, y))

        self.set_processing(i, j, False)

        return res

    def set_processing(self, i, j, val):
        if val:
            self.processing.add((i, j))
        else:
            self.processing.discard((i, j))

    def is_processing(self, i, j):
        return (i,j) in self.processing

    def is_in_bounds(self, i, j):
        r, c = self.r, self.c
        return  0 <= i < r and 0 <= j < c

    def val(self, i, j):
        return self.matrix[i][j]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        self.r, self.c = len(matrix), len(matrix[0])
        self.processing = set()
        self.matrix = matrix
        res = 1

        for i in range(self.r):
            for j in range(self.c):
                res = max(res, self.lip(i, j))

        return res
