"""
LeetCode 79. Word Search

Problem Statement:
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters
"""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        m, n = len(board), len(board[0])

        def dfs(row: int, col: int, index: int) -> bool:
            # Base case: if we've matched all characters
            if index == len(word):
                return True

            # Check bounds and current character
            if (row < 0 or row >= m or col < 0 or col >= n or
                    board[row][col] != word[index]):
                return False

            # Mark as visited
            temp = board[row][col]
            board[row][col] = '#'

            # Try all four directions
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row, new_col = row + dx, col + dy
                if dfs(new_row, new_col, index + 1):
                    return True

            # Restore the cell
            board[row][col] = temp
            return False

        # Try each cell as starting point
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False


def test_word_search():
    solution = Solution()

    test_cases = [
        {
            "board": [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"]
            ],
            "word": "ABCCED",
            "expected": True,
            "description": "Path exists"
        },
        {
            "board": [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"]
            ],
            "word": "SEE",
            "expected": True,
            "description": "Short path exists"
        },
        {
            "board": [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"]
            ],
            "word": "ABCB",
            "expected": False,
            "description": "Path doesn't exist"
        },
        {
            "board": [["A"]],
            "word": "A",
            "expected": True,
            "description": "Single cell"
        },
        {
            "board": [
                ["A", "B"],
                ["C", "D"]
            ],
            "word": "ABDC",
            "expected": True,
            "description": "Snake pattern"
        },
        {
            "board": [
                ["A", "A", "A"],
                ["A", "A", "A"]
            ],
            "word": "AAA",
            "expected": True,
            "description": "Same letters"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        board = [row[:] for row in test_case["board"]]  # Create a copy
        word = test_case["word"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"Board:")
        for row in board:
            print(row)
        print(f"Word: {word}")

        result = solution.exist(board, word)

        assert result == expected, \
            f"Expected {expected}, but got {result}"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_word_search()
    print("\nAll test cases passed! 🎉")
