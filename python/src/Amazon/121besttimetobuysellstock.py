"""
LeetCode 121. Best Time to Buy and Sell Stock

Problem Statement:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a 
different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any 
profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4
"""

from typing import List, Tuple


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        One-pass solution using minimum price tracking.
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not prices:
            return 0

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Update minimum price seen so far
            min_price = min(min_price, price)
            # Update maximum profit if selling at current price
            max_profit = max(max_profit, price - min_price)

        return max_profit

    def maxProfitWithDays(self, prices: List[int]) -> Tuple[int, int, int]:
        """
        Returns (max_profit, buy_day, sell_day).
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not prices:
            return (0, -1, -1)

        min_price = float('inf')
        max_profit = 0
        min_day = sell_day = buy_day = 0

        for day, price in enumerate(prices):
            if price < min_price:
                min_price = price
                min_day = day

            current_profit = price - min_price
            if current_profit > max_profit:
                max_profit = current_profit
                buy_day = min_day
                sell_day = day

        return (max_profit, buy_day, sell_day)

    def maxProfitBruteForce(self, prices: List[int]) -> int:
        """
        Brute force solution (for comparison).
        Time complexity: O(n^2)
        Space complexity: O(1)
        """
        max_profit = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)

        return max_profit


def visualize_prices(prices: List[int], buy_day: int = -1, sell_day: int = -1) -> None:
    """Helper function to visualize stock prices and transactions"""
    if not prices:
        print("Empty price list")
        return

    # Find the maximum price for scaling
    max_price = max(prices)
    height = min(20, max_price)  # Limit height for very large numbers
    scale = height / max_price if max_price > 0 else 1

    # Create the price chart
    for h in range(height, -1, -1):
        line = ""
        price_at_height = h / scale
        for day, price in enumerate(prices):
            if h == 0:
                line += "─"  # Bottom line
            elif day == buy_day and price * scale >= h:
                line += "B"  # Buy point
            elif day == sell_day and price * scale >= h:
                line += "S"  # Sell point
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
            "expected": 5,
            "description": "Standard case with profit"
        },
        {
            "prices": [7, 6, 4, 3, 1],
            "expected": 0,
            "description": "Decreasing prices"
        },
        {
            "prices": [1],
            "expected": 0,
            "description": "Single price"
        },
        {
            "prices": [3, 3, 3, 3],
            "expected": 0,
            "description": "Constant prices"
        },
        {
            "prices": [1, 2, 4, 8, 16],
            "expected": 15,
            "description": "Strictly increasing prices"
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
        result2 = solution.maxProfitBruteForce(prices)
        profit, buy_day, sell_day = solution.maxProfitWithDays(prices)

        print("\nPrice visualization:")
        visualize_prices(prices, buy_day, sell_day)

        if profit > 0:
            print(f"Buy on day {buy_day} (price = {prices[buy_day]})")
            print(f"Sell on day {sell_day} (price = {prices[sell_day]})")
            print(f"Profit: {profit}")
        else:
            print("No profitable transaction possible")

        assert result1 == expected and result2 == expected and profit == expected, \
            f"Expected {expected}, but got {result1} (optimal), " \
            f"{result2} (brute force), {profit} (with days)"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_max_profit()
    print("\nAll test cases passed! 🎉")
