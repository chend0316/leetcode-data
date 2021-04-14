from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.rowUsed = [set() for _ in range(9)]
        self.colUsed = [set() for _ in range(9)]
        self.blockUsed = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    self._set(row, col, board[row][col])
        self._solve(board, 0)

    def _solve(self, board: List[List[str]], i):
        if i == 81: return True
        row, col = i // 9, i % 9
        if board[row][col] != '.':
            return self._solve(board, i + 1)
        for num in '123456789':
            if self._in(row, col, num): continue
            board[row][col] = num
            self._set(row, col, num)
            if self._solve(board, i + 1):
                return True
            else:
                board[row][col] = '.'
                self._unset(row, col, num)
        return False

    def _in(self, row, col, c):
        return c in self.rowUsed[row] or c in self.colUsed[col] or c in self.blockUsed[row//3*3 + col//3]

    def _set(self, row, col, c):
        self.rowUsed[row].add(c)
        self.colUsed[col].add(c)
        self.blockUsed[row//3*3 + col//3].add(c)
    
    def _unset(self, row, col, c):
        self.rowUsed[row].remove(c)
        self.colUsed[col].remove(c)
        self.blockUsed[row//3*3 + col//3].remove(c)
