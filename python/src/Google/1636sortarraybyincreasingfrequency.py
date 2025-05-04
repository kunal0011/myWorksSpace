"""
LeetCode 1636. Sort Array by Increasing Frequency

Problem Statement:
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. 
If multiple values have the same frequency, sort them in decreasing order.
Return the sorted array.

Time Complexity: O(nlogn) where n is the length of the array
Space Complexity: O(n) for storing frequency counts
"""

from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Logic:
        # 1. Use Counter to count frequency of each number
        # 2. Sort array using custom key:
        #    - Primary key: frequency (ascending)
        #    - Secondary key: number itself (descending)
        # 3. Return sorted array

        # Count frequency of each number
        freq = Counter(nums)

        # Sort using custom comparator
        # For same frequency, larger number comes first (descending)
        # For different frequencies, smaller frequency comes first (ascending)
        return sorted(nums, key=lambda x: (freq[x], -x))


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        [1, 1, 2, 2, 2, 3],          # Expected: [3,1,1,2,2,2]
        [2, 3, 1, 3, 2],            # Expected: [1,3,3,2,2]
        [-1, 1, -6, 4, 5, -6, 1, 4, 1],  # Expected: [5,-1,4,4,-6,-6,1,1,1]
        [1, 2, 2, 3, 3, 3],          # Expected: [1,2,2,3,3,3]
    ]

    for i, nums in enumerate(test_cases):
        result = solution.frequencySort(nums)
        print(f"Test case {i + 1}:")
        print(f"Input array: {nums}")
        print(f"Sorted by frequency: {result}")

        # Print frequency analysis
        freq = Counter(nums)
        print("Frequency analysis:")
        for num in sorted(freq.keys()):
            print(f"Number {num}: appears {freq[num]} times")
        print()
