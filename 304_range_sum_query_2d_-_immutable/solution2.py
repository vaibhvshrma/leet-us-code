class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = self.get_prefix(matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        up = self.prefix[row1-1][col2] if row1 else 0
        left = self.prefix[row2][col1-1] if col1 else 0
        diag = self.prefix[row1-1][col1-1] if row1 and col1 else 0
        return self.prefix[row2][col2] - up - left + diag

    @staticmethod
    def get_prefix(matrix):
        res = []
        for row in matrix:
            pref_row = []
            sm = 0
            for i in range(len(row)):
                sm += row[i]
                pref_row.append(sm)
            res.append(pref_row)

        # add column wise to get area prefix
        # intution: 1D prefix gives linear sum
        # 2d sum will give area sum starting at (0,0)
        for i in range(1, len(res)):
            for j in range(len(res[0])):
                res[i][j] += res[i-1][j]

        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
