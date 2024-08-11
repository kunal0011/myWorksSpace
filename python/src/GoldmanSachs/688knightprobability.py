class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        directions = [(-2, -1), (-1, -2), (1, -2), (2, -1),
                      (2, 1), (1, 2), (-1, 2), (-2, 1)]

        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k + 1)]
        dp[0][row][column] = 1  # Starting position

        for move in range(1, k + 1):
            for r in range(n):
                for c in range(n):
                    for dr, dc in directions:
                        prev_r, prev_c = r + dr, c + dc
                        if 0 <= prev_r < n and 0 <= prev_c < n:
                            dp[move][r][c] += dp[move - 1][prev_r][prev_c] / 8

        # Sum the probabilities for all cells after k moves
        result = 0
        for r in range(n):
            for c in range(n):
                result += dp[k][r][c]

        return result
