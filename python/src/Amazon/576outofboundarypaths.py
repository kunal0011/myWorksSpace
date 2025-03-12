"""
LeetCode 576 - Out of Boundary Paths

There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. 
You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). 
You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. 
Since the answer can be very large, return it modulo 109 + 7.

Example 1:
Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6
Explanation: There are 6 paths to move the ball out of boundary.

Example 2:
Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12

Constraints:
- 1 <= m, n <= 50
- 0 <= maxMove <= 50
- 0 <= startRow < m
- 0 <= startColumn < n
"""

from typing import List, Dict, Tuple
from functools import lru_cache


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """
        Optimized solution using dynamic programming with memoization
        Time Complexity: O(m * n * maxMove)
        Space Complexity: O(m * n * maxMove)
        """
        MOD = 10**9 + 7
        
        @lru_cache(None)
        def dp(moves: int, row: int, col: int) -> int:
            # If we're out of bounds, this is a valid path
            if row < 0 or row >= m or col < 0 or col >= n:
                return 1
            # If no moves left but still in bounds, no valid path
            if moves == 0:
                return 0
                
            paths = 0
            # Try all four directions
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row, new_col = row + dx, col + dy
                paths = (paths + dp(moves - 1, new_row, new_col)) % MOD
                
            return paths
            
        return dp(maxMove, startRow, startColumn)
    
    def findPaths_tabulation(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """
        Alternative solution using tabulation (bottom-up DP)
        Time Complexity: O(m * n * maxMove)
        Space Complexity: O(m * n)
        """
        MOD = 10**9 + 7
        
        # dp[i][j] represents number of ways to reach position (i,j)
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        count = 0
        
        # For each move
        for moves in range(maxMove):
            temp = [[0] * n for _ in range(m)]
            
            # For each cell
            for row in range(m):
                for col in range(n):
                    if dp[row][col] > 0:
                        # Try all four directions
                        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            new_row, new_col = row + dx, col + dy
                            
                            if 0 <= new_row < m and 0 <= new_col < n:
                                temp[new_row][new_col] = (temp[new_row][new_col] + dp[row][col]) % MOD
                            else:
                                count = (count + dp[row][col]) % MOD
            
            dp = temp
            
        return count


def test_find_paths():
    """
    Test function with comprehensive test cases
    """
    solution = Solution()
    
    test_cases = [
        # Basic test cases
        (2, 2, 2, 0, 0, 6),  # Example 1
        (1, 3, 3, 0, 1, 12),  # Example 2
        
        # Edge cases
        (1, 1, 1, 0, 0, 4),  # Smallest possible grid
        (1, 1, 0, 0, 0, 0),  # No moves allowed
        (2, 2, 0, 1, 1, 0),  # Center position, no moves
        
        # Test cases with different starting positions
        (3, 3, 1, 1, 1, 0),  # Center position, one move
        (3, 3, 2, 1, 1, 4),  # Center position, two moves
        
        # Larger grids
        (4, 4, 3, 1, 1, 14),
        (3, 2, 4, 0, 0, 20),
        
        # Maximum moves test
        (2, 3, 8, 1, 1, 1104),
        
        # Corner cases
        (3, 3, 3, 0, 0, 11),  # Start from corner
        (3, 3, 3, 2, 2, 11),  # Start from opposite corner
    ]
    
    print("Running tests for Out of Boundary Paths...\n")
    
    for i, (m, n, maxMove, startRow, startColumn, expected) in enumerate(test_cases, 1):
        # Test both implementations
        result1 = solution.findPaths(m, n, maxMove, startRow, startColumn)
        result2 = solution.findPaths_tabulation(m, n, maxMove, startRow, startColumn)
        
        print(f"Test Case {i}:")
        print(f"Grid: {m}x{n}, Max Moves: {maxMove}")
        print(f"Start Position: ({startRow}, {startColumn})")
        print(f"Expected: {expected}")
        print(f"Recursive DP: {result1} {'✅' if result1 == expected else '❌'}")
        print(f"Tabulation DP: {result2} {'✅' if result2 == expected else '❌'}")
        
        if result1 != expected or result2 != expected:
            print("❌ Test case failed!")
            print(f"Got: {result1} (Recursive), {result2} (Tabulation)")
            print(f"Expected: {expected}")
        else:
            print("✅ Test case passed!")
        print()


if __name__ == "__main__":
    test_find_paths()
