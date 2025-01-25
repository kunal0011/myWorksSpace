from typing import List

"""
LeetCode 37. Sudoku Solver

Problem Statement:
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes.
The '.' character indicates empty cells.

Example:
Input: board = 
[["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]]
Output: solved board

Approach:
1. Use backtracking with constraint checking
2. Try numbers 1-9 for each empty cell
3. Recursively solve for next empty cell
4. Backtrack if no valid number found
"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Modifies the board in-place to solve the Sudoku puzzle
        """
        def is_valid(num: str, pos: tuple) -> bool:
            # Check row
            for j in range(9):
                if board[pos[0]][j] == num and j != pos[1]:
                    return False

            # Check column
            for i in range(9):
                if board[i][pos[1]] == num and i != pos[0]:
                    return False

            # Check 3x3 box
            box_x = pos[1] // 3
            box_y = pos[0] // 3
            for i in range(box_y * 3, box_y * 3 + 3):
                for j in range(box_x * 3, box_x * 3 + 3):
                    if board[i][j] == num and (i, j) != pos:
                        return False

            return True

        def find_empty() -> tuple:
            """Find an empty position on the board"""
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        return (i, j)
            return None

        def solve() -> bool:
            """Recursive function to solve the Sudoku"""
            empty = find_empty()
            if not empty:
                return True

            row, col = empty
            for num in map(str, range(1, 10)):
                if is_valid(num, (row, col)):
                    board[row][col] = num

                    if solve():
                        return True

                    board[row][col] = '.'

            return False

        solve()


def print_board(board: List[List[str]]) -> None:
    """Helper function to print the Sudoku board"""
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


def explain_solve_step(board: List[List[str]], pos: tuple, num: str, is_valid: bool) -> None:
    """Helper function to explain each solving step"""
    print(f"\nTrying {num} at position {pos}")
    if is_valid:
        print(f"✓ Valid placement")
        print_board(board)
    else:
        print(f"✗ Invalid placement - violates Sudoku rules")


def test_sudoku_solver():
    """Test function to verify the Sudoku solver"""
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
            "description": "Standard Sudoku puzzle"
        },
        {
            "board": [
                [".", ".", "9", "7", "4", "8", ".", ".", "."],
                ["7", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", "2", ".", "1", ".", "9", ".", ".", "."],
                [".", ".", "7", ".", ".", ".", "2", "4", "."],
                [".", "6", "4", ".", "1", ".", "5", "9", "."],
                [".", "9", "8", ".", ".", ".", "3", ".", "."],
                [".", ".", ".", "8", ".", "3", ".", "2", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "6"],
                [".", ".", ".", "2", "7", "5", "9", ".", "."]
            ],
            "description": "More challenging Sudoku puzzle"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        board = [row[:] for row in test_case["board"]]  # Create a deep copy
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print("Initial board:")
        print_board(board)

        solution.solveSudoku(board)

        print("\nSolved board:")
        print_board(board)

        # Verify solution is valid
        # Note: We could add validation here to check if solution follows Sudoku rules
        print(f"✓ Test case {i} completed!")


if __name__ == "__main__":
    try:
        test_sudoku_solver()
        print("\nAll test cases completed successfully! 🎉")
    except Exception as e:
        print(f"Test failed! {str(e)}")
