"""
LeetCode 221 - Maximal Square

Problem Statement:
Given an m x n binary matrix filled with 0's and 1's, find the largest square submatrix
containing only 1's and return its area.

Solution Logic:
1. Use Dynamic Programming approach
2. dp[i][j] represents the side length of max square ending at position (i,j)
3. For each cell with '1':
   - If at edge (i=0 or j=0), dp[i][j] = 1
   - Else, dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
4. Track maximum side length found
5. Time: O(m*n), Space: O(m*n)
"""

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_side = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1],
                                       dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side


def test_maximal_square():
    solution = Solution()
    
    # Test Case 1: Basic case
    matrix1 = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    print("Test 1:")
    print("Matrix:")
    for row in matrix1:
        print(row)
    print(f"Maximal square area: {solution.maximalSquare(matrix1)}")  # Expected: 4
    
    # Test Case 2: All zeros
    matrix2 = [["0"]]
    print("\nTest 2:")
    print("Matrix:", matrix2)
    print(f"Maximal square area: {solution.maximalSquare(matrix2)}")  # Expected: 0
    
    # Test Case 3: All ones
    matrix3 = [["1","1"],["1","1"]]
    print("\nTest 3:")
    print("Matrix:")
    for row in matrix3:
        print(row)
    print(f"Maximal square area: {solution.maximalSquare(matrix3)}")  # Expected: 4

if __name__ == "__main__":
    test_maximal_square()
