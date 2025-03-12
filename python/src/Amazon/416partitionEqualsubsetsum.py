"""
LeetCode 416 - Partition Equal Subset Sum

Problem Statement:
-----------------
Given an integer array nums, return true if you can partition the array into two subsets 
such that the sum of the elements in both subsets is equal or false otherwise.

Key Points:
----------
1. We need to find if array can be split into two subsets with equal sums
2. Each element must be used exactly once
3. The order of elements doesn't matter
4. The solution uses dynamic programming for optimization

Examples:
--------
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:
-----------
* 1 <= nums.length <= 200
* 1 <= nums[i] <= 100
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Determines if nums can be partitioned into two equal sum subsets.
        
        Algorithm:
        1. Calculate total sum - if odd, return False (can't partition equally)
        2. Target sum for each subset would be total_sum/2
        3. Use dynamic programming to find if subset with target sum exists
        
        Time Complexity: O(n * target) where n is length of nums and target is total_sum/2
        Space Complexity: O(target)
        """
        # Calculate total sum
        total_sum = sum(nums)
        
        # If total is odd, we can't partition into equal subsets
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(nums)

        # DP array where dp[i] represents if sum i can be achieved
        # using some combination of numbers
        dp = [False] * (target + 1)
        dp[0] = True  # Empty subset has sum 0

        # For each number, update possible sums in reverse order
        # to avoid using same number multiple times
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]


def test_can_partition():
    """
    Test driver for the partition equal subset sum problem
    """
    test_cases = [
        ([1, 5, 11, 5], True),  # Basic case where partition is possible
        ([1, 2, 3, 5], False),  # Cannot be partitioned
        ([1, 1], True),  # Smallest possible case
        ([1, 2, 3, 4, 5, 6, 7], True),  # Larger case with solution
        ([100], False),  # Single element
        ([1, 2, 5], False),  # Simple impossible case
        ([2, 2, 1, 1], True),  # Even number of same elements
        ([1, 2, 3, 6], False),  # Sum is even but no valid partition
        ([1, 1, 1, 1], True),  # All same numbers
    ]
    
    solution = Solution()
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.canPartition(nums)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test case {i}: {status}")
        print(f"Input: nums = {nums}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print("-" * 40)

if __name__ == "__main__":
    test_can_partition()
