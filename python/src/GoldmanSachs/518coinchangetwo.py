from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Initialize the dp array with 0s and set dp[0] to 1
        dp = [0] * (amount + 1)
        dp[0] = 1

        # For each coin, update the dp array
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]

        return dp[amount]
