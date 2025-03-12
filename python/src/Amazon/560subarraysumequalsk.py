"""
LeetCode 560 - Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Explanation: Subarray [1,1] (index 0,1) and [1,1] (index 1,2) have sum = 2.

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
Explanation: Subarray [1,2] and [3] have sum = 3.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7
"""

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Optimized solution using prefix sum and hashmap
        Time Complexity: O(n) where n is the length of nums
        Space Complexity: O(n) for storing prefix sums
        """
        count = 0
        current_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # To handle the case when subarray starts from index 0

        for num in nums:
            current_sum += num
            # If (current_sum - k) exists in prefix_sums, it means we found a subarray with sum k
            if (current_sum - k) in prefix_sums:
                count += prefix_sums[current_sum - k]
            prefix_sums[current_sum] += 1
            
        return count
    
    def subarraySum_bruteforce(self, nums: List[int], k: int) -> int:
        """
        Brute force solution for validation (not recommended for large inputs)
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        count = 0
        n = len(nums)
        
        for start in range(n):
            current_sum = 0
            for end in range(start, n):
                current_sum += nums[end]
                if current_sum == k:
                    count += 1
                    
        return count


def test_subarray_sum():
    """
    Test function with comprehensive test cases
    """
    solution = Solution()
    
    test_cases = [
        # Basic test cases
        ([1,1,1], 2, 2),
        ([1,2,3], 3, 2),
        
        # Edge cases
        ([1], 1, 1),
        ([1], 0, 0),
        ([0], 0, 1),
        
        # Test cases with negative numbers
        ([1,-1,0], 0, 3),
        ([-1,-1,1], 0, 1),
        
        # Complex test cases
        ([3,4,7,2,-3,1,4,2], 7, 4),
        ([1,2,1,2,1], 3, 4),
        ([-1,-1,1], -2, 1),
        
        # Test cases with multiple solutions
        ([1,1,1,1], 2, 3),
        ([0,0,0,0], 0, 10),  # Includes all possible subarrays
        
        # Test case with large numbers
        ([100,1,2,3,4], 3, 1)
    ]
    
    print("Running tests for Subarray Sum Equals K...\n")
    
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        # Test optimized solution
        result = solution.subarraySum(nums, k)
        # Test brute force solution for validation
        result_bf = solution.subarraySum_bruteforce(nums, k)
        
        print(f"Test Case {i}:")
        print(f"Input: nums = {nums}, k = {k}")
        print(f"Expected: {expected}")
        print(f"Optimized Solution: {result} {'✅' if result == expected else '❌'}")
        print(f"Brute Force Solution: {result_bf} {'✅' if result_bf == expected else '❌'}")
        
        if result != expected:
            print(f"❌ Test case failed!")
            print(f"Got: {result}")
            print(f"Expected: {expected}")
        else:
            print("✅ Test case passed!")
        print()


if __name__ == "__main__":
    test_subarray_sum()
