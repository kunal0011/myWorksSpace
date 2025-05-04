"""
LeetCode 2089 - Find Target Indices After Sorting Array

Problem Statement:
You are given a 0-indexed integer array nums and a target element target.
A target index is an index i such that nums[i] == target.
Return a list of all target indices after sorting nums in non-decreasing order.
The list should be sorted in ascending order.

Time Complexity: O(n log n) due to sorting
Space Complexity: O(k) where k is the count of target numbers
"""

from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        """
        Logic:
        1. First sort the array in ascending order
        2. Two approaches possible:
           a. Linear scan (current): O(n)
              - Iterate through sorted array and collect indices where num equals target
           b. Optimal for very large arrays with few targets: O(log n)
              - Use binary search to find first and last occurrence
              - Return range between them

        Args:
            nums: List of integers
            target: Integer to find
        Returns:
            List of indices where target appears in sorted array
        """
        # Count numbers less than target and equal to target
        less = sum(1 for x in nums if x < target)
        equal = sum(1 for x in nums if x == target)

        # Return range of indices
        return list(range(less, less + equal))


# Alternative solution using binary search
class SolutionBinarySearch:
    def find_first(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        first = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first = mid
                right = mid - 1  # Look in left half
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first

    def find_last(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        last = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                last = mid
                left = mid + 1  # Look in right half
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last

    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        first = self.find_first(nums, target)
        if first == -1:
            return []
        last = self.find_last(nums, target)
        return list(range(first, last + 1))


# Test driver
def main():
    # Test cases
    test_cases = [
        {
            'nums': [1, 2, 5, 2, 3],
            'target': 2,
            'expected': [1, 2]
        },
        {
            'nums': [1, 2, 5, 2, 3],
            'target': 3,
            'expected': [3]
        },
        {
            'nums': [1, 2, 5, 2, 3],
            'target': 5,
            'expected': [4]
        },
        {
            'nums': [1, 2, 5, 2, 3],
            'target': 4,
            'expected': []
        }
    ]

    solution = Solution()

    for i, test in enumerate(test_cases, 1):
        result = solution.targetIndices(test['nums'], test['target'])
        status = "PASSED" if result == test['expected'] else "FAILED"
        print(f"Test {i}: {status}")
        print(f"Input: nums = {test['nums']}, target = {test['target']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}\n")


if __name__ == "__main__":
    main()
