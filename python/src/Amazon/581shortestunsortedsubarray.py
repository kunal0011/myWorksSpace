"""
LeetCode 581 - Shortest Unsorted Continuous Subarray

Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray 
in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

Example 1:
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6,4,8,10,9] in ascending order to make the whole array sorted in ascending order.

Example 2:
Input: nums = [1,2,3,4]
Output: 0
Explanation: The array is already sorted.

Example 3:
Input: nums = [1]
Output: 0
Explanation: The array is already sorted.

Constraints:
- 1 <= nums.length <= 10^4
- -10^5 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        Optimized one-pass solution without sorting
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(nums)
        if n < 2:
            return 0
            
        # Find the first number out of order from start
        start = 0
        while start < n - 1 and nums[start] <= nums[start + 1]:
            start += 1
            
        # Array is sorted
        if start == n - 1:
            return 0
            
        # Find the first number out of order from end
        end = n - 1
        while end > 0 and nums[end] >= nums[end - 1]:
            end -= 1
            
        # Find min and max in the window
        window_min = float('inf')
        window_max = float('-inf')
        for i in range(start, end + 1):
            window_min = min(window_min, nums[i])
            window_max = max(window_max, nums[i])
            
        # Extend the window if needed
        while start > 0 and nums[start - 1] > window_min:
            start -= 1
        while end < n - 1 and nums[end + 1] < window_max:
            end += 1
            
        return end - start + 1
    
    def findUnsortedSubarray_sorting(self, nums: List[int]) -> int:
        """
        Alternative solution using sorting
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        if len(nums) < 2:
            return 0
            
        sorted_nums = sorted(nums)
        start = len(nums)
        end = 0
        
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                start = min(start, i)
                end = max(end, i)
                
        return end - start + 1 if end >= start else 0


def test_find_unsorted_subarray():
    """
    Test function with comprehensive test cases
    """
    solution = Solution()
    
    test_cases = [
        # Basic test cases
        ([2,6,4,8,10,9,15], 5),  # Example 1
        ([1,2,3,4], 0),          # Example 2
        ([1], 0),                # Example 3
        
        # Edge cases
        ([1,1], 0),              # Equal elements
        ([2,1], 2),              # Completely unsorted
        ([1,2,3,3,3], 0),        # Multiple equal elements
        
        # Complex test cases
        ([1,3,2,2,2], 4),        # Multiple equal elements in unsorted part
        ([2,3,3,2,4], 4),        # Unsorted with duplicates
        ([1,3,5,4,2], 5),        # Completely unsorted
        ([1,2,4,5,3], 3),        # One element out of place
        
        # Test cases with negative numbers
        ([-1,1,-2,2], 4),
        ([1,-1,2,-2], 4),
        
        # Larger test cases
        ([1,3,2,4,5,6,7,8,9], 2),
        ([1,2,3,5,4,6,7,8,9], 2),
        
        # Special patterns
        ([1,2,3,4,5,4,6,7,8], 3),  # Local dip
        ([1,5,3,4,2,6,7], 5),      # Mountain pattern
        
        # Already sorted with duplicates
        ([1,1,1,2,2,3], 0),
        ([1,2,2,2,3,3], 0)
    ]
    
    print("Running tests for Shortest Unsorted Continuous Subarray...\n")
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        # Test both implementations
        result1 = solution.findUnsortedSubarray(nums)
        result2 = solution.findUnsortedSubarray_sorting(nums)
        
        print(f"Test Case {i}:")
        print(f"Input: nums = {nums}")
        print(f"Expected: {expected}")
        print(f"Optimized Solution: {result1} {'✅' if result1 == expected else '❌'}")
        print(f"Sorting Solution: {result2} {'✅' if result2 == expected else '❌'}")
        
        if result1 != expected or result2 != expected:
            print("❌ Test case failed!")
            print(f"Got: {result1} (Optimized), {result2} (Sorting)")
            print(f"Expected: {expected}")
        else:
            print("✅ Test case passed!")
        print()


if __name__ == "__main__":
    test_find_unsorted_subarray()