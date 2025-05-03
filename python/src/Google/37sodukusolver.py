"""
LeetCode 37 - Sudoku Solver

Problem Statement:
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Time Complexity: O(9^(n*n)), where n is the board size (typically 9)
Space Complexity: O(n*n) for recursion stack
"""

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Modifies the input board in-place
        """
        def is_valid(num: str, pos: tuple) -> bool:
            # Check row
            row, col = pos
            for x in range(9):
                if board[row][x] == num and x != col:
                    return False
            
            # Check column
            for x in range(9):
                if board[x][col] == num and x != row:
                    return False
            
            # Check 3x3 box
            box_x = col // 3
            box_y = row // 3
            for i in range(box_y * 3, box_y * 3 + 3):
                for j in range(box_x * 3, box_x * 3 + 3):
                    if board[i][j] == num and (i, j) != (row, col):
                        return False
            
            return True

        def find_empty() -> tuple:
            # Find an empty position
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        return (i, j)
            return None

        def solve() -> bool:
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


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def test_sudoku_solver():
    solution = Solution()
    
    # Test cases
    test_cases = [
        [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ],
        [
            [".",".","9","7","4","8",".",".","."],
            ["7",".",".",".",".",".",".",".","."],
            [".","2",".","1",".","9",".",".","."],
            [".",".","7",".",".",".","2","4","."],
            [".","6","4",".","1",".","5","9","."],
            [".","9","8",".",".",".","3",".","."],
            [".",".",".","8",".","3",".","2","."],
            [".",".",".",".",".",".",".",".","6"],
            [".",".",".","2","7","5","9",".","."]
        ]
    ]
    
    for i, board in enumerate(test_cases, 1):
        # Make a deep copy of the board for testing
        board_copy = [row[:] for row in board]
        print(f"Test case {i}:")
        print("Original board:")
        print_board(board_copy)
        
        solution.solveSudoku(board_copy)
        
        print("\nSolved board:")
        print_board(board_copy)
        print("\n" + "="*30 + "\n")


if __name__ == "__main__":
    test_sudoku_solver()