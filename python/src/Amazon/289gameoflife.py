from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Define the directions for the 8 neighbors
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1)]
        rows, cols = len(board), len(board[0])

        # Iterate through each cell
        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0

                # Count live neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and abs(board[nr][nc]) == 1:
                        live_neighbors += 1

                # Apply the rules of the Game of Life
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    # Mark as dead in the next state (but keep the information of the current state)
                    board[r][c] = -1
                if board[r][c] == 0 and live_neighbors == 3:
                    # Mark as live in the next state
                    board[r][c] = 2

        # Update the board to the next state
        for r in range(rows):
            for c in range(cols):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0
