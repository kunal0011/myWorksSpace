from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        result = prices[:]

        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                j = stack.pop()
                result[j] = prices[j] - price
            stack.append(i)

        return result


# Testing
solution = Solution()
prices = [8, 4, 6, 2, 3]
print("Python Test Result:", solution.finalPrices(
    prices))  # Output should be [4, 2, 4, 2, 3]
