from typing import List

"""
LeetCode 51. N-Queens

Problem Statement:
The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' indicates a queen and '.' indicates an empty space.

Example 1:
Input: n = 4
Output: [
    [".Q..",  // Solution 1
     "...Q",
     "Q...",
     "..Q."],
    
    ["..Q.",  // Solution 2
     "Q...",
     "...Q",
     ".Q.."]
]

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
- 1 <= n <= 9
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row: int):
            if row == n:
                # All queens are placed, add the solution
                result.append(["".join(board[i]) for i in range(n)])
                return

            for col in range(n):
                # Check if the current position is under attack
                if col in cols or (row + col) in diag1 or (row - col) in diag2:
                    continue

                # Place the queen
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)

                # Try next row
                backtrack(row + 1)

                # Remove the queen (backtrack)
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)

        # Initialize result and board
        result = []
        board = [['.'] * n for _ in range(n)]

        # Sets to track attacked positions
        cols = set()       # Columns where queens are placed
        diag1 = set()      # Diagonals (row + col)
        diag2 = set()      # Diagonals (row - col)

        backtrack(0)
        return result


def explain_solution(n: int) -> None:
    """
    Explains the solution process with visualization
    """
    print(f"\nSolving N-Queens for n = {n}")
    print("=" * 50)

    def print_board(board: List[List[str]], row: int = -1, col: int = -1):
        """Prints current board state with optional highlighting"""
        for i in range(len(board)):
            for j in range(len(board)):
                if i == row and j == col:
                    print('?', end=' ')  # Current attempt
                else:
                    print(board[i][j], end=' ')
            print()
        print()

    def backtrack(row: int, board: List[List[str]],
                  cols: set, diag1: set, diag2: set, depth: int = 0):
        indent = "  " * depth
        if row == n:
            print(f"{indent}Found solution:")
            print_board(board)
            solutions.append(["".join(row) for row in board])
            return

        print(f"{indent}Trying row {row}")
        for col in range(n):
            if col in cols or (row + col) in diag1 or (row - col) in diag2:
                print(f"{indent}Position ({row},{col}) is under attack")
                continue

            print(f"{indent}Trying position ({row},{col}):")
            board[row][col] = 'Q'
            print_board(board, row, col)

            cols.add(col)
            diag1.add(row + col)
            diag2.add(row - col)

            backtrack(row + 1, board, cols, diag1, diag2, depth + 1)

            board[row][col] = '.'
            cols.remove(col)
            diag1.remove(row + col)
            diag2.remove(row - col)

    solutions = []
    board = [['.'] * n for _ in range(n)]
    backtrack(0, board, set(), set(), set())

    print(f"\nFound {len(solutions)} solutions:")
    for i, sol in enumerate(solutions, 1):
        print(f"\nSolution {i}:")
        for row in sol:
            print(' '.join(row))


def test_nqueens():
    """
    Test function with various test cases
    """
    solution = Solution()
    test_cases = [
        {
            "n": 4,
            "expected_count": 2,
            "description": "4x4 board"
        },
        {
            "n": 1,
            "expected_count": 1,
            "description": "1x1 board"
        },
        {
            "n": 5,
            "expected_count": 10,
            "description": "5x5 board"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        n = test_case["n"]
        expected_count = test_case["expected_count"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: n = {n}")

        result = solution.solveNQueens(n)

        assert len(result) == expected_count, \
            f"\nTest case {i} failed!\nExpected {expected_count} solutions, got {len(result)}"
        print(f"✓ Test case {i} passed! Found {len(result)} solutions")


if __name__ == "__main__":
    try:
        test_nqueens()
        print("\nAll test cases passed successfully! 🎉")

        # Demonstrate solution process
        explain_solution(4)
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
