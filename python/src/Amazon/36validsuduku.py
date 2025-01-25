from typing import List
from collections import defaultdict

"""
LeetCode 36. Valid Sudoku

Problem Statement:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated
according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Constraints:
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit 1-9 or '.'

Approach:
1. Use sets to track numbers in each row, column, and box
2. Single pass through board
3. Time Complexity: O(1) since board is always 9x9
4. Space Complexity: O(1)
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize sets for rows, columns, and boxes
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        # Check each cell
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue

                # Get box index (0-8)
                box_idx = (i // 3) * 3 + j // 3

                # Check if value already exists in row, column, or box
                if (val in rows[i] or
                    val in cols[j] or
                        val in boxes[box_idx]):
                    return False

                # Add value to sets
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_idx].add(val)

        return True


def explain_validation(board: List[List[str]]) -> None:
    """
    Function to explain the Sudoku validation process
    """
    print("\nValidating Sudoku board:")
    print_board(board)
    print("\nChecking rules:")

    # Initialize tracking sets
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)

    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val == '.':
                continue

            box_idx = (i // 3) * 3 + j // 3

            print(f"\nChecking cell ({i},{j}) = {val}")
            print(f"Box index: {box_idx}")

            # Check and explain violations
            if val in rows[i]:
                print(f"❌ Value {val} already exists in row {i}")
                return False
            if val in cols[j]:
                print(f"❌ Value {val} already exists in column {j}")
                return False
            if val in boxes[box_idx]:
                print(f"❌ Value {val} already exists in box {box_idx}")
                return False

            # Add value to sets
            rows[i].add(val)
            cols[j].add(val)
            boxes[box_idx].add(val)
            print("✓ Valid placement")

    print("\n✓ Valid Sudoku board!")
    return True


def print_board(board: List[List[str]]) -> None:
    """
    Helper function to print Sudoku board in a readable format
    """
    print("-" * 25)
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 25)
        row = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row += "| "
            row += board[i][j] + " "
        print(row)
    print("-" * 25)


def test_valid_sudoku():
    """
    Test function to verify the isValidSudoku solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "board": [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"]
            ],
            "expected": True,
            "description": "Valid Sudoku board"
        },
        {
            "board": [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"]
            ],
            "expected": False,
            "description": "Invalid board - duplicate in row"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        board = test_case["board"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print_board(board)

        result = solution.isValidSudoku(board)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_valid_sudoku()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with an example
        valid_board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        explain_validation(valid_board)
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
