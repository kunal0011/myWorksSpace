from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Update the minimum price seen so far
            if price < min_price:
                min_price = price

            # Calculate the current profit
            profit = price - min_price

            # Update the maximum profit seen so far
            if profit > max_profit:
                max_profit = profit

        return max_profit


# Example usage:
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
print(Solution().maxProfit([7, 6, 4, 3, 1]))  # Output: 0
