"""
LeetCode 419 - Battleships in a Board

Problem Statement:
-----------------
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the 
number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they 
can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), 
where k can be of any size. At least one horizontal or vertical cell separates between 
two battleships (there are no adjacent battleships).

Key Points:
----------
1. Battleships are marked with 'X', empty cells with '.'
2. Battleships are either horizontal (1×k) or vertical (k×1)
3. No adjacent battleships (must have at least one cell separation)
4. The solution must use O(1) extra memory
5. The solution can modify the input board

Examples:
--------
Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2
Explanation: Two battleships are present: one horizontal and one vertical.

Input: board = [["."]]
Output: 0
Explanation: No battleships on an empty board.

Constraints:
-----------
* m == board.length
* n == board[i].length
* 1 <= m, n <= 200
* board[i][j] is either '.' or 'X'
"""

from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        """
        Count the number of battleships on the board using O(1) extra space.
        
        Algorithm:
        1. Only count the "start" of each battleship
        2. A cell is considered a battleship start if:
           - It contains 'X'
           - Has no 'X' above it
           - Has no 'X' to its left
        
        Time Complexity: O(m*n) where m,n are board dimensions
        Space Complexity: O(1) as we only use a counter
        """
        if not board or not board[0]:
            return 0

        rows, cols = len(board), len(board[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                # Count a new battleship only if:
                # - Current cell is 'X'
                # - No 'X' above or to the left (means it's the start of a battleship)
                if (board[r][c] == 'X' and 
                    (r == 0 or board[r-1][c] != 'X') and 
                    (c == 0 or board[r][c-1] != 'X')):
                    count += 1

        return count


def test_count_battleships():
    """
    Test driver for the battleships counting problem
    """
    test_cases = [
        (
            [
                ["X", ".", ".", "X"],
                [".", ".", ".", "X"],
                [".", ".", ".", "X"]
            ],
            2  # One horizontal ship and one vertical ship
        ),
        (
            [["."]], 
            0  # Empty board
        ),
        (
            [
                ["X", "X", "X", "X"],
                [".", ".", ".", "."],
                ["X", "X", ".", "X"]
            ],
            3  # Two horizontal ships and one single-cell ship
        ),
        (
            [
                [".", "X", ".", "."],
                [".", "X", ".", "."],
                [".", "X", ".", "."]
            ],
            1  # One vertical ship
        ),
        (
            [
                ["X", ".", "X", "."],
                [".", ".", ".", "."],
                ["X", ".", "X", "."]
            ],
            4  # Four single-cell ships
        )
    ]
    
    solution = Solution()
    
    for i, (board, expected) in enumerate(test_cases, 1):
        result = solution.countBattleships(board)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test case {i}: {status}")
        print("Board:")
        for row in board:
            print(row)
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print("-" * 40)

if __name__ == "__main__":
    test_count_battleships()
