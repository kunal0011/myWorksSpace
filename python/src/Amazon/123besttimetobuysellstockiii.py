from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # Initialize variables to track profits
        first_buy = float('-inf')   # Profit after first buy
        first_sell = 0              # Profit after first sell
        second_buy = float('-inf')  # Profit after second buy
        second_sell = 0             # Profit after second sell

        for price in prices:
            # Maximize first_buy (minimizing the cost of the first stock purchase)
            first_buy = max(first_buy, -price)

            # Maximize first_sell (selling after the first buy)
            first_sell = max(first_sell, first_buy + price)

            # Maximize second_buy (buying after the first sell)
            second_buy = max(second_buy, first_sell - price)

            # Maximize second_sell (selling after the second buy)
            second_sell = max(second_sell, second_buy + price)

        return second_sell
