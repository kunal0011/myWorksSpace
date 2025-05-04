"""
LeetCode 2018. Check if Word Can be Placed In Crossword

Problem Statement:
Given an m x n grid board of characters and a string word, return true if word can be placed in board,
or false otherwise. Each cell of the board contains either a '#' (wall) or ' ' (empty slot). The word 
can be placed horizontally or vertically in the board, and it must occupy a complete row or column 
between two black cells ('#') or the board's borders.

Time Complexity: O(m*n*k) where m,n are board dimensions and k is word length
Space Complexity: O(1) as we only use constant extra space
"""

from typing import List


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        # Logic:
        # 1. For each cell in board:
        #    - Try placing word horizontally (left to right)
        #    - Try placing word horizontally reversed
        #    - Try placing word vertically (top to bottom)
        #    - Try placing word vertically reversed
        # 2. For each placement:
        #    - Check if word fits between walls/borders
        #    - Check if each cell matches word or is empty
        # 3. Return true if any placement works

        rows, cols = len(board), len(board[0])
        length = len(word)

        def canPlaceHorizontally(row, col):
            # Ensure word fits in the row
            if col + length > cols:
                return False
            if col > 0 and board[row][col - 1] != '#':  # No adjacent left space
                return False
            # No adjacent right space
            if col + length < cols and board[row][col + length] != '#':
                return False
            for i in range(length):
                if board[row][col + i] not in [' ', word[i]]:
                    return False
            return True

        def canPlaceVertically(row, col):
            # Ensure word fits in the column
            if row + length > rows:
                return False
            if row > 0 and board[row - 1][col] != '#':  # No adjacent upper space
                return False
            # No adjacent lower space
            if row + length < rows and board[row + length][col] != '#':
                return False
            for i in range(length):
                if board[row + i][col] not in [' ', word[i]]:
                    return False
            return True

        def canPlaceHorizontallyReversed(row, col):
            if col - length + 1 < 0:
                return False
            if col < cols - 1 and board[row][col + 1] != '#':
                return False
            if col - length >= 0 and board[row][col - length] != '#':
                return False
            for i in range(length):
                if board[row][col - i] not in [' ', word[i]]:
                    return False
            return True

        def canPlaceVerticallyReversed(row, col):
            if row - length + 1 < 0:
                return False
            if row < rows - 1 and board[row + 1][col] != '#':
                return False
            if row - length >= 0 and board[row - length][col] != '#':
                return False
            for i in range(length):
                if board[row - i][col] not in [' ', word[i]]:
                    return False
            return True

        # Check each position for horizontal, vertical, and their reverse placements
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ' ' or board[r][c] == word[0]:
                    if canPlaceHorizontally(r, c) or canPlaceHorizontallyReversed(r, c):
                        return True
                    if canPlaceVertically(r, c) or canPlaceVerticallyReversed(r, c):
                        return True
        return False


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        (
            [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]],
            "abc"
        ),  # Expected: True
        (
            [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]],
            "ac"
        ),  # Expected: False
        (
            [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "#"]],
            "abc"
        ),  # Expected: False
        (
            [["#", "#", "#"], [" ", " ", " "], ["#", "#", "#"]],
            "aaa"
        ),  # Expected: True
    ]

    for i, (board, word) in enumerate(test_cases):
        result = solution.placeWordInCrossword(board, word)
        print(f"\nTest case {i + 1}:")
        print("Board:")
        for row in board:
            print(row)
        print(f"Word: '{word}'")
        print(f"Can be placed: {result}")

        if result:
            print("Possible placements:")
            # Check all four directions for visualization
            rows, cols = len(board), len(board[0])
            for r in range(rows):
                for c in range(cols):
                    # Show horizontal placements
                    if (c == 0 or board[r][c-1] == '#') and c + len(word) <= cols:
                        if all(board[r][c+i] in [' ', word[i]] for i in range(len(word))):
                            if c + len(word) == cols or board[r][c+len(word)] == '#':
                                print(f"Horizontal at ({r},{c})")

                    # Show vertical placements
                    if (r == 0 or board[r-1][c] == '#') and r + len(word) <= rows:
                        if all(board[r+i][c] in [' ', word[i]] for i in range(len(word))):
                            if r + len(word) == rows or board[r+len(word)][c] == '#':
                                print(f"Vertical at ({r},{c})")
        print("-" * 50)
