"""
LeetCode 463 - Island Perimeter

Problem Statement:
-----------------
You are given row x col grid representing a map where grid[i][j] = 1 represents land 
and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely 
surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around 
the island. One cell is a square with side length 1. The grid is rectangular, width and height 
don't exceed 100. Determine the perimeter of the island.

Key Points:
----------
1. Exactly one island (connected group of 1's)
2. No lakes (water surrounded by land)
3. Each cell connects only horizontally/vertically
4. Each land cell contributes 4 to perimeter
5. Subtract 2 for each adjacent land cell pair

Examples:
--------
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes as shown in the diagram.

Input: grid = [[1]]
Output: 4

Input: grid = [[1,0]]
Output: 4

Constraints:
-----------
* row == grid.length
* col == grid[i].length
* 1 <= row, col <= 100
* grid[i][j] is 0 or 1
"""

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        Calculate the perimeter of the island in the grid.
        
        Algorithm:
        1. For each land cell, add 4 to perimeter
        2. For each adjacent pair of land cells, subtract 2
           (because shared edge isn't part of perimeter)
        3. Only need to check right and bottom neighbors to avoid counting twice
        
        Time Complexity: O(m*n) where m,n are grid dimensions
        Space Complexity: O(1) only using constant extra space
        """
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Each land cell contributes 4 sides initially
                    perimeter += 4

                    # Check and subtract for adjacent land cells
                    # Only need to check right and bottom to avoid double counting
                    if r < rows - 1 and grid[r + 1][c] == 1:
                        perimeter -= 2  # Shared edge between vertical neighbors
                    if c < cols - 1 and grid[r][c + 1] == 1:
                        perimeter -= 2  # Shared edge between horizontal neighbors

        return perimeter


def print_grid(grid: List[List[int]]) -> None:
    """Helper function to visualize the grid"""
    for row in grid:
        print(" ".join(["█" if cell == 1 else "·" for cell in row]))


def test_island_perimeter():
    """
    Test driver for island perimeter calculation
    """
    test_cases = [
        (
            [
                [0,1,0,0],
                [1,1,1,0],
                [0,1,0,0],
                [1,1,0,0]
            ],
            16  # Basic case with multiple connected cells
        ),
        (
            [[1]],
            4   # Single cell island
        ),
        (
            [[1,0]],
            4   # Single cell with adjacent water
        ),
        (
            [
                [1,1,1,1],
                [1,1,1,1],
                [1,1,1,1]
            ],
            16  # Rectangular island
        ),
        (
            [
                [0,0,0,0],
                [0,1,0,0],
                [0,0,0,0]
            ],
            4   # Isolated single cell
        ),
        (
            [
                [1,1],
                [1,1]
            ],
            8   # 2x2 square island
        ),
        (
            [
                [1,0,1],
                [0,1,0],
                [1,0,1]
            ],
            16  # Disconnected land cells
        ),
        (
            [
                [1,1,1],
                [1,0,1],
                [1,1,1]
            ],
            16  # Island with a hole (not possible in constraints but good edge case)
        )
    ]
    
    solution = Solution()
    
    for i, (grid, expected) in enumerate(test_cases, 1):
        result = solution.islandPerimeter(grid)
        status = "PASSED" if result == expected else "FAILED"
        print(f"\nTest case {i}: {status}")
        print("Grid:")
        print_grid(grid)
        print(f"Expected perimeter: {expected}")
        print(f"Got: {result}")
        print("-" * 40)

if __name__ == "__main__":
    test_island_perimeter()
