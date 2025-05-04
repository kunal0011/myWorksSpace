"""
LeetCode 2150 - Find All Lonely Numbers in the Array

Problem Statement:
You are given an integer array nums. A number x is lonely when it appears exactly once in nums,
and no adjacent values (x + 1 or x - 1) appear in nums. Return all lonely numbers in nums.
You may return the answer in any order.

Time Complexity: O(n) where n is length of nums
Space Complexity: O(n) for storing counter and result
"""

from collections import Counter


class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        """
        Logic:
        1. Use Counter to get frequency of each number
        2. For each number in nums:
           - Check if it appears exactly once
           - Check if neither (num-1) nor (num+1) exist in array
           - If both conditions true, it's lonely
        3. Return list of lonely numbers

        Args:
            nums: List of integers
        Returns:
            List of lonely integers
        """
        count = Counter(nums)
        lonely_numbers = []

        for num in nums:
            if count[num] == 1 and count[num - 1] == 0 and count[num + 1] == 0:
                lonely_numbers.append(num)

        return lonely_numbers


# Test driver
def main():
    # Test cases
    test_cases = [
        {
            'nums': [10, 6, 5, 8],
            'expected': [10, 8]
        },
        {
            'nums': [1, 3, 5, 3],
            'expected': [1, 5]
        },
        {
            'nums': [1, 1, 1, 1],
            'expected': []
        }
    ]

    solution = Solution()

    for i, test in enumerate(test_cases, 1):
        result = solution.findLonely(test['nums'])
        # Sort for consistent comparison
        result.sort()
        expected = sorted(test['expected'])
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test {i}: {status}")
        print(f"Input: nums = {test['nums']}")
        print(f"Output: {result}")
        print(f"Expected: {expected}\n")


if __name__ == "__main__":
    main()
