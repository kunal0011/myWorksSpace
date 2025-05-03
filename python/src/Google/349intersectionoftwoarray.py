"""
LeetCode 349 - Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Time Complexity: O(n) where n is the length of the longer array
Space Complexity: O(n) for storing the sets
"""

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert both lists to sets - O(n) time and space
        set1 = set(nums1)
        set2 = set(nums2)

        # Find the intersection of both sets - O(min(n,m)) time
        intersection = set1 & set2

        # Convert the result to a list
        return list(intersection)


def test_intersection():
    # Test cases
    test_cases = [
        ([1, 2, 2, 1], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4]),
        ([], [1, 2, 3]),
        ([1, 2, 3], []),
        ([1, 1, 1], [1, 1]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ]

    expected_outputs = [
        [2],
        [4, 9],
        [],
        [],
        [1],
        [1, 2, 3, 4, 5],
    ]

    solution = Solution()
    for i, ((nums1, nums2), expected) in enumerate(zip(test_cases, expected_outputs)):
        result = solution.intersection(nums1, nums2)
        print(f"Test case {i + 1}:")
        print(f"Input: nums1 = {nums1}, nums2 = {nums2}")
        print(f"Expected: {sorted(expected)}")
        print(f"Got: {sorted(result)}")
        print(f"{'✓ Passed' if sorted(result) == sorted(expected) else '✗ Failed'}\n")


if __name__ == "__main__":
    test_intersection()
