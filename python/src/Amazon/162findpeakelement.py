"""
LeetCode 162. Find Peak Element

Problem Statement:
A peak element is an element that is strictly greater than its neighbors.
Given an integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2,
or index number 5 where the peak element is 6.

Constraints:
- 1 <= nums.length <= 1000
- -2^31 <= nums[i] <= 2^31 - 1
- nums[i] != nums[i + 1] for all valid i
"""

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Time complexity: O(log n)
        Space complexity: O(1)
        Uses binary search to find a peak element.
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If mid element is less than next element,
            # there must be a peak in the right half
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            # If mid element is greater than next element,
            # there must be a peak in the left half (including mid)
            else:
                right = mid

        return left


def test_find_peak():
    """Test function with various test cases."""
    solution = Solution()

    test_cases = [
        {
            "nums": [1, 2, 3, 1],
            "expected": 2,
            "description": "Basic case with single peak"
        },
        {
            "nums": [1, 2, 1, 3, 5, 6, 4],
            "valid_outputs": [1, 5],
            "description": "Multiple peaks"
        },
        {
            "nums": [1],
            "expected": 0,
            "description": "Single element"
        },
        {
            "nums": [1, 2],
            "expected": 1,
            "description": "Two elements ascending"
        },
        {
            "nums": [2, 1],
            "expected": 0,
            "description": "Two elements descending"
        },
        {
            "nums": [1, 2, 3],
            "expected": 2,
            "description": "Strictly increasing"
        },
        {
            "nums": [3, 2, 1],
            "expected": 0,
            "description": "Strictly decreasing"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        result = solution.findPeakElement(test_case["nums"])

        if "valid_outputs" in test_case:
            assert result in test_case["valid_outputs"], \
                f'Test case {i} failed. Got index {result}, expected one of {test_case["valid_outputs"]}'
        else:
            assert result == test_case["expected"], \
                f'Test case {i} failed. Got index {result}, expected {test_case["expected"]}'

        print(f'Test case {i} passed: {test_case["description"]}')

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_find_peak()
