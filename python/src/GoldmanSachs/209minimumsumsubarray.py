from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = float('inf')  # Initialize minimum length to infinity
        current_sum = 0
        left = 0  # Left pointer of the sliding window

        for right in range(n):
            # Expand the window by including nums[right]
            current_sum += nums[right]

            # Contract the window until the sum is less than target
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0
