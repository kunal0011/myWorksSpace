"""
LeetCode 209 - Minimum Size Subarray Sum

Problem Statement:
Given an array of positive integers nums and a positive integer target, return the minimal length 
of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0.

Solution Logic:
1. Use sliding window technique with two pointers (left and right)
2. Expand window by adding elements from right
3. When sum >= target, try to minimize window by removing elements from left
4. Keep track of minimum length found
5. Time complexity: O(n), Space complexity: O(1)
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = float('inf')  # Initialize minimum length to infinity
        current_sum = 0
        left = 0  # Left pointer of the sliding window

        for right in range(n):
            # Expand the window by including nums[right]
            current_sum += nums[right]

            # Contract the window until the sum is less than target
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0

def test_min_subarray():
    solution = Solution()
    
    # Test Case 1: Regular case
    nums1 = [2,3,1,2,4,3]
    target1 = 7
    result1 = solution.minSubArrayLen(target1, nums1)
    print(f"Test 1: nums={nums1}, target={target1}")
    print(f"Output: {result1}")  # Expected: 2
    
    # Test Case 2: No solution exists
    nums2 = [1,1,1,1]
    target2 = 7
    result2 = solution.minSubArrayLen(target2, nums2)
    print(f"\nTest 2: nums={nums2}, target={target2}")
    print(f"Output: {result2}")  # Expected: 0
    
    # Test Case 3: Single element solution
    nums3 = [4,1,4]
    target3 = 4
    result3 = solution.minSubArrayLen(target3, nums3)
    print(f"\nTest 3: nums={nums3}, target={target3}")
    print(f"Output: {result3}")  # Expected: 1

if __name__ == "__main__":
    test_min_subarray()
