"""
LeetCode 1020: Number of Enclaves

Problem Statement:
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Logic:
1. Use DFS to flood-fill all land cells connected to boundary
2. Any remaining land cells (1's) are enclaves
3. Process:
   - First mark all land cells connected to boundary as visited (change to 0)
   - Then count remaining 1's in the grid
4. Optimization: Process boundary cells first, then use DFS

Time Complexity: O(m*n) where m,n are dimensions of grid
Space Complexity: O(m*n) for recursion stack in worst case
"""

from typing import List


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


def test_num_enclaves():
    solution = Solution()

    # Test case 1: Basic case with enclaves
    grid1 = [
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    result1 = solution.numEnclaves(grid1)
    assert result1 == 3, f"Test case 1 failed. Expected 3, got {result1}"
    print(f"Test case 1 passed: enclaves={result1}")

    # Test case 2: No enclaves (all connected to boundary)
    grid2 = [
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
    ]
    result2 = solution.numEnclaves(grid2)
    assert result2 == 0, f"Test case 2 failed. Expected 0, got {result2}"
    print(f"\nTest case 2 passed: enclaves={result2}")

    # Test case 3: All cells are land
    grid3 = [
        [1, 1],
        [1, 1]
    ]
    result3 = solution.numEnclaves(grid3)
    assert result3 == 0, f"Test case 3 failed. Expected 0, got {result3}"
    print(f"\nTest case 3 passed: enclaves={result3}")

    # Test case 4: Complex case with multiple enclaves
    grid4 = [
        [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
        [1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 1]
    ]
    result4 = solution.numEnclaves(grid4)
    print(f"\nTest case 4 passed: enclaves={result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_num_enclaves()
