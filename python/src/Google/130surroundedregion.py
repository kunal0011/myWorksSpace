class Solution:
    def solve(self, board):
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = 'E'  # Mark this 'O' as 'E' (escaped)
            # Explore all four directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # Step 1: Mark all 'O's connected to the boundary
        for r in range(rows):
            for c in range(cols):
                if (r in [0, rows-1] or c in [0, cols-1]) and board[r][c] == 'O':
                    dfs(r, c)

        # Step 2: Flip all 'O's to 'X's and 'E's back to 'O's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  # Surrounded region
                elif board[r][c] == 'E':
                    board[r][c] = 'O'  # Not surrounded, revert to original


# Example usage
board = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]

solution = Solution()
solution.solve(board)
for row in board:
    print(row)
