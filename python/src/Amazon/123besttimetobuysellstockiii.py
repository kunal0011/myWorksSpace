"""
LeetCode 123. Best Time to Buy and Sell Stock III

Problem Statement:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the
stock before you buy again).

Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: 
Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: 
Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging
multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^5
"""

from typing import List, Tuple


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        One-pass Dynamic Programming solution.
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not prices:
            return 0

        # Initialize states
        # buy1: maximum profit after first buy
        # sell1: maximum profit after first sell
        # buy2: maximum profit after second buy
        # sell2: maximum profit after second sell
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0

        for price in prices:
            # We can buy first stock with our initial money (0 - price)
            buy1 = max(buy1, -price)
            # We can sell first stock after buying (buy1 + price)
            sell1 = max(sell1, buy1 + price)
            # We can buy second stock after first sell (sell1 - price)
            buy2 = max(buy2, sell1 - price)
            # We can sell second stock after second buy (buy2 + price)
            sell2 = max(sell2, buy2 + price)

        return sell2

    def maxProfitWithTransactions(self, prices: List[int]) -> Tuple[int, List[Tuple[int, int]]]:
        """
        Dynamic Programming solution that tracks transactions.
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if not prices:
            return 0, []

        n = len(prices)

        # First pass: calculate maximum profit from left to right
        left_profits = [0] * n
        min_price = float('inf')
        max_profit = 0

        for i in range(n):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
            left_profits[i] = max_profit

        # Second pass: calculate maximum profit from right to left
        # and find the optimal split point
        max_price = float('-inf')
        max_profit = 0
        total_max = 0
        split_point = 0

        for i in range(n-1, -1, -1):
            max_price = max(max_price, prices[i])
            max_profit = max(max_profit, max_price - prices[i])
            current_total = max_profit + (left_profits[i-1] if i > 0 else 0)
            if current_total > total_max:
                total_max = current_total
                split_point = i

        # Find the actual transactions
        transactions = []

        # Find first transaction (before split point)
        if split_point > 0:
            min_price = prices[0]
            min_day = 0
            max_profit = 0
            sell_day = 0

            for i in range(split_point):
                if prices[i] < min_price:
                    min_price = prices[i]
                    min_day = i
                current_profit = prices[i] - min_price
                if current_profit > max_profit:
                    max_profit = current_profit
                    sell_day = i

            if max_profit > 0:
                transactions.append((min_day, sell_day))

        # Find second transaction (after split point)
        if split_point < n:
            min_price = prices[split_point]
            min_day = split_point
            max_profit = 0
            sell_day = split_point

            for i in range(split_point, n):
                if prices[i] < min_price:
                    min_price = prices[i]
                    min_day = i
                current_profit = prices[i] - min_price
                if current_profit > max_profit:
                    max_profit = current_profit
                    sell_day = i

            if max_profit > 0:
                transactions.append((min_day, sell_day))

        return total_max, transactions


def visualize_prices_with_transactions(prices: List[int],
                                       transactions: List[Tuple[int, int]]) -> None:
    """Helper function to visualize stock prices and transactions"""
    if not prices:
        print("Empty price list")
        return

    # Find the maximum price for scaling
    max_price = max(prices)
    height = min(20, max_price)  # Limit height for very large numbers
    scale = height / max_price if max_price > 0 else 1

    # Create transaction markers
    markers = {}
    for i, (buy_day, sell_day) in enumerate(transactions):
        markers[buy_day] = f'B{i+1}'
        markers[sell_day] = f'S{i+1}'

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
            "prices": [3, 3, 5, 0, 0, 3, 1, 4],
            "expected": 6,
            "description": "Standard case with two transactions"
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
            "prices": [1, 2, 4, 2, 5, 7, 2, 4, 9, 0],
            "expected": 13,
            "description": "Complex case"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        prices = test_case["prices"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"Prices: {prices}")

        # Test both implementations
        result1 = solution.maxProfit(prices)
        profit, transactions = solution.maxProfitWithTransactions(prices)

        print("\nPrice visualization with transactions:")
        visualize_prices_with_transactions(prices, transactions)

        if transactions:
            print("Transactions:")
            total = 0
            for j, (buy_day, sell_day) in enumerate(transactions, 1):
                profit_trade = prices[sell_day] - prices[buy_day]
                total += profit_trade
                print(f"Transaction {j}: Buy on day {buy_day} (price = {prices[buy_day]}) "
                      f"and sell on day {sell_day} (price = {prices[sell_day]}), "
                      f"profit = {profit_trade}")
            print(f"Total profit: {total}")
        else:
            print("No profitable transactions possible")

        assert result1 == expected and profit == expected, \
            f"Expected {expected}, but got {result1} (DP), {profit} (with transactions)"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_max_profit()
    print("\nAll test cases passed! 🎉")
