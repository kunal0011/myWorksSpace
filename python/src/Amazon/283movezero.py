"""
LeetCode 283 - Move Zeroes

Problem Statement:
Given an integer array nums, move all 0's to the end of it while maintaining 
the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Logic:
1. Use two-pointer technique:
   - last_non_zero_found_at: points to where next non-zero should go
   - i: iterates through the array
2. When finding non-zero element:
   - Swap with element at last_non_zero_found_at
   - Increment last_non_zero_found_at
3. This maintains relative order and moves zeros to end
"""

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

def test_move_zeroes():
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([0,1,0,3,12], [1,3,12,0,0]),    # Standard case
        ([0], [0]),                       # Single zero
        ([1], [1]),                       # Single non-zero
        ([0,0,0], [0,0,0]),              # All zeros
        ([1,2,3], [1,2,3]),              # No zeros
        ([0,0,1,0,2], [1,2,0,0,0])       # Multiple zeros scattered
    ]
    
    for i, (nums, expected) in enumerate(test_cases):
        nums_copy = nums.copy()
        solution.moveZeroes(nums)
        assert nums == expected, f"Test case {i + 1} failed: input={nums_copy}, expected={expected}, got={nums}"
        print(f"Test case {i + 1} passed: input={nums_copy}, output={nums}")

if __name__ == "__main__":
    test_move_zeroes()
    print("All test cases passed!")
