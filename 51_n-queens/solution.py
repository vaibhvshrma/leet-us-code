import functools
from typing import List

class Solution:
    @staticmethod
    def get_result_board(queens):
        n = len(queens)
        board = ["".join(["Q" if i == pos else "." for i in range(n)]) for pos in queens]
        return board

    @staticmethod
    @functools.cache
    def endangered_places(row, col, n):
        res = [(i, j) for i in range(n) for j in range(n) if (
            i == row
            or j == col
            or i-row == j-col
            or i+j == row+col
        )]
        return set(res)

    def is_safe_from_queen(self, i_qn, row, col):
        q_row, q_col = i_qn, self.queens[i_qn]
        return (row, col) not in self.endangered_places(q_row, q_col, len(self.queens))

    def is_safe(self, row, col):
        return all(
            self.is_safe_from_queen(i_qn, row, col)
            for i_qn, pos in enumerate(self.queens)
            if pos != -1
        )

    def place_queen(self, n, row):
        if row == n:
            self.res.append(self.get_result_board(self.queens))
            return
        for i in range(n):
            if self.is_safe(row, i):
                self.queens[row] = i
                self.place_queen(n, row+1)
                self.queens[row] = -1

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        self.queens = [-1] * n
        self.place_queen(n, 0)
        return self.res
