from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # Variable to track the length of the current smooth descent period
        descent_length = 1

        # Initialize the count of descent periods
        total_periods = 0

        # Iterate through the prices array
        for i in range(1, len(prices)):
            if prices[i-1] - prices[i] == 1:
                # If current price is exactly 1 less than the previous price, extend the descent
                descent_length += 1
            else:
                # Add the total periods for the current descent period
                total_periods += (descent_length * (descent_length + 1)) // 2
                # Reset the descent length
                descent_length = 1

        # Add the periods for the last descent period
        total_periods += (descent_length * (descent_length + 1)) // 2

        return total_periods
