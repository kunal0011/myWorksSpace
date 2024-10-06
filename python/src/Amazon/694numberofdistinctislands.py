from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(x, y, base_x, base_y):
            # Out of bounds or water, stop recursion
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return

            # Mark the current cell as visited
            grid[x][y] = 0

            # Record the relative position of this cell compared to the starting cell
            shape.append((x - base_x, y - base_y))

            # Explore all four directions
            dfs(x + 1, y, base_x, base_y)  # Down
            dfs(x - 1, y, base_x, base_y)  # Up
            dfs(x, y + 1, base_x, base_y)  # Right
            dfs(x, y - 1, base_x, base_y)  # Left

        # Set to store distinct island shapes
        distinct_islands = set()

        # Traverse the grid to find islands
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:  # Found an island
                    shape = []
                    # Perform DFS to record the shape of the island
                    dfs(i, j, i, j)
                    # Convert the shape to a tuple and add to the set
                    distinct_islands.add(tuple(shape))

        # The number of distinct islands is the size of the set
        return len(distinct_islands)
