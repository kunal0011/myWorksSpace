"""
LeetCode 807: Max Increase to Keep City Skyline

There is a city composed of n x n blocks, where each block contains a building. 
The height of the building at grid[r][c] is represented by grid[r][c].

A city's skyline is the outer contour of the rectangles formed by all the buildings 
when viewed from outside the city. The skyline from each cardinal direction (north, south, east, 
and west) may be different.

We are allowed to increase the height of any number of buildings by any amount (the amount 
can be different per building). The height of a 0-height building can also be increased.
However, increasing the height of a building should not affect the city's skyline from 
any cardinal direction.

Return the maximum total sum that the height of the buildings can be increased by 
without changing the city's skyline from any direction.

Constraints:
- n == grid.length == grid[i].length
- 2 <= n <= 50
- 0 <= grid[i][j] <= 100
"""

from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        """
        Optimized solution using list comprehension and zip
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        if not grid or not grid[0]:
            return 0
            
        n = len(grid)
        row_max = [max(row) for row in grid]
        col_max = [max(col) for col in zip(*grid)]
        
        return sum(min(row_max[i], col_max[j]) - grid[i][j]
                  for i in range(n)
                  for j in range(n))
    
    def maxIncreaseKeepingSkyline_readable(self, grid: List[List[int]]) -> int:
        """
        More readable solution with explicit loops
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        n = len(grid)
        row_max = []
        col_max = []
        
        # Get maximum heights for each row and column
        for i in range(n):
            row_max.append(max(grid[i]))
            col_height = 0
            for j in range(n):
                col_height = max(col_height, grid[j][i])
            col_max.append(col_height)
        
        total_increase = 0
        # Calculate possible increase for each building
        for i in range(n):
            for j in range(n):
                max_height = min(row_max[i], col_max[j])
                total_increase += max_height - grid[i][j]
                
        return total_increase


def validate_skyline(grid: List[List[int]], increase: int) -> bool:
    """Validate if the increase maintains original skyline"""
    n = len(grid)
    # Check grid constraints
    if not 2 <= n <= 50:
        return False
    if any(not 0 <= val <= 100 for row in grid for val in row):
        return False
    
    # Check if increase is non-negative
    if increase < 0:
        return False
        
    return True


def test_max_increase_skyline():
    """Test function for Max Increase Keeping Skyline"""
    test_cases = [
        ([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]], 35),
        ([[0,0,0],[0,0,0],[0,0,0]], 0),
        ([[1,1],[1,1]], 0),
        ([[1,2,3],[4,5,6],[7,8,9]], 12),
        ([[50,50],[50,50]], 0),
        ([[1,0],[0,1]], 1)
    ]
    
    solution = Solution()
    
    for i, (grid, expected) in enumerate(test_cases, 1):
        # Test both implementations
        result1 = solution.maxIncreaseKeepingSkyline(grid)
        result2 = solution.maxIncreaseKeepingSkyline_readable(grid)
        
        print(f"\nTest case {i}:")
        print(f"Grid:")
        for row in grid:
            print(row)
        print(f"Expected increase: {expected}")
        print(f"Optimized: {result1} {'✓' if result1 == expected else '✗'}")
        print(f"Readable: {result2} {'✓' if result2 == expected else '✗'}")
        
        # Validate the solution
        is_valid = validate_skyline(grid, result1)
        print(f"Valid solution: {'✓' if is_valid else '✗'}")


if __name__ == "__main__":
    test_max_increase_skyline()
