"""
LeetCode 322 - Coin Change

Problem Statement:
You are given an integer array coins representing coins of different denominations and 
an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

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

def run_tests():
    solution = Solution()
    
    test_cases = [
        ([1, 2, 5], 11, 3),  # 5 + 5 + 1 = 11
        ([2], 3, -1),        # Cannot make amount 3 with only coin 2
        ([1], 0, 0),         # Amount 0 needs 0 coins
        ([1], 1, 1),         # Amount 1 needs 1 coin
        ([1, 2, 5], 100, 20),# Tests larger amount
        ([186, 419, 83, 408], 6249, 20)  # Complex case
    ]
    
    for i, (coins, amount, expected) in enumerate(test_cases, 1):
        result = solution.coinChange(coins, amount)
        print(f"\nTest case {i}:")
        print(f"Coins: {coins}")
        print(f"Amount: {amount}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")

if __name__ == "__main__":
    run_tests()
