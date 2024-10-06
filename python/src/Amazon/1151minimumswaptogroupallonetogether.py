from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # Step 1: Calculate the total number of 1's
        total_ones = sum(data)

        if total_ones == 0:  # If there are no 1's, no swaps are needed
            return 0

        # Step 2: Initialize the sliding window
        max_ones_in_window = 0
        current_ones_in_window = 0
        window_size = total_ones

        # Step 3: Sliding window to find the maximum number of 1's in any window of size total_ones
        for i in range(len(data)):
            current_ones_in_window += data[i]

            if i >= window_size:
                current_ones_in_window -= data[i - window_size]

            max_ones_in_window = max(
                max_ones_in_window, current_ones_in_window)

        # Step 4: Calculate the minimum number of swaps
        return total_ones - max_ones_in_window
