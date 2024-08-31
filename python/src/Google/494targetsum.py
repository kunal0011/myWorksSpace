class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total_sum = sum(nums)

        # If target is out of possible range, return 0
        if abs(target) > total_sum or (target + total_sum) % 2 != 0:
            return 0

        # Transform target to a subset sum problem
        P = (target + total_sum) // 2

        # Initialize DP array
        dp = [0] * (P + 1)
        dp[0] = 1  # There's one way to make sum 0: using an empty subset

        # Fill DP array
        for num in nums:
            for i in range(P, num - 1, -1):
                dp[i] += dp[i - num]

        return dp[P]
