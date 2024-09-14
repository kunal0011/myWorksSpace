from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        prefix_sum = 0
        min_diff = float('inf')
        result_idx = -1

        for i in range(n):
            # Update prefix sum
            prefix_sum += nums[i]

            # Calculate the average of the first i + 1 elements
            left_avg = prefix_sum // (i + 1)

            # Calculate the average of the last n - i - 1 elements
            if i != n - 1:
                right_avg = (total_sum - prefix_sum) // (n - i - 1)
            else:
                right_avg = 0  # No elements on the right for the last element

            # Calculate the absolute difference
            diff = abs(left_avg - right_avg)

            # Update the result if we found a smaller difference
            if diff < min_diff:
                min_diff = diff
                result_idx = i

        return result_idx
