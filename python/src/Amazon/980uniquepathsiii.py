from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # Get dimensions of the grid
        m, n = len(grid), len(grid[0])

        # Initialize variables
        start = None
        empty_squares = 0

        # Find the start position and count empty squares
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)  # Start position
                # Non-obstacle squares (empty or start/end)
                if grid[i][j] != -1:
                    empty_squares += 1

        # Directions for moving up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # DFS function
        def dfs(x, y, squares_visited):
            # Base case: if we reach the end square
            if grid[x][y] == 2:
                # If we've visited all non-obstacle squares, it's a valid path
                return 1 if squares_visited == empty_squares else 0

            # Temporarily mark this square as visited
            temp = grid[x][y]
            grid[x][y] = -1  # Mark as obstacle to avoid revisiting

            # Initialize path count
            path_count = 0

            # Explore all 4 directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1:
                    path_count += dfs(nx, ny, squares_visited + 1)

            # Backtrack: restore the grid value
            grid[x][y] = temp

            return path_count

        # Start DFS from the starting square
        return dfs(start[0], start[1], 1)
