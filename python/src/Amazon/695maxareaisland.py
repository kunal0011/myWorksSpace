"""
LeetCode 695: Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid 
are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.
"""

from typing import List, Set, Tuple


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r: int, c: int, visited: Set[Tuple[int, int]]) -> int:
            # Base case: if out of bounds, at water, or already visited
            if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) 
                or grid[r][c] == 0 or (r, c) in visited):
                return 0

            # Add current cell to visited set
            visited.add((r, c))

            # Recursively count the area by exploring the neighboring cells
            return 1 + dfs(r+1, c, visited) + dfs(r-1, c, visited) + \
                   dfs(r, c+1, visited) + dfs(r, c-1, visited)

        visited = set()
        max_area = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c, visited))

        return max_area


def test_max_area_of_island():
    test_cases = [
        # grid, expected
        (
            [
                [0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]
            ],
            6
        ),
        ([[0,0,0,0,0,0,0,0]], 0),
        ([[1]], 1),
    ]
    
    solution = Solution()
    for i, (grid, expected) in enumerate(test_cases, 1):
        result = solution.maxAreaOfIsland(grid)
        print(f"Test case {i}:")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}\n")


if __name__ == "__main__":
    test_max_area_of_island()
