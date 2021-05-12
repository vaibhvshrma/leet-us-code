class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [self.get_prefix(row) for row in matrix]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return sum(self.get_sum(i_row, col1, col2) for i_row in range(row1, row2+1))

    @staticmethod
    def get_prefix(row):
        res = []
        sm = 0
        for i in range(len(row)):
            sm += row[i]
            res.append(sm)
        return res

    def get_sum(self, i_row, col1, col2):
        return self.prefix[i_row][col2] - (0 if col1 == 0 else self.prefix[i_row][col1-1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
