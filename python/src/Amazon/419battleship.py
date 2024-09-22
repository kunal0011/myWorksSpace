class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        if not board or not board[0]:
            return 0

        rows, cols = len(board), len(board[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                # We count a new battleship only if:
                # - The current cell is 'X'
                # - There is no 'X' above or to the left of the current cell
                if board[r][c] == 'X':
                    if (r == 0 or board[r-1][c] != 'X') and (c == 0 or board[r][c-1] != 'X'):
                        count += 1

        return count


# Example usage
solution = Solution()

# Test case 1
board1 = [
    ["X", ".", ".", "X"],
    [".", ".", ".", "X"],
    [".", ".", ".", "X"]
]
print(solution.countBattleships(board1))  # Expected output: 2

# Test case 2
board2 = [
    ["X", "X", "X", "X"],
    [".", ".", ".", "."],
    ["X", "X", ".", "X"]
]
print(solution.countBattleships(board2))  # Expected output: 3
