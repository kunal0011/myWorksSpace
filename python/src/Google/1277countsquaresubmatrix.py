"""
LeetCode 1277: Count Square Submatrices with All Ones

Problem Statement:
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
A square matrix is a matrix with equal number of rows and columns.

Logic:
1. Use dynamic programming where dp[i][j] represents the size of largest square ending at position (i,j)
2. For each cell (i,j):
   - If matrix[i][j] = 0, dp[i][j] = 0
   - If matrix[i][j] = 1:
     * For first row/column: dp[i][j] = 1
     * For others: dp[i][j] = min(left, up, diagonal) + 1
3. Total squares = sum of all values in dp array

Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""

from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        total_squares = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1  # First row or first column
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1],
                                       dp[i-1][j-1]) + 1
                    total_squares += dp[i][j]

        return total_squares


def test_count_squares():
    solution = Solution()
    
    # Test case 1: Basic matrix
    matrix1 = [
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]
    ]
    result1 = solution.countSquares(matrix1)
    assert result1 == 15, f"Test case 1 failed. Expected 15, got {result1}"
    print(f"Test case 1 passed: {result1} squares")
    
    # Test case 2: Single cell matrix
    matrix2 = [[1]]
    result2 = solution.countSquares(matrix2)
    assert result2 == 1, f"Test case 2 failed. Expected 1, got {result2}"
    print(f"\nTest case 2 passed: {result2} squares")
    
    # Test case 3: Empty matrix
    matrix3 = []
    result3 = solution.countSquares(matrix3)
    assert result3 == 0, f"Test case 3 failed. Expected 0, got {result3}"
    print(f"\nTest case 3 passed: {result3} squares")
    
    # Test case 4: Matrix with all zeros
    matrix4 = [[0,0],[0,0]]
    result4 = solution.countSquares(matrix4)
    assert result4 == 0, f"Test case 4 failed. Expected 0, got {result4}"
    print(f"\nTest case 4 passed: {result4} squares")
    
    print("\nAll test cases passed!")

if __name__ == "__main__":
    test_count_squares()
