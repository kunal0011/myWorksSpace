from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        # If the total sum is odd, we can't split it into two equal subsets
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        # Initialize DP array
        dp = [False] * (target + 1)
        dp[0] = True

        # Iterate over the numbers in nums
        for num in nums:
            # Update the dp array backwards
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]
