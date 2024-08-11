from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        # Create a dp table where dp[i][j] will be the minimum path sum ending at (i, j)
        dp = [[float('inf')] * n for _ in range(n)]

        # Initialize the first row of dp with the first row of matrix
        for j in range(n):
            dp[0][j] = matrix[0][j]

        # Fill the dp table
        for i in range(1, n):
            for j in range(n):
                # Check the three possible cells from the previous row
                min_prev_row = dp[i-1][j]  # Directly above
                if j > 0:
                    # Top-left diagonal
                    min_prev_row = min(min_prev_row, dp[i-1][j-1])
                if j < n - 1:
                    # Top-right diagonal
                    min_prev_row = min(min_prev_row, dp[i-1][j+1])

                # Update dp table
                dp[i][j] = matrix[i][j] + min_prev_row

        # The answer is the minimum value in the last row of dp
        return min(dp[-1])


# Example usage:
print(Solution().minFallingPathSum(
    [[2, 1, 3], [6, 5, 4], [7, 8, 9]]))  # Output: 13
print(Solution().minFallingPathSum([[-19, 57], [-40, -5]]))  # Output: -59
