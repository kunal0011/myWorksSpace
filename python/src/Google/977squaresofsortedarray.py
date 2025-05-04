"""
LeetCode 977: Squares of a Sorted Array

Problem Statement:
Given an integer array nums sorted in non-decreasing order, return an array of the squares 
of each number sorted in non-decreasing order.

Logic:
1. Use two-pointer approach since array is already sorted
2. Compare absolute values from both ends since squares of negatives might be larger
3. Fill result array from end to start (largest to smallest)
4. Move pointers based on which absolute value is larger

Time Complexity: O(n) where n is length of array
Space Complexity: O(n) for result array
"""

from typing import List


class Solution:
    def sortedSquares(self, nums):
        # Initialize two pointers
        left, right = 0, len(nums) - 1
        result = [0] * len(nums)  # Result array of the same size as nums
        position = len(nums) - 1  # Position to fill from the end

        # Two-pointer approach
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[position] = nums[left] ** 2
                left += 1
            else:
                result[position] = nums[right] ** 2
                right -= 1
            position -= 1

        return result


def test_sorted_squares():
    solution = Solution()

    # Test case 1: Array with negative numbers
    nums1 = [-4, -1, 0, 3, 10]
    result1 = solution.sortedSquares(nums1)
    expected1 = [0, 1, 9, 16, 100]
    assert result1 == expected1, f"Test case 1 failed. Expected {expected1}, got {result1}"
    print(f"Test case 1 passed: nums={nums1}, result={result1}")

    # Test case 2: Array with only negative numbers
    nums2 = [-7, -3, -1]
    result2 = solution.sortedSquares(nums2)
    expected2 = [1, 9, 49]
    assert result2 == expected2, f"Test case 2 failed. Expected {expected2}, got {result2}"
    print(f"\nTest case 2 passed: nums={nums2}, result={result2}")

    # Test case 3: Array with only positive numbers
    nums3 = [1, 2, 3, 4]
    result3 = solution.sortedSquares(nums3)
    expected3 = [1, 4, 9, 16]
    assert result3 == expected3, f"Test case 3 failed. Expected {expected3}, got {result3}"
    print(f"\nTest case 3 passed: nums={nums3}, result={result3}")

    # Test case 4: Single element array
    nums4 = [-5]
    result4 = solution.sortedSquares(nums4)
    expected4 = [25]
    assert result4 == expected4, f"Test case 4 failed. Expected {expected4}, got {result4}"
    print(f"\nTest case 4 passed: nums={nums4}, result={result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_sorted_squares()
