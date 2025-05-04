"""
LeetCode 1708. Largest Subarray Length K

Problem Statement:
An array A is larger than some array B if for the first index i where A[i] != B[i], A[i] > B[i].
Given an array nums of integers and integer k, return the lexicographically largest subarray of length k.

Time Complexity: O(n) where n is length of array
Space Complexity: O(k) for returning the subarray
"""

from typing import List


class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        # Logic:
        # 1. For each possible starting index i from 0 to n-k:
        #    - Compare subarray starting at i with current max subarray
        #    - If current subarray is lexicographically larger, update max_index
        # 2. Return subarray of length k starting from max_index

        # We need to find the starting index of the largest subarray of length k
        max_index = 0
        for i in range(1, len(nums) - k + 1):
            if nums[i:i+k] > nums[max_index:max_index+k]:
                max_index = i
        return nums[max_index:max_index+k]


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([1, 4, 5, 2, 3], 3),              # Expected: [5,2,3]
        ([1, 4, 5, 2, 3], 4),              # Expected: [4,5,2,3]
        ([3, 2, 1], 2),                  # Expected: [3,2]
        ([1, 2, 3, 4, 5], 1),             # Expected: [5]
        ([9, 8, 7, 6, 5, 4, 3, 2, 1], 3)      # Expected: [9,8,7]
    ]

    for i, (nums, k) in enumerate(test_cases):
        result = solution.largestSubarray(nums, k)
        print(f"Test case {i + 1}:")
        print(f"Input array: {nums}")
        print(f"k: {k}")
        print(f"Largest subarray of length {k}: {result}")

        # Print all possible subarrays for verification
        print("All possible subarrays of length k:")
        for j in range(len(nums) - k + 1):
            print(f"Starting at index {j}: {nums[j:j+k]}")
        print()
