
from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        total_area = 0

        for i in range(n):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    # Add top and bottom faces
                    total_area += 2

                    # Check front (i-1), back (i+1), left (j-1), right (j+1) faces
                    # For each, check if neighboring cell is present and less than current cell
                    # Otherwise, consider as exposed
                    # Front
                    if i == 0:
                        total_area += grid[i][j]
                    else:
                        total_area += max(grid[i][j] - grid[i-1][j], 0)

                    # Back
                    if i == n-1:
                        total_area += grid[i][j]
                    else:
                        total_area += max(grid[i][j] - grid[i+1][j], 0)

                    # Left
                    if j == 0:
                        total_area += grid[i][j]
                    else:
                        total_area += max(grid[i][j] - grid[i][j-1], 0)

                    # Right
                    if j == len(grid[0])-1:
                        total_area += grid[i][j]
                    else:
                        total_area += max(grid[i][j] - grid[i][j+1], 0)

        return total_area
