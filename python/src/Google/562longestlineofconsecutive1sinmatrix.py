"""
LeetCode 562 - Longest Line of Consecutive One in Matrix

Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.
The line could be horizontal, vertical, diagonal, or anti-diagonal.

Logic:
1. Use 3D dynamic programming array where:
   - First two dimensions (i,j) represent matrix position
   - Third dimension k represents direction (0:horizontal, 1:vertical, 2:diagonal, 3:anti-diagonal)
2. For each cell containing 1:
   - Update length of consecutive ones in all 4 directions
   - Consider boundary conditions for each direction
3. Keep track of maximum length found

Time Complexity: O(m*n) where m,n are dimensions of matrix
Space Complexity: O(m*n) for the 3D DP array
"""

from typing import List


class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0

        m, n = len(mat), len(mat[0])
        # DP array: dp[i][j][k] stores the longest line of 1s ending at (i, j) in direction k
        dp = [[[0] * 4 for _ in range(n)] for _ in range(m)]
        longest = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    # Horizontal
                    dp[i][j][0] = dp[i][j-1][0] + 1 if j > 0 else 1
                    # Vertical
                    dp[i][j][1] = dp[i-1][j][1] + 1 if i > 0 else 1
                    # Diagonal
                    dp[i][j][2] = dp[i-1][j-1][2] + 1 if i > 0 and j > 0 else 1
                    # Anti-diagonal
                    dp[i][j][3] = dp[i-1][j+1][3] + \
                        1 if i > 0 and j < n-1 else 1

                    # Update longest line found
                    longest = max(
                        longest, dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3])

        return longest


def run_test_cases():
    solution = Solution()
    test_cases = [
        {
            "matrix": [[0, 1, 1, 0],
                       [0, 1, 1, 0],
                       [0, 0, 0, 1]],
            "expected": 3,
            "explanation": "Longest line of 1s is diagonal, length 3"
        },
        {
            "matrix": [[1, 1, 1, 1],
                       [0, 1, 1, 0],
                       [0, 0, 0, 1]],
            "expected": 4,
            "explanation": "Longest line of 1s is horizontal, length 4"
        },
        {
            "matrix": [[0, 1, 0],
                       [0, 1, 0],
                       [0, 1, 0]],
            "expected": 3,
            "explanation": "Longest line of 1s is vertical, length 3"
        },
        {
            "matrix": [[1]],
            "expected": 1,
            "explanation": "Single cell matrix"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.longestLine(test["matrix"])
        print(f"\nTest Case {i}:")
        print("Matrix:")
        for row in test["matrix"]:
            print(row)
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"Explanation: {test['explanation']}")
        print(f"{'✓ Passed' if result == test['expected'] else '✗ Failed'}")


if __name__ == "__main__":
    run_test_cases()
