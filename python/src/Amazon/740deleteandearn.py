"""
LeetCode 740: Delete and Earn

You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

- Pick any nums[i] and delete it to earn nums[i] points
- Delete ALL elements equal to nums[i] - 1 and nums[i] + 1
- Continue doing this until there are no more elements to delete

Return the maximum number of points you can earn by applying the above operation some number of times.
"""

from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Optimize by using Counter to handle duplicates efficiently
        count = Counter(nums)
        
        # Find the range we need to process
        min_num = min(nums)
        max_num = max(nums)
        
        # Use just two variables instead of an array for dp
        # prev2 represents dp[i-2], prev1 represents dp[i-1]
        prev1 = prev2 = 0
        
        # Process only the numbers that exist in the input
        for num in range(min_num, max_num + 1):
            # Current represents dp[i]
            current = max(prev1, prev2 + count[num] * num)
            prev2 = prev1
            prev1 = current
            
        return prev1


def test_delete_and_earn():
    """Test function for Delete and Earn solution"""
    test_cases = [
        ([3, 4, 2], 6),
        ([2, 2, 3, 3, 3, 4], 9),
        ([1], 1),
        ([], 0),
        ([1, 1, 1], 3),
        ([8,3,4,7,6,6,9,2,5,8,2,4,9,5,9,1,5,7,1,4], 61),
        ([1, 2, 3, 4], 6),
    ]
    
    solution = Solution()
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.deleteAndEarn(nums)
        success = result == expected
        print(f"\nTest case {i}:")
        print(f"Input: {nums}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if success else '✗ Failed'}")


if __name__ == "__main__":
    test_delete_and_earn()
