"""
LeetCode 1275: Find Winner on a Tic Tac Toe Game

Problem Statement:
Two players A and B take turns placing characters into empty squares ' ' of a 3 x 3 board.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are represented by 1 and -1 respectively in the board.
Return 'A' if player A wins, 'B' if player B wins, 'Draw' if the game ends in a draw, and 'Pending' if the game is still ongoing.

Logic:
1. Use a 3x3 matrix to represent board (1 for A, -1 for B)
2. For each move:
   - Place appropriate value based on turn (even index = A, odd = B)
   - Check for winner after each move:
     * Sum rows, columns, diagonals
     * If sum equals 3 or -3, we have a winner
3. Return appropriate result based on game state

Time Complexity: O(m) where m is number of moves
Space Complexity: O(1) for 3x3 board
"""

from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # Initialize the board
        board = [[0] * 3 for _ in range(3)]

        def check_winner():
            # Check rows, columns, and diagonals
            for i in range(3):
                if abs(sum(board[i])) == 3:
                    return board[i][0]
                if abs(sum(board[j][i] for j in range(3))) == 3:
                    return board[0][i]
            if abs(board[0][0] + board[1][1] + board[2][2]) == 3:
                return board[0][0]
            if abs(board[0][2] + board[1][1] + board[2][0]) == 3:
                return board[0][2]
            return 0

        # Process each move
        for index, (row, col) in enumerate(moves):
            player = 1 if index % 2 == 0 else -1
            board[row][col] = player

            # Check if the current player has won
            winner = check_winner()
            if winner != 0:
                return 'A' if winner == 1 else 'B'

        # Check if the board is full
        if len(moves) == 9:
            return "Draw"

        return "Pending"


def test_tic_tac_toe():
    solution = Solution()

    # Test case 1: A wins
    moves1 = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
    result1 = solution.tictactoe(moves1)
    assert result1 == "A", f"Test case 1 failed. Expected 'A', got {result1}"
    print(f"Test case 1 passed: {result1}")

    # Test case 2: B wins
    moves2 = [[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 2]]
    result2 = solution.tictactoe(moves2)
    assert result2 == "B", f"Test case 2 failed. Expected 'B', got {result2}"
    print(f"\nTest case 2 passed: {result2}")

    # Test case 3: Draw
    moves3 = [[0, 0], [1, 1], [2, 0], [1, 0], [
        1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
    result3 = solution.tictactoe(moves3)
    assert result3 == "Draw", f"Test case 3 failed. Expected 'Draw', got {result3}"
    print(f"\nTest case 3 passed: {result3}")

    # Test case 4: Pending
    moves4 = [[0, 0], [1, 1], [2, 0]]
    result4 = solution.tictactoe(moves4)
    assert result4 == "Pending", f"Test case 4 failed. Expected 'Pending', got {result4}"
    print(f"\nTest case 4 passed: {result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_tic_tac_toe()
