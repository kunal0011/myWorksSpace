from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return 0

        max_row = [0] * n
        max_col = [0] * n

        # Calculate max heights in each row and column
        for r in range(n):
            for c in range(n):
                max_row[r] = max(max_row[r], grid[r][c])
                max_col[c] = max(max_col[c], grid[r][c])

        # Calculate maximum increase possible for each building
        max_increase = 0
        for r in range(n):
            for c in range(n):
                max_possible_height = min(max_row[r], max_col[c])
                max_increase += max_possible_height - grid[r][c]

        return max_increase
