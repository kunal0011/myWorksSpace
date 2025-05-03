"""
LeetCode 416 - Partition Equal Subset Sum

Given an integer array nums, return true if you can partition the array into two subsets 
such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # If total sum is odd, we can't partition into equal subsets
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        n = len(nums)
        
        # dp[i] represents if sum i can be achieved using subset of numbers
        dp = [False] * (target + 1)
        dp[0] = True  # Empty subset has sum 0
        
        for num in nums:
            # Check from target to num (backwards to avoid using same element multiple times)
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target]


# Test driver
def main():
    solution = Solution()
    
    # Test cases
    test_cases = [
        [1,5,11,5],     # Should return True ([1,5,5] and [11])
        [1,2,3,5],      # Should return False
        [2,2,1,1],      # Should return True ([2,2] and [1,1])
        [1,2,5],        # Should return False
        [1,1,1,1],      # Should return True ([1,1] and [1,1])
        [100,100,100,100,100,100,100,100], # Should return True
    ]
    
    for nums in test_cases:
        result = solution.canPartition(nums)
        print(f"\nInput: nums = {nums}")
        print(f"Output: {result}")


if __name__ == "__main__":
    main()