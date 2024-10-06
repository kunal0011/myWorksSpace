from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            # Base case: if out of bounds or at a water cell, return 0
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 0

            # Mark the cell as visited by setting it to 0
            grid[r][c] = 0

            # Recursively count the area by exploring the neighboring cells
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        max_area = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:  # Start a DFS if you find a land cell
                    max_area = max(max_area, dfs(r, c))

        return max_area
