"""
LeetCode 413 - Arithmetic Slices

Problem Statement:
-----------------
Given an integer array nums, return the number of arithmetic subarrays of nums.

A sequence of numbers is called arithmetic if it consists of at least three elements and if 
the difference between any two consecutive elements is the same.

For example:
* [1,3,5,7,9] is arithmetic because the difference between each consecutive pair is 2
* [7,7,7,7] is arithmetic because the difference between each consecutive pair is 0
* [3,-1,-5,-9] is arithmetic because the difference between each consecutive pair is -4

A subarray is a contiguous subsequence of the array.

Key Points:
----------
1. The array must have at least 3 elements to form an arithmetic slice
2. All pairs of consecutive elements must have the same difference
3. The sequence must be contiguous (subarray)
4. An arithmetic sequence of length n contains (n-2) different arithmetic slices

Examples:
--------
Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums:
[1,2,3], [2,3,4] and [1,2,3,4] itself.

Input: nums = [1]
Output: 0
Explanation: Array has less than 3 elements.

Constraints:
-----------
* 1 <= nums.length <= 5000
* -1000 <= nums[i] <= 1000

Time Complexity: O(n) where n is the length of the input array
Space Complexity: O(1) as we only use constant extra space
"""

from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        Returns the number of arithmetic slices in the array.
        An arithmetic slice is a subarray with at least 3 elements where all pairs of consecutive elements have the same difference.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if len(nums) < 3:
            return 0
            
        count = 0  # Total count of arithmetic slices
        current = 0  # Current consecutive arithmetic slice length
        
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                current += 1  # Extend current arithmetic slice
                count += current  # Add number of new slices formed
            else:
                current = 0  # Reset when sequence breaks
                
        return count

def test_arithmetic_slices():
    """
    Test driver for the arithmetic slices problem
    """
    # Test cases
    test_cases = [
        ([1, 2, 3, 4], 3),  # Basic case with one arithmetic sequence
        ([1], 0),  # Array with single element
        ([1, 2, 3, 4, 5], 6),  # Longer arithmetic sequence
        ([1, 2, 4, 6, 8], 2),  # Multiple arithmetic slices
        ([7, 7, 7, 7], 3),  # Constant sequence
        ([3, 1, 2, 4, 6, 8], 2),  # Non-consecutive arithmetic slices
    ]
    
    solution = Solution()
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.numberOfArithmeticSlices(nums)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test case {i}: {status}")
        print(f"Input: {nums}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print("-" * 40)

if __name__ == "__main__":
    test_arithmetic_slices()