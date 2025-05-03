"""
LeetCode 419: Battleships in a Board

Problem Statement:
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] is either '.' or 'X'
"""


def countBattleships(board: list[list[str]]) -> int:
    # One-pass solution without modifying the input board
    # We only count the top-left cell of each battleship

    if not board or not board[0]:
        return 0

    count = 0
    m, n = len(board), len(board[0])

    for i in range(m):
        for j in range(n):
            # Only count cells that are:
            # 1. Marked as battleship ('X')
            # 2. Don't have battleship cell above them
            # 3. Don't have battleship cell to their left
            if (board[i][j] == 'X' and
                (i == 0 or board[i-1][j] != 'X') and
                    (j == 0 or board[i][j-1] != 'X')):
                count += 1

    return count

# Test driver


def run_tests():
    # Test cases
    test_cases = [
        {
            "board": [
                ["X", ".", ".", "X"],
                [".", ".", ".", "X"],
                ["X", ".", ".", "X"]
            ],
            "expected": 3
        },
        {
            "board": [["."]],
            "expected": 0
        },
        {
            "board": [
                ["X", "X", "X"]
            ],
            "expected": 1
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = countBattleships(test["board"])
        status = "PASSED" if result == test["expected"] else "FAILED"
        print(f"Test {i}: {status}")
        print(f"Input board:")
        for row in test["board"]:
            print(row)
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}\n")


if __name__ == "__main__":
    print("Running test cases for Battleships in a Board problem:\n")
    run_tests()

"""
Solution Logic Explanation:

1. Optimal Approach (One-Pass, O(1) extra space):
   - Instead of counting all cells or using visited array, we only count the "start" of each battleship
   - A start cell is the top-leftmost cell of each battleship
   - We can identify start cells by checking if they have no battleship cells above or to their left

2. Key Points:
   - We only count a cell if it's:
     a) Marked as 'X'
     b) Has no 'X' above it (first row or cell above is '.')
     c) Has no 'X' to its left (first column or cell to left is '.')
   - This ensures we count each battleship exactly once
   - Works because battleships are guaranteed to be:
     * Not adjacent
     * Only horizontal or vertical

3. Time and Space Complexity:
   - Time: O(m*n) where m and n are the dimensions of the board
   - Space: O(1) as we only use a counter variable
   - No need for extra visited array or board modification
"""
