"""
LeetCode 322 - Coin Change

Problem Statement:
You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money. Return the fewest number 
of coins that you need to make up that amount. If that amount of money cannot be 
made up by any combination of the coins, return -1.

Logic:
1. Use Dynamic Programming bottom-up approach:
   - dp[i] represents minimum coins needed for amount i
   - Initialize dp array with amount + 1 (impossible value)
2. For each amount from 1 to target:
   - Try each coin denomination
   - Update dp[i] = min(dp[i], dp[i-coin] + 1)
3. Time: O(amount * len(coins)), Space: O(amount)
"""

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp array with amount + 1 (impossible value)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        # For each amount, try each coin
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] <= amount else -1

def test_coin_change():
    solution = Solution()
    
    # Test cases
    test_cases = [
        ({
            'coins': [1,2,5],
            'amount': 11,
            'expected': 3
        }, "3 coins (5 + 5 + 1)"),
        ({
            'coins': [2],
            'amount': 3,
            'expected': -1
        }, "Cannot make amount 3 with only coin 2"),
        ({
            'coins': [1],
            'amount': 0,
            'expected': 0
        }, "Zero amount needs zero coins"),
        ({
            'coins': [186,419,83,408],
            'amount': 6249,
            'expected': 20
        }, "Complex case with larger values")
    ]
    
    for i, (test_case, explanation) in enumerate(test_cases):
        result = solution.coinChange(test_case['coins'], test_case['amount'])
        assert result == test_case['expected'], \
            f"Test case {i + 1} failed: expected {test_case['expected']}, got {result}"
        print(f"Test case {i + 1} passed:")
        print(f"Coins: {test_case['coins']}")
        print(f"Amount: {test_case['amount']}")
        print(f"Result: {result}")
        print(f"Explanation: {explanation}\n")

if __name__ == "__main__":
    test_coin_change()
    print("All test cases passed!")
