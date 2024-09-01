class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return
            grid[r][c] = 0
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        # Remove all 1's connected to the boundary
        for i in range(rows):
            for j in [0, cols - 1]:
                if grid[i][j] == 1:
                    dfs(i, j)

        for j in range(cols):
            for i in [0, rows - 1]:
                if grid[i][j] == 1:
                    dfs(i, j)

        # Count the remaining enclaves
        return sum(grid[i][j] == 1 for i in range(rows) for j in range(cols))
