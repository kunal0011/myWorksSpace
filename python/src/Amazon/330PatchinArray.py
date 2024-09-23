from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        i = 0
        current_range = 1  # The smallest number we cannot cover

        while current_range <= n:
            # If nums[i] is within the current range, extend the range
            if i < len(nums) and nums[i] <= current_range:
                current_range += nums[i]
                i += 1
            # Otherwise, we need to patch the array with current_range
            else:
                current_range += current_range
                patches += 1

        return patches
