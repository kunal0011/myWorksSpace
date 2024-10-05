from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        def backtrack(i, j, index):
            # Base case: if all characters in the word are found
            if index == len(word):
                return True

            # Base case: out of bounds or mismatch in character
            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or board[i][j] != word[index]:
                return False

            # Mark current cell as visited
            visited[i][j] = True

            # Explore neighbors in all four directions
            found = (backtrack(i + 1, j, index + 1) or
                     backtrack(i - 1, j, index + 1) or
                     backtrack(i, j + 1, index + 1) or
                     backtrack(i, j - 1, index + 1))

            # Backtrack: unmark current cell
            visited[i][j] = False

            return found

        # Start search from each cell in the board
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backtrack(i, j, 0):
                    return True

        return False
