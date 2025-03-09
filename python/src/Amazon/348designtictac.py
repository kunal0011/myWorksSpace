"""
LeetCode 348: Design Tic-tac-toe

Problem Statement:
Assume the following rules are for the tic-tac-toe game on an n x n board between two players:
1. A move is guaranteed to be valid and is placed on an empty block.
2. Once a winning condition is reached, no more moves are allowed.
3. A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins.

Implement the TicTacToe class:
- TicTacToe(int n) Initializes the object with the size of the board n.
- int move(int row, int col, int player) Indicates that player with id player makes a move at cell (row, col).
  The move is guaranteed to be a valid move, and the two players alternate in making moves.
  Return 0 if no winner after the move, or 1 if player 1 wins, or 2 if player 2 wins.

Example:
Input:
["TicTacToe", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1]]
Output:
[null, 0, 0, 0, 0, 1]

Explanation:
TicTacToe ticTacToe = new TicTacToe(3);
ticTacToe.move(0, 0, 1); // return 0
ticTacToe.move(0, 2, 2); // return 0
ticTacToe.move(2, 2, 1); // return 0
ticTacToe.move(1, 1, 2); // return 0
ticTacToe.move(2, 0, 1); // return 1 (player 1 wins)

Logic:
1. Use arrays to track each row, column, and diagonal sum
2. For player 1: add 1, For player 2: add -1
3. After each move, check if any row, column, or diagonal sum equals n or -n
4. Time Complexity: O(1) for each move
5. Space Complexity: O(n) to store the rows and columns arrays
"""

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

def run_test_cases():
    print("Running test cases for TicTacToe...\n")
    
    # Test case 1: 3x3 board, Player 1 wins with horizontal line
    print("Test case 1: Player 1 wins with horizontal line")
    game1 = TicTacToe(3)
    moves1 = [
        (2, 0, 1), (0, 0, 2),
        (2, 1, 1), (0, 1, 2),
        (2, 2, 1)  # Player 1 wins
    ]
    expected1 = [0, 0, 0, 0, 1]
    results1 = []
    
    for row, col, player in moves1:
        result = game1.move(row, col, player)
        results1.append(result)
        print(f"Move: ({row}, {col}) by Player {player}, Result: {result}")
    
    print(f"Expected: {expected1}")
    print(f"Got: {results1}")
    print(f"Pass? {results1 == expected1}\n")
    
    # Test case 2: 3x3 board, Player 2 wins with diagonal
    print("Test case 2: Player 2 wins with diagonal")
    game2 = TicTacToe(3)
    moves2 = [
        (0, 1, 1), (0, 0, 2),
        (1, 0, 1), (1, 1, 2),
        (2, 1, 1), (2, 2, 2)  # Player 2 wins
    ]
    expected2 = [0, 0, 0, 0, 0, 2]
    results2 = []
    
    for row, col, player in moves2:
        result = game2.move(row, col, player)
        results2.append(result)
        print(f"Move: ({row}, {col}) by Player {player}, Result: {result}")
    
    print(f"Expected: {expected2}")
    print(f"Got: {results2}")
    print(f"Pass? {results2 == expected2}\n")
    
    # Test case 3: 2x2 board, no winner
    print("Test case 3: 2x2 board with no winner")
    game3 = TicTacToe(2)
    moves3 = [
        (0, 0, 1), (0, 1, 2),
        (1, 0, 2), (1, 1, 1)
    ]
    expected3 = [0, 0, 0, 0]
    results3 = []
    
    for row, col, player in moves3:
        result = game3.move(row, col, player)
        results3.append(result)
        print(f"Move: ({row}, {col}) by Player {player}, Result: {result}")
    
    print(f"Expected: {expected3}")
    print(f"Got: {results3}")
    print(f"Pass? {results3 == expected3}\n")
    
    # Test case 4: 4x4 board, Player 1 wins with vertical line
    print("Test case 4: 4x4 board, Player 1 wins with vertical line")
    game4 = TicTacToe(4)
    moves4 = [
        (0, 1, 1), (0, 0, 2),
        (1, 1, 1), (1, 0, 2),
        (2, 1, 1), (2, 0, 2),
        (3, 1, 1)  # Player 1 wins
    ]
    expected4 = [0, 0, 0, 0, 0, 0, 1]
    results4 = []
    
    for row, col, player in moves4:
        result = game4.move(row, col, player)
        results4.append(result)
        print(f"Move: ({row}, {col}) by Player {player}, Result: {result}")
    
    print(f"Expected: {expected4}")
    print(f"Got: {results4}")
    print(f"Pass? {results4 == expected4}")


if __name__ == "__main__":
    run_test_cases()
