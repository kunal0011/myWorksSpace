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
    print("Test 1:")
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {solution.minSubArrayLen(target1, nums1)}")  # Expected: 2
    
    # Test Case 2: No solution exists
    nums2 = [1,1,1,1]
    target2 = 7
    print("\nTest 2:")
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {solution.minSubArrayLen(target2, nums2)}")  # Expected: 0
    
    # Test Case 3: Exact sum case
    nums3 = [1,4,4]
    target3 = 4
    print("\nTest 3:")
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {solution.minSubArrayLen(target3, nums3)}")  # Expected: 1

if __name__ == "__main__":
    test_min_subarray()
