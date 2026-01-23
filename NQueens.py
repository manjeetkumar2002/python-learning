class Solution:

    def isSafe(self, row, col, board, n):
        duprow = row
        dupcol = col

        # diagonal upward check
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        # row check
        row = duprow
        col = dupcol
        while col >= 0:
            if board[row][col] == "Q":
                return False
            col -= 1
        # diagonal downward check
        row = duprow
        col = dupcol
        while col >= 0 and row < n:
            if board[row][col] == "Q":
                return False
            col -= 1
            row += 1
        return True

    def solve(self, col, board, n, ans):
        if col == n:
            ans.append(board.copy())
            return

        for row in range(n):
            if self.isSafe(row, col, board, n):
                board[row] = board[row][:col] + "Q" + board[row][col + 1:n]
                self.solve(col + 1, board, n, ans)
                board[row] = board[row][:col] + "." + board[row][col + 1:n]

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = ["." * n for _ in range(n)]
        self.solve(0, board, n, ans)
        return ans