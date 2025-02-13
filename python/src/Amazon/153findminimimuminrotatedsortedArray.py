"""
LeetCode 153. Find Minimum in Rotated Sorted Array

Problem Statement:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:
- [4,5,6,7,0,1,2] if it was rotated 4 times
- [0,1,2,4,5,6,7] if it was rotated 7 times

Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Constraints:
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique
- nums is sorted and rotated between 1 and n times
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Time complexity: O(log n)
        Space complexity: O(1)

        Uses binary search to find the pivot point (minimum element).
        """
        left, right = 0, len(nums) - 1

        # If array is not rotated or has one element
        if nums[left] <= nums[right]:
            return nums[left]

        while left <= right:
            mid = (left + right) // 2

            # If mid+1 is the minimum element
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            # If mid is the minimum element
            if mid > 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]

            # Decide which half to search
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1

        return nums[0]


def test_find_min():
    """Test function with various test cases."""
    solution = Solution()

    test_cases = [
        {
            "nums": [3, 4, 5, 1, 2],
            "expected": 1,
            "description": "Basic rotated array"
        },
        {
            "nums": [4, 5, 6, 7, 0, 1, 2],
            "expected": 0,
            "description": "Rotated array with more elements"
        },
        {
            "nums": [11, 13, 15, 17],
            "expected": 11,
            "description": "Not rotated array"
        },
        {
            "nums": [2, 1],
            "expected": 1,
            "description": "Two elements rotated"
        },
        {
            "nums": [1],
            "expected": 1,
            "description": "Single element"
        },
        {
            "nums": [5, 1, 2, 3, 4],
            "expected": 1,
            "description": "Rotated once from end"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        result = solution.findMin(test_case["nums"])
        assert result == test_case["expected"], \
            f'Test case {i} failed. Expected {test_case["expected"]}, got {result}'
        print(f'Test case {i} passed: {test_case["description"]}')

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_find_min()
