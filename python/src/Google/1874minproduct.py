"""
LeetCode 1874. Minimize Product Sum of Two Arrays

Problem Statement:
The product sum of two arrays nums1 and nums2 is defined as the sum of nums1[i] * nums2[i] for all 0 <= i < n.
Given two arrays nums1 and nums2 of length n, you can reorder the elements in nums1. Return the minimum product sum
possible after reordering nums1.

Time Complexity: O(nlogn) for sorting
Space Complexity: O(1) as we modify arrays in place
"""

from typing import List


class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Logic:
        # 1. Sort nums1 in ascending order
        # 2. Sort nums2 in descending order
        # 3. Multiply corresponding elements and sum
        # This works because:
        # - To minimize product sum, multiply smallest with largest
        # - This ensures minimum possible products

        nums1.sort()
        nums2.sort(reverse=True)

        return sum(a * b for a, b in zip(nums1, nums2))


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([5, 3, 4, 2], [4, 2, 2, 5]),           # Expected: 40
        ([2, 1, 4, 5, 7], [3, 2, 4, 8, 6]),       # Expected: 65
        ([1, 2], [3, 4]),                    # Expected: 10
        ([12, 4, 3, 1, 5], [2, 4, 3, 5, 1])       # Expected: 40
    ]

    for i, (nums1, nums2) in enumerate(test_cases):
        # Make copies to preserve original arrays for display
        nums1_copy = nums1.copy()
        nums2_copy = nums2.copy()

        result = solution.minProductSum(nums1_copy, nums2_copy)
        print(f"Test case {i + 1}:")
        print(f"nums1: {nums1}")
        print(f"nums2: {nums2}")
        print(f"Minimum product sum: {result}")

        # Show the sorted arrays and products for verification
        print("After sorting:")
        print(f"sorted nums1: {nums1_copy}")
        print(f"sorted nums2: {nums2_copy}")
        print("Products:")
        for a, b in zip(nums1_copy, nums2_copy):
            print(f"{a} * {b} = {a*b}")
        print()
