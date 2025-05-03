"""
LeetCode 518 - Coin Change II

Problem Statement:
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the number of different ways you can make amount using any combination of the coins (unlimited supply of each coin).
The order of coins doesn't matter. For example, if coins=[2,5] and amount=4, answer is 0 because no combination can make 4.
If amount=5, answer is 1 because only {5} can make 5. If amount=10, answer is 2 because {2,2,2,2,2} and {5,5} can make 10.

Time Complexity: O(amount * len(coins))
Space Complexity: O(amount)
"""

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Initialize dp array where dp[x] represents number of ways to make amount x
        dp = [0] * (amount + 1)
        # Base case: there is 1 way to make amount 0 (using no coins)
        dp[0] = 1

        # For each coin, update the number of ways for all possible amounts
        for coin in coins:
            # For each amount from coin value up to target amount
            for x in range(coin, amount + 1):
                # Add the number of ways we can make amount x-coin
                # This represents using current coin to complete previous combinations
                dp[x] += dp[x - coin]

        return dp[amount]


def run_tests():
    solution = Solution()

    # Test Case 1: Basic case with multiple solutions
    amount1, coins1 = 5, [1, 2, 5]
    print(f"Test Case 1:")
    print(f"Amount: {amount1}, Coins: {coins1}")
    print(f"Result: {solution.change(amount1, coins1)}")  # Expected: 4
    # Ways: {1,1,1,1,1}, {1,1,1,2}, {1,2,2}, {5}

    # Test Case 2: No solution possible
    amount2, coins2 = 3, [2]
    print(f"\nTest Case 2:")
    print(f"Amount: {amount2}, Coins: {coins2}")
    print(f"Result: {solution.change(amount2, coins2)}")  # Expected: 0

    # Test Case 3: Multiple coins with multiple solutions
    amount3, coins3 = 10, [2, 5]
    print(f"\nTest Case 3:")
    print(f"Amount: {amount3}, Coins: {coins3}")
    print(f"Result: {solution.change(amount3, coins3)}")  # Expected: 2
    # Ways: {2,2,2,2,2}, {5,5}

    # Test Case 4: Zero amount
    amount4, coins4 = 0, [1, 2, 3]
    print(f"\nTest Case 4:")
    print(f"Amount: {amount4}, Coins: {coins4}")
    print(f"Result: {solution.change(amount4, coins4)}")  # Expected: 1


if __name__ == "__main__":
    run_tests()
