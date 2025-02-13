"""
LeetCode 122. Best Time to Buy and Sell Stock II

Problem Statement:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one
share of the stock at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation:
Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation:
Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: No profit can be made.

Constraints:
- 1 <= prices.length <= 3 * 10^4
- 0 <= prices[i] <= 10^4
"""

from typing import List, Tuple


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Peak Valley approach - One pass solution.
        Time complexity: O(n)
        Space complexity: O(1)
        """
        total_profit = 0

        # Add up all positive price differences
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                total_profit += prices[i] - prices[i-1]

        return total_profit

    def maxProfitWithTransactions(self, prices: List[int]) -> Tuple[int, List[Tuple[int, int]]]:
        """
        Returns total profit and list of (buy_day, sell_day) transactions.
        Time complexity: O(n)
        Space complexity: O(n)
        """
        total_profit = 0
        transactions = []
        buy_day = -1

        for i in range(len(prices) - 1):
            # Found a valley (potential buy point)
            if buy_day == -1 and prices[i] < prices[i + 1]:
                buy_day = i
            # Found a peak (potential sell point)
            elif buy_day != -1 and prices[i] > prices[i + 1]:
                total_profit += prices[i] - prices[buy_day]
                transactions.append((buy_day, i))
                buy_day = -1

        # Handle last day
        if buy_day != -1 and prices[-1] > prices[buy_day]:
            total_profit += prices[-1] - prices[buy_day]
            transactions.append((buy_day, len(prices) - 1))

        return total_profit, transactions

    def maxProfitDP(self, prices: List[int]) -> int:
        """
        Dynamic Programming approach.
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not prices:
            return 0

        # dp[i][0] represents max profit if not holding stock on day i
        # dp[i][1] represents max profit if holding stock on day i
        not_holding = 0
        holding = -prices[0]

        for i in range(1, len(prices)):
            # Update max profit for not holding stock
            not_holding = max(not_holding, holding + prices[i])
            # Update max profit for holding stock
            holding = max(holding, not_holding - prices[i])

        return not_holding


def visualize_prices_with_transactions(prices: List[int],
                                       transactions: List[Tuple[int, int]]) -> None:
    """Helper function to visualize stock prices and multiple transactions"""
    if not prices:
        print("Empty price list")
        return

    # Find the maximum price for scaling
    max_price = max(prices)
    height = min(20, max_price)  # Limit height for very large numbers
    scale = height / max_price if max_price > 0 else 1

    # Create transaction markers
    markers = {}
    for buy_day, sell_day in transactions:
        markers[buy_day] = 'B'
        markers[sell_day] = 'S'

    # Create the price chart
    for h in range(height, -1, -1):
        line = ""
        price_at_height = h / scale
        for day, price in enumerate(prices):
            if h == 0:
                line += "─"  # Bottom line
            elif day in markers and price * scale >= h:
                line += markers[day]  # Transaction point
            elif price * scale >= h:
                line += "│"  # Price line
            else:
                line += " "
        print(f"{price_at_height:4.0f} {line}")

    # Print day numbers
    print("    ", end="")
    for i in range(len(prices)):
        print(i % 10, end="")
    print("\n")


def test_max_profit():
    solution = Solution()

    test_cases = [
        {
            "prices": [7, 1, 5, 3, 6, 4],
            "expected": 7,
            "description": "Multiple transactions"
        },
        {
            "prices": [1, 2, 3, 4, 5],
            "expected": 4,
            "description": "Strictly increasing"
        },
        {
            "prices": [7, 6, 4, 3, 1],
            "expected": 0,
            "description": "Strictly decreasing"
        },
        {
            "prices": [1],
            "expected": 0,
            "description": "Single day"
        },
        {
            "prices": [2, 2, 2, 2],
            "expected": 0,
            "description": "Constant prices"
        },
        {
            "prices": [1, 2, 1, 2, 1, 2],
            "expected": 3,
            "description": "Alternating prices"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        prices = test_case["prices"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"Prices: {prices}")

        # Test all implementations
        result1 = solution.maxProfit(prices)
        result2 = solution.maxProfitDP(prices)
        profit, transactions = solution.maxProfitWithTransactions(prices)

        print("\nPrice visualization with transactions:")
        visualize_prices_with_transactions(prices, transactions)

        if transactions:
            print("Transactions:")
            total = 0
            for buy_day, sell_day in transactions:
                profit_trade = prices[sell_day] - prices[buy_day]
                total += profit_trade
                print(f"Buy on day {buy_day} (price = {prices[buy_day]}) and "
                      f"sell on day {sell_day} (price = {prices[sell_day]}), "
                      f"profit = {profit_trade}")
            print(f"Total profit: {total}")
        else:
            print("No profitable transactions possible")

        assert result1 == expected and result2 == expected and profit == expected, \
            f"Expected {expected}, but got {result1} (peak valley), " \
            f"{result2} (DP), {profit} (with transactions)"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_max_profit()
    print("\nAll test cases passed! 🎉")
