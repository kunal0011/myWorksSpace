from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0

        rows, cols = len(board), len(board[0])
        count = 0

        for i in range(rows):
            for j in range(cols):
                # Check if the current cell is part of a battleship
                if board[i][j] == 'X':
                    # Check if it's the start of a new battleship
                    # Check if it's not a continuation of a horizontal or vertical ship
                    if (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                        count += 1

        return count
