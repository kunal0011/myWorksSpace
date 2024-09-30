from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        # If total sum is odd, we can't partition into two equal subsets
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(nums)

        # DP array to check if a subset sum is possible
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]
