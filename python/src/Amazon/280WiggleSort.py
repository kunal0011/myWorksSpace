"""
LeetCode 280 - Wiggle Sort

Problem Statement:
Given an unsorted array nums, reorder it in-place such that:
nums[0] <= nums[1] >= nums[2] <= nums[3]....
In other words, each element at an even-indexed position should be less than or equal to
its adjacent elements, and each element at an odd-indexed position should be greater than
or equal to its adjacent elements.

Logic:
1. Iterate through array indices 0 to n-2
2. For even indices i:
   - If nums[i] > nums[i+1], swap them
3. For odd indices i:
   - If nums[i] < nums[i+1], swap them
4. No need for sorting, just local comparisons and swaps
"""

from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        for i in range(len(nums) - 1):
            if (i % 2 == 0 and nums[i] > nums[i + 1]) or (i % 2 == 1 and nums[i] < nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]


def test_wiggle_sort():
    solution = Solution()
    
    # Test cases
    test_cases = [
        [3, 5, 2, 1, 6, 4],           # General case
        [1],                          # Single element
        [1, 2],                      # Two elements
        [1, 1, 1, 1],               # All same elements
        [6, 5, 4, 3, 2, 1],         # Descending order
        [1, 2, 3, 4, 5, 6]          # Ascending order
    ]
    
    def verify_wiggle(nums):
        for i in range(len(nums) - 1):
            if i % 2 == 0:
                if nums[i] > nums[i + 1]:
                    return False
            else:
                if nums[i] < nums[i + 1]:
                    return False
        return True
    
    for i, nums in enumerate(test_cases):
        original = nums.copy()
        solution.wiggleSort(nums)
        assert verify_wiggle(nums), f"Test case {i + 1} failed: input={original}, output={nums}"
        print(f"Test case {i + 1} passed: input={original}, output={nums}")

if __name__ == "__main__":
    test_wiggle_sort()
    print("All test cases passed!")
