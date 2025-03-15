"""
LeetCode 892: Surface Area of 3D Shapes

You are given an n x n grid where you have placed some 1 x 1 x h cubes. Each value grid[i][j] 
represents the height of the cube placed at (i, j).

Return the total surface area of the resulting shape.

Constraints:
- n == grid.length == grid[0].length
- 1 <= n <= 50
- 0 <= grid[i][j] <= 50
"""

from typing import List

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = 0
        
        # Direction vectors for adjacent cells (up, right, down, left)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    # Add top and bottom faces
                    area += 2
                    
                    # Add lateral faces
                    height = grid[i][j]
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        # If neighbor exists, add difference in height
                        # If no neighbor, add full height
                        neighbor_height = grid[ni][nj] if 0 <= ni < n and 0 <= nj < n else 0
                        area += max(height - neighbor_height, 0)
                        
        return area

def validate_grid(grid: List[List[int]]) -> bool:
    """Validate grid according to constraints"""
    n = len(grid)
    if n < 1 or n > 50 or len(grid[0]) != n:
        return False
    return all(0 <= cell <= 50 for row in grid for cell in row)

def test_surface_area():
    """Test function for 3D Surface Area calculation"""
    test_cases = [
        ([[2]], 10),
        ([[1,2],[3,4]], 34),
        ([[1,1,1],[1,0,1],[1,1,1]], 32),
        ([[2,2,2],[2,1,2],[2,2,2]], 46),
        ([[1,0],[0,2]], 16),
        ([[1,2,3],[3,8,4],[5,3,5]], 85)
    ]
    
    solution = Solution()
    
    for i, (grid, expected) in enumerate(test_cases, 1):
        is_valid = validate_grid(grid)
        result = solution.surfaceArea(grid)
        
        print(f"\nTest case {i}:")
        print("Grid configuration:")
        for row in grid:
            print(row)
        print(f"Expected surface area: {expected}")
        print(f"Calculated surface area: {result}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        
        # Additional statistics
        total_blocks = sum(sum(row) for row in grid)
        print(f"Total blocks: {total_blocks}")
        print(f"Average surface area per block: {result/total_blocks if total_blocks else 0:.2f}")

if __name__ == "__main__":
    test_surface_area()
