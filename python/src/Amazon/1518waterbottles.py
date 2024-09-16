class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drinks = numBottles
        empty_bottles = numBottles

        while empty_bottles >= numExchange:
            # How many new full bottles can we get from empty ones
            new_bottles = empty_bottles // numExchange
            total_drinks += new_bottles

            # Update the number of empty bottles
            empty_bottles = new_bottles + (empty_bottles % numExchange)

        return total_drinks


# Testing
solution = Solution()
numBottles = 9
numExchange = 3
print("Python Test Result:", solution.numWaterBottles(
    numBottles, numExchange))  # Output should be 13
