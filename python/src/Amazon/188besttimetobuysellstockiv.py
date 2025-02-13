"""
LeetCode 188. Best Time to Buy and Sell Stock IV

Problem Statement:
You are given an integer k and an array prices where prices[i] is the price of a given stock on the iᵗʰ day.
Find the maximum profit you can achieve. You may complete at most k transactions.

Note:
- A transaction is a buy and a sell.
- You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Total profit is 4 + 3 = 7.

Constraints:
- 0 <= k <= 100
- 0 <= prices.length <= 1000
- 0 <= prices[i] <= 1000
"""

from typing import List, Tuple, Dict
import math


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        Calculate maximum profit with at most k transactions.
        Time Complexity: O(n*k) in the worst-case scenario.
        Space Complexity: O(n*k)
        """
        n = len(prices)
        if n == 0:
            return 0

        # If k is large enough, it's equivalent to unlimited transactions.
        if k >= n // 2:
            total_profit = 0
            for i in range(1, n):
                profit = prices[i] - prices[i-1]
                total_profit += profit if profit > 0 else 0
            return total_profit

        # Initialize DP table:
        # dp[t][i] represents the maximum profit using at most t transactions until day i.
        dp = [[0]*n for _ in range(k+1)]

        # Fill dp table
        for t in range(1, k+1):
            # This holds the maximum value of dp[t-1][i] - prices[i] seen so far.
            max_diff = -prices[0]
            for i in range(1, n):
                # Either we do nothing on day i, or we sell stock on day i.
                dp[t][i] = max(dp[t][i-1], prices[i] + max_diff)
                # Update max_diff with the profit if we buy on day i.
                max_diff = max(max_diff, dp[t-1][i] - prices[i])
        return dp[k][n-1]

    def maxProfitWithSteps(self, k: int, prices: List[int]) -> Tuple[int, List[Dict]]:
        """
        Calculate maximum profit with step tracking.
        Returns:
            A tuple containing the maximum profit and a list of step-by-step details.
        Time Complexity: O(n*k)
        Space Complexity: O(n*k) for the DP table and steps.
        """
        steps = []
        n = len(prices)
        if n == 0:
            steps.append({
                "action": "Empty prices list",
                "result": 0
            })
            return 0, steps

        # Unlimited transaction case
        if k >= n // 2:
            total_profit = 0
            transaction_details = []
            for i in range(1, n):
                profit = prices[i] - prices[i-1]
                if profit > 0:
                    total_profit += profit
                    transaction_details.append({
                        "buy_day": i,
                        "sell_day": i+1,
                        "buy_price": prices[i-1],
                        "sell_price": prices[i],
                        "profit": profit
                    })
            steps.append({
                "action": "Unlimited transactions",
                "total_profit": total_profit,
                "transactions": transaction_details
            })
            return total_profit, steps

        # Initialize DP table: (k+1) by n
        dp = [[0]*n for _ in range(k+1)]
        steps.append({
            "action": "Initialize DP table",
            "dimensions": (k+1, n),
            "dp_initial": dp
        })

        # Fill DP table with transaction iterations.
        for t in range(1, k+1):
            max_diff = -prices[0]
            # To track details for transaction number t.
            transaction_steps = []
            for i in range(1, n):
                prev_profit = dp[t][i-1]
                candidate_profit = prices[i] + max_diff
                dp[t][i] = max(prev_profit, candidate_profit)
                transaction_steps.append({
                    "transaction": t,
                    "day": i,
                    "price": prices[i],
                    "dp_previous": prev_profit,
                    "max_diff": max_diff,
                    "candidate_profit": candidate_profit,
                    "dp_current": dp[t][i]
                })
                # Update max_diff for future days.
                max_diff = max(max_diff, dp[t-1][i] - prices[i])
            steps.append({
                "action": f"Processed transaction {t}",
                "transaction_steps": transaction_steps,
                "final_max_diff": max_diff,
                "dp_row": dp[t]
            })

        final_profit = dp[k][n-1]
        steps.append({
            "action": "Final result",
            "final_profit": final_profit,
            "full_dp_table": dp
        })
        return final_profit, steps


def test_max_profit():
    """
    Test function with various test cases for Best Time to Buy and Sell Stock IV.
    """
    test_cases = [
        {
            "k": 2,
            "prices": [2, 4, 1],
            "expected": 2,
            "description": "Simple case with one profitable transaction"
        },
        {
            "k": 2,
            "prices": [3, 2, 6, 5, 0, 3],
            "expected": 7,
            "description": "Optimal use of two transactions"
        },
        {
            "k": 1,
            "prices": [1, 2],
            "expected": 1,
            "description": "Single transaction profit"
        },
        {
            "k": 100,  # Large k triggers the unlimited transaction case.
            "prices": [1, 2, 3, 4, 5],
            "expected": 4,
            "description": "Unlimited transactions case (k >= n/2)"
        },
    ]

    solution = Solution()

    for idx, tc in enumerate(test_cases, 1):
        k = tc["k"]
        prices = tc["prices"]
        expected = tc["expected"]
        print(f"\n{'='*80}")
        print(f"Test Case {idx}: {tc['description']}")
        print(f"k = {k}, prices = {prices}")

        result_basic = solution.maxProfit(k, prices)
        result_steps, steps = solution.maxProfitWithSteps(k, prices)

        print(f"Output (basic): {result_basic}")
        print(f"Output (with steps): {result_steps}")

        # Uncomment the next line to visualize detailed steps (can be verbose)
        # from pprint import pprint; pprint(steps)

        assert result_basic == expected, f"Basic approach failed: expected {expected}, got {result_basic}"
        assert result_steps == expected, f"Step tracking approach failed: expected {expected}, got {result_steps}"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_max_profit()
