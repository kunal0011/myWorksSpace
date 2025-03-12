"""
LeetCode 414 - Third Maximum Number

Problem Statement:
-----------------
Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.

Key Points:
----------
1. The solution should return the third DISTINCT maximum (duplicates don't count)
2. If there are fewer than 3 distinct numbers, return the maximum number
3. The time complexity should be O(n) and space complexity O(1)

Examples:
--------
Input: nums = [3,2,1]
Output: 1
Explanation: First maximum = 3, second maximum = 2, third maximum = 1.

Input: nums = [1,2]
Output: 2
Explanation: The third maximum does not exist, so return maximum (2).

Input: nums = [2,2,3,1]
Output: 1
Explanation: First maximum = 3, second maximum = 2, third maximum = 1.

Constraints:
-----------
* 1 <= nums.length <= 10^4
* -2^31 <= nums[i] <= 2^31 - 1
"""

from typing import List
import math

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        Returns the third maximum number in the array.
        If third maximum doesn't exist, returns the maximum number.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Initialize three variables to track top 3 maximums
        first = second = third = float('-inf')
        
        for num in nums:
            # Skip duplicates
            if num in [first, second, third]:
                continue
                
            # Update the three maximums accordingly
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
        
        # If third maximum exists (not -inf), return it
        # Otherwise return the first maximum
        return third if third != float('-inf') else first

def test_third_maximum():
    """
    Test driver for the third maximum number problem
    """
    test_cases = [
        ([3, 2, 1], 1),  # Basic case with three numbers
        ([1, 2], 2),  # Case with less than three distinct numbers
        ([2, 2, 3, 1], 1),  # Case with duplicates
        ([5, 2, 2], 5),  # Case with duplicates and less than three distinct numbers
        ([1, 1, 2], 2),  # Case with duplicates at the beginning
        ([1, 2, -2147483648], -2147483648),  # Case with minimum integer value
        ([1, 2, 2, 5, 3, 5], 1),  # Case with multiple duplicates
    ]
    
    solution = Solution()
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.thirdMax(nums)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test case {i}: {status}")
        print(f"Input: {nums}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print("-" * 40)

if __name__ == "__main__":
    test_third_maximum()
