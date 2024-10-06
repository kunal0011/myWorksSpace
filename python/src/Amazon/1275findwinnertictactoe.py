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
