class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag1 = 0  # Main diagonal
        self.diag2 = 0  # Anti-diagonal

    def move(self, row: int, col: int, player: int) -> int:
        # Determine the value to add (1 for player 1, -1 for player 2)
        to_add = 1 if player == 1 else -1

        # Update the row and column for the move
        self.rows[row] += to_add
        self.cols[col] += to_add

        # Update the diagonals if applicable
        if row == col:
            self.diag1 += to_add  # Main diagonal (top-left to bottom-right)
        if row + col == self.n - 1:
            self.diag2 += to_add  # Anti-diagonal (top-right to bottom-left)

        # Check if this move wins the game
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diag1) == self.n or abs(self.diag2) == self.n:
            return player

        # No one wins with this move
        return 0

# Test cases


def test_tic_tac_toe():
    # Initialize the game with a 3x3 board
    game = TicTacToe(3)

    # Player 1 moves (0, 0)
    assert game.move(0, 0, 1) == 0, "Test case 1 failed"

    # Player 2 moves (0, 2)
    assert game.move(0, 2, 2) == 0, "Test case 2 failed"

    # Player 1 moves (2, 2)
    assert game.move(2, 2, 1) == 0, "Test case 3 failed"

    # Player 2 moves (1, 1)
    assert game.move(1, 1, 2) == 0, "Test case 4 failed"

    # Player 1 moves (2, 0)
    assert game.move(2, 0, 1) == 0, "Test case 5 failed"

    # Player 2 moves (1, 0)
    assert game.move(1, 0, 2) == 0, "Test case 6 failed"

    # Player 1 moves (2, 1) and wins the game by completing the bottom row
    assert game.move(2, 1, 1) == 1, "Test case 7 failed"

    print("All test cases passed!")


# Run the tests
test_tic_tac_toe()
