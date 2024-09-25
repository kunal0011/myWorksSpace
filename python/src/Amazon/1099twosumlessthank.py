from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # Sort the array
        nums.sort()

        # Initialize two pointers
        left, right = 0, len(nums) - 1
        max_sum = -1

        # Two-pointer technique
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum < k:
                # If the sum is valid, update max_sum and move left pointer
                max_sum = max(max_sum, current_sum)
                left += 1
            else:
                # If the sum is too large, move the right pointer
                right -= 1

        return max_sum
