from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add 1s to the start and end of the nums array to handle edge cases
        nums = [1] + nums + [1]
        n = len(nums)

        # Initialize DP table
        dp = [[0] * n for _ in range(n)]

        # Fill the DP table
        for length in range(2, n):  # length is the distance between i and j
            for i in range(n - length):  # start index
                j = i + length  # end index
                for k in range(i + 1, j):  # balloon to burst between i and j
                    dp[i][j] = max(dp[i][j], dp[i][k] + nums[i]
                                   * nums[k] * nums[j] + dp[k][j])

        return dp[0][n - 1]
