class Solution:
    def solveSudoku(self, board):
        def is_valid(board, row, col, num):
            # Check if 'num' is not in the current row
            for x in range(9):
                if board[row][x] == num:
                    return False

            # Check if 'num' is not in the current column
            for x in range(9):
                if board[x][col] == num:
                    return False

            # Check if 'num' is not in the current 3x3 sub-grid
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col + 3):
                    if board[r][c] == num:
                        return False

            return True

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in '123456789':
                            if is_valid(board, i, j, num):
                                board[i][j] = num
                                if solve(board):
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        solve(board)


# Example usage
solution = Solution()
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", ".", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".5"],
    [".", ".", ".", "4", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

solution.solveSudoku(board)
for row in board:
    print(row)
