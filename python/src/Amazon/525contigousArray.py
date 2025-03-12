"""
LeetCode 525 - Contiguous Array

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0,1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0,1] (or [1,0]) is a longest contiguous subarray with equal number of 0 and 1.

Key Concepts:
1. Use a count variable that increments for 1 and decrements for 0
2. Use a hash map to store the first occurrence of each count
3. When we see a count again, we've found a subarray with equal 0s and 1s
"""

from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Edge case
        if not nums or len(nums) < 2:
            return 0
            
        # Initialize variables
        count = 0
        max_length = 0
        count_map = {0: -1}  # Initialize with 0 count at index -1
        
        # Iterate through array
        for i, num in enumerate(nums):
            # Increment count for 1, decrement for 0
            count += 1 if num == 1 else -1
            
            # If count exists in map, we found a valid subarray
            if count in count_map:
                max_length = max(max_length, i - count_map[count])
            else:
                # Only store first occurrence of count
                count_map[count] = i
                
        return max_length

    def findMaxLength_alternative(self, nums: List[int]) -> int:
        """Alternative solution using transformation of 0s to -1s"""
        # Transform array: 0 -> -1 to make sum = 0 mean equal numbers
        transformed = [-1 if x == 0 else 1 for x in nums]
        
        prefix_sum = 0
        max_length = 0
        sum_map = {0: -1}  # sum -> first index
        
        for i, num in enumerate(transformed):
            prefix_sum += num
            
            if prefix_sum in sum_map:
                max_length = max(max_length, i - sum_map[prefix_sum])
            else:
                sum_map[prefix_sum] = i
                
        return max_length


def test_contiguous_array():
    """Test function to verify both solution approaches"""
    solution = Solution()
    
    test_cases = [
        ([0,1], 2),
        ([0,1,0], 2),
        ([0,0,1,1], 4),
        ([0,1,1,0,1,1,1,0], 4),
        ([0], 0),
        ([1], 0),
        ([], 0),
        ([0,0,0,1,1,1,0], 6),
        ([1,1,1,1], 0),
        ([0,0,1,0,0,0,1,1], 6),
        ([0,1,1,0,1,1,1,0,0,0], 8),
        ([1,0,1,0,1,0,1,0], 8),
        ([0,0,0,0,0,1,1,1,1,1], 10)
    ]
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        # Test main solution
        result_main = solution.findMaxLength(nums)
        # Test alternative solution
        result_alt = solution.findMaxLength_alternative(nums)
        
        status_main = "✓" if result_main == expected else "✗"
        status_alt = "✓" if result_alt == expected else "✗"
        
        print(f"Test {i}:")
        print(f"Input: nums={nums}")
        print(f"Main Solution: {status_main} Got: {result_main}")
        print(f"Alternative Solution: {status_alt} Got: {result_alt}")
        print(f"Expected: {expected}\n")


if __name__ == "__main__":
    test_contiguous_array()