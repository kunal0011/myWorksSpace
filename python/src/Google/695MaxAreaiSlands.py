"""
LeetCode 695: Max Area of Island
Problem Statement:
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid 
are surrounded by water.
Return the maximum area of an island in grid. If there is no island, return 0.

Logic:
1. Use DFS (Depth-First Search) to explore each island
2. For each land cell (1), explore all connected land cells in 4 directions
3. Mark visited cells as 0 to avoid revisiting
4. Keep track of maximum area found

Time Complexity: O(R * C) where R = rows, C = columns
Space Complexity: O(R * C) for recursive call stack in worst case
"""

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


def test_max_area_of_island():
    solution = Solution()

    # Test Case 1: Example from LeetCode
    grid1 = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ]
    result1 = solution.maxAreaOfIsland(grid1)
    assert result1 == 6, f"Expected 6, but got {result1}"
    print("Test case 1: Complex grid with multiple islands ✓")

    # Test Case 2: No islands
    grid2 = [[0, 0, 0, 0, 0]]
    result2 = solution.maxAreaOfIsland(grid2)
    assert result2 == 0, f"Expected 0, but got {result2}"
    print("Test case 2: Grid with no islands ✓")

    # Test Case 3: Single cell island
    grid3 = [[1]]
    result3 = solution.maxAreaOfIsland(grid3)
    assert result3 == 1, f"Expected 1, but got {result3}"
    print("Test case 3: Single cell island ✓")

    # Test Case 4: Multiple islands of same size
    grid4 = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]
    ]
    result4 = solution.maxAreaOfIsland(grid4)
    assert result4 == 4, f"Expected 4, but got {result4}"
    print("Test case 4: Multiple islands of same size ✓")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_max_area_of_island()
