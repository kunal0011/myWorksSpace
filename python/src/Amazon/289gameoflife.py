"""
LeetCode 289 - Game of Life

Problem Statement:
Given a board of m x n cells, each cell has an initial state: live (1) or dead (0).
Each cell interacts with its eight neighbors using the following four rules:
1. Any live cell with fewer than two live neighbors dies (underpopulation)
2. Any live cell with two or three live neighbors lives
3. Any live cell with more than three live neighbors dies (overpopulation)
4. Any dead cell with exactly three live neighbors becomes live

The board needs to be updated in-place.
Use these states to handle in-place updates:
- 0: dead cell
- 1: live cell
- -1: live cell that will become dead
- 2: dead cell that will become live

Logic:
1. Use special states (-1, 2) to mark changes while preserving original state
2. For each cell:
   - Count live neighbors (cells with abs value 1)
   - Apply rules using special states
3. Final pass: convert all cells to their final states (0 or 1)
"""

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


def test_game_of_life():
    solution = Solution()
    
    # Test cases
    test_cases = [
        # Test case 1: Standard case
        {
            'input': [[0,1,0], [0,0,1], [1,1,1], [0,0,0]],
            'expected': [[0,0,0], [1,0,1], [0,1,1], [0,1,0]]
        },
        # Test case 2: All dead cells
        {
            'input': [[0,0,0], [0,0,0]],
            'expected': [[0,0,0], [0,0,0]]
        },
        # Test case 3: All live cells
        {
            'input': [[1,1], [1,1]],
            'expected': [[1,1], [1,1]]
        }
    ]
    
    for i, test_case in enumerate(test_cases):
        board = [row[:] for row in test_case['input']]  # Deep copy
        solution.gameOfLife(board)
        assert board == test_case['expected'], f"Test case {i + 1} failed"
        print(f"Test case {i + 1} passed")
        print("Input:")
        for row in test_case['input']:
            print(row)
        print("Output:")
        for row in board:
            print(row)
        print()

if __name__ == "__main__":
    test_game_of_life()
    print("All test cases passed!")
