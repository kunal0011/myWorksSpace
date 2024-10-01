from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)

        # If k >= n // 2, we can treat it as an unlimited transactions problem
        if k >= n // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n - 1))

        # Initialize dp table
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]

        # Initialize base cases
        for j in range(k + 1):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]

        # Fill dp table
        for i in range(1, n):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])

        return dp[-1][k][0]
