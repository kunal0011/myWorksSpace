"""
LeetCode 532 - K-diff Pairs in an Array

Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
- 0 <= i, j < nums.length
- i != j
- |nums[i] - nums[j]| == k

Note that |val| denotes the absolute value of val.

Example 1:
Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:
Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:
Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
"""

from typing import List
from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """
        Hash map based solution.
        Time complexity: O(n)
        Space complexity: O(n)
        """
        count = Counter(nums)
        pairs = 0
        
        for num in count:
            # For k > 0, look for num + k in counter
            if k > 0 and num + k in count:
                pairs += 1
            # For k = 0, check if the number appears more than once
            elif k == 0 and count[num] > 1:
                pairs += 1
                
        return pairs

    def findPairs_twoPointer(self, nums: List[int], k: int) -> int:
        """
        Two pointer solution with sorting.
        Time complexity: O(n log n)
        Space complexity: O(1) excluding the space needed for sorting
        """
        if not nums or k < 0:
            return 0
            
        nums.sort()
        left = 0
        right = 1
        pairs = 0
        n = len(nums)
        
        while left < n and right < n:
            # Skip duplicates for left pointer
            if left > 0 and nums[left] == nums[left - 1]:
                left += 1
                continue
                
            # Make sure right is ahead of left
            if right <= left:
                right = left + 1
                continue
                
            diff = nums[right] - nums[left]
            
            if diff == k:
                pairs += 1
                left += 1
                right += 1
            elif diff < k:
                right += 1
            else:
                left += 1
                
        return pairs


def test_kdiff_pairs():
    """Test function to verify both solution approaches"""
    solution = Solution()
    
    test_cases = [
        # Basic test cases from problem description
        ([3,1,4,1,5], 2, 2),
        ([1,2,3,4,5], 1, 4),
        ([1,3,1,5,4], 0, 1),
        
        # Additional test cases
        ([], 1, 0),                    # Empty array
        ([1], 0, 0),                   # Single element
        ([1,1,1,1], 0, 1),            # All same elements
        ([1,1,1,2,2,2], 0, 2),        # Multiple duplicates
        ([1,2,3,4,5], 2, 3),          # Consecutive numbers
        ([1,1,1,2,2,2,3,3,3], 1, 2),  # Groups of duplicates
        ([1,2,4,4,3,3,0,9,2,3], 3, 2),# Complex case
        ([-1,0,1], 1, 2),             # Negative numbers
        ([3,1,4,1,5], -1, 0),         # Negative k
        ([1,2,3,4,5], 10, 0)          # k larger than any difference
    ]
    
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        # Create copies of nums for each solution
        nums1 = nums.copy()
        nums2 = nums.copy()
        
        # Test hash map solution
        result_hash = solution.findPairs(nums1, k)
        # Test two pointer solution
        result_two_pointer = solution.findPairs_twoPointer(nums2, k)
        
        status_hash = "✓" if result_hash == expected else "✗"
        status_two_pointer = "✓" if result_two_pointer == expected else "✗"
        
        print(f"Test {i}:")
        print(f"Input: nums={nums}, k={k}")
        print(f"Hash Map Solution: {status_hash} Got: {result_hash}")
        print(f"Two Pointer Solution: {status_two_pointer} Got: {result_two_pointer}")
        print(f"Expected: {expected}\n")


if __name__ == "__main__":
    test_kdiff_pairs()