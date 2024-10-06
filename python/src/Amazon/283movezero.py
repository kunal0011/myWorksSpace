from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointer to track where the next non-zero element should go
        last_non_zero_found_at = 0

        # Move all the non-zero elements to the beginning of the array
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap current element with the element at last_non_zero_found_at
                nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]
                last_non_zero_found_at += 1
