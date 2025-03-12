"""
LeetCode 540 - Single Element in a Sorted Array

You are given a sorted array nums consisting of n elements where all elements appear exactly twice, 
except for one element which appears exactly once. Find this single element that appears only once.

You must implement a solution with O(log n) runtime complexity and O(1) space complexity.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10
"""

from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Edge cases
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            # Check if mid is the single element
            if (mid > 0 and mid < len(nums) - 1 and 
                nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]):
                return nums[mid]
            
            # If mid is even, it should match with next element
            # If mid is odd, it should match with previous element
            # If this pattern is violated, single element is on the left side
            if mid % 2 == 0:
                if mid + 1 < len(nums) and nums[mid] == nums[mid + 1]:
                    left = mid + 2
                else:
                    right = mid - 1
            else:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                else:
                    right = mid - 1

        return nums[left]


def test_single_non_duplicate():
    """
    Test function with comprehensive test cases and detailed error reporting
    """
    solution = Solution()
    
    test_cases = [
        # Regular cases
        ([1, 1, 2, 2, 3, 3, 4, 4, 5], 5),
        ([1, 1, 2, 3, 3, 4, 4, 5, 5], 2),
        ([1, 2, 2, 3, 3, 4, 4, 5, 5], 1),
        ([3, 3, 7, 7, 10, 11, 11], 10),
        ([1, 1, 2], 2),
        
        # Edge cases
        ([1], 1),  # Single element array
        ([1, 1, 2, 2, 3], 3),  # Single element at end
        ([1, 2, 2, 3, 3], 1),  # Single element at start
        ([1, 1, 2, 2, 3, 3, 4], 4),  # Odd length array
    ]
    
    passed = 0
    total = len(test_cases)
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        try:
            result = solution.singleNonDuplicate(nums)
            assert result == expected, f"Got {result}, but expected {expected}"
            passed += 1
            print(f"✓ Test case {i} passed: nums={nums}, expected={expected}")
        except AssertionError as e:
            print(f"✗ Test case {i} failed: {e}")
            print(f"  Input array: {nums}")
            
    print(f"\nTest Results: {passed}/{total} test cases passed")
    if passed == total:
        print("All test cases passed successfully!")
    else:
        print(f"Failed {total - passed} test case(s)")


if __name__ == "__main__":
    test_single_non_duplicate()
