class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        for i in range(1, n):
            for j in range(n):
                grid[i][j] += min(grid[i-1][k] for k in range(n) if k != j)
        return min(grid[-1])
