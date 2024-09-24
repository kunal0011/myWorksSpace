from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon or not dungeon[0]:
            return 0

        m, n = len(dungeon), len(dungeon[0])
        # Create a dp array to store the minimum health needed at each cell
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

        # The knight must have at least 1 HP to survive the last cell
        dp[m][n-1] = dp[m-1][n] = 1

        # Fill the dp table backwards (from bottom-right to top-left)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # Minimum health needed to move to the next cell (either right or down)
                min_health = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                # The knight must have at least 1 HP in any cell
                dp[i][j] = max(1, min_health)

        return dp[0][0]
