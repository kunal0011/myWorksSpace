MOD = 10**9 + 7


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # 3D DP table to store results for each move at each cell
        dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]

        # Starting position
        dp[0][startRow][startColumn] = 1
        result = 0

        # Directions for movement: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Loop over the number of moves
        for move in range(1, maxMove + 1):
            for i in range(m):
                for j in range(n):
                    if dp[move - 1][i][j] > 0:
                        for direction in directions:
                            ni, nj = i + direction[0], j + direction[1]
                            if 0 <= ni < m and 0 <= nj < n:
                                dp[move][ni][nj] = (
                                    dp[move][ni][nj] + dp[move - 1][i][j]) % MOD
                            else:
                                result = (result + dp[move - 1][i][j]) % MOD
        return result
