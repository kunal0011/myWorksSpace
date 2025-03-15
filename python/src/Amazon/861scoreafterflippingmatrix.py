"""
LeetCode 861: Score After Flipping Matrix

You are given an m x n binary matrix grid. A move consists of choosing any row or column 
and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

After making any number of moves, every row of this matrix is interpreted as a binary number, 
and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 20
- grid[i][j] is either 0 or 1
"""

from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        
        # Make a copy to avoid modifying input
        grid = [row[:] for row in grid]
        
        # Step 1: Ensure first column is all 1s
        for i in range(rows):
            if grid[i][0] == 0:
                self._flip_row(grid, i)
                
        # Step 2: Flip columns to maximize 1s
        for j in range(1, cols):
            ones = sum(grid[i][j] for i in range(rows))
            if ones < (rows + 1) // 2:
                self._flip_column(grid, j)
                
        # Step 3: Calculate score
        return sum(int(''.join(map(str, row)), 2) for row in grid)
    
    def _flip_row(self, grid: List[List[int]], row: int) -> None:
        """Flip all bits in given row"""
        for j in range(len(grid[0])):
            grid[row][j] ^= 1
            
    def _flip_column(self, grid: List[List[int]], col: int) -> None:
        """Flip all bits in given column"""
        for i in range(len(grid)):
            grid[i][col] ^= 1

def validate_grid(grid: List[List[int]]) -> bool:
    """Validate grid according to constraints"""
    if not grid or not grid[0]:
        return False
    m, n = len(grid), len(grid[0])
    if not (1 <= m <= 20 and 1 <= n <= 20):
        return False
    return all(x in (0, 1) for row in grid for x in row)

def print_grid(grid: List[List[int]], label: str = "") -> None:
    """Pretty print grid with binary and decimal values"""
    if label:
        print(f"\n{label}:")
    for row in grid:
        binary = ''.join(map(str, row))
        decimal = int(binary, 2)
        print(f"{binary} = {decimal}")

def test_matrix_score():
    """Test function for Matrix Score"""
    test_cases = [
        ([[0,0,1,1],[1,0,1,0],[1,1,0,0]], 39),
        ([[1]], 1),
        ([[0]], 1),
        ([[1,1,1],[1,0,1],[0,0,0]], 7),
        ([[0,0,1],[0,0,1],[0,1,1]], 7)
    ]
    
    solution = Solution()
    
    for i, (grid, expected) in enumerate(test_cases, 1):
        # Make a deep copy for displaying original
        original = [row[:] for row in grid]
        is_valid = validate_grid(grid)
        result = solution.matrixScore(grid)
        
        print(f"\nTest case {i}:")
        print("Original grid:")
        print_grid(original, "Original")
        print(f"Final score: {result}")
        print(f"Expected score: {expected}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        # Additional statistics
        print(f"Grid dimensions: {len(grid)}x{len(grid[0])}")
        original_score = sum(int(''.join(map(str, row)), 2) for row in original)
        print(f"Score improvement: {result - original_score}")

if __name__ == "__main__":
    test_matrix_score()
