from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)

        # If (target + total_sum) is odd or target is larger than total_sum, no solution exists
        if (total_sum + target) % 2 != 0 or abs(target) > total_sum:
            return 0

        # Subset sum we are looking for
        subset_sum = (total_sum + target) // 2

        # DP array to count the number of ways to reach each sum
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # There's one way to make sum 0 (by choosing no elements)

        # Dynamic programming to fill dp array
        for num in nums:
            # Traverse backward to ensure that each number is only used once
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[subset_sum]
