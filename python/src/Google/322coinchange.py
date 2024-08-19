class Solution:
    def coinChange(self, coins, amount):
        # Initialize DP array with amount + 1 (infinity), as we want to minimize this
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins are needed to make the amount 0

        # For each coin, update the dp array
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        # If dp[amount] is still infinity, return -1, meaning it's not possible
        return dp[amount] if dp[amount] != float('inf') else -1
