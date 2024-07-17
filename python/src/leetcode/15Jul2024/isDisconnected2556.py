from collections import deque
from typing import List


class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        def dfs(i, j):
            if i >= m or j >= n or grid[i][j] == 0:
                return False
            grid[i][j] = 0
            if i == m - 1 and j == n - 1:
                return True
            return dfs(i + 1, j) or dfs(i, j + 1)

        m, n = len(grid), len(grid[0])
        a = dfs(0, 0)
        grid[0][0] = grid[-1][-1] = 1
        b = dfs(0, 0)
        return not (a and b)


# Example usage
grid = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 1]
]
m = len(grid)
n = len(grid[0])
s = Solution()
# Output: True or False based on the grid
print(s.isPossibleToCutPath(grid))
