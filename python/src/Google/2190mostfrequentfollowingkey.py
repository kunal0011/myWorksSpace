"""
LeetCode 2190 - Most Frequent Number Following Key In an Array

Problem Statement:
You are given a 0-indexed integer array nums. You are also given an integer key, which is present in nums.
For every unique integer target in nums, count the number of times target immediately follows key in nums.
Return the target with the maximum count. If there are multiple targets with the maximum count, return the
one with the minimum value.

Time Complexity: O(n) where n is length of nums
Space Complexity: O(k) where k is number of unique targets
"""

from collections import defaultdict


class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        """
        Logic:
        1. Use defaultdict to track frequency of numbers following key
        2. Iterate through array (except last element):
           - If current number is key, increment count of next number
        3. Find number with highest frequency
           - If tie, return smaller number

        Args:
            nums: List of integers
            key: Integer to look for
        Returns:
            Most frequent number following key
        """
        freq_map = defaultdict(int)

        # Iterate through nums and check the pair (key, target)
        for i in range(len(nums) - 1):
            if nums[i] == key:
                target = nums[i + 1]
                freq_map[target] += 1

        # Find the target with the highest frequency
        most_frequent_target = -1
        max_count = 0
        for target, count in freq_map.items():
            if count > max_count or (count == max_count and target < most_frequent_target):
                most_frequent_target = target
                max_count = count

        return most_frequent_target


# Test driver
def main():
    # Test cases
    test_cases = [
        {
            'nums': [1, 100, 200, 1, 100],
            'key': 1,
            'expected': 100
        },
        {
            'nums': [2, 2, 2, 2, 3],
            'key': 2,
            'expected': 2
        },
        {
            'nums': [1, 1000, 2, 1000, 2, 3],
            'key': 2,
            'expected': 3
        }
    ]

    solution = Solution()

    for i, test in enumerate(test_cases, 1):
        result = solution.mostFrequent(test['nums'], test['key'])
        status = "PASSED" if result == test['expected'] else "FAILED"
        print(f"Test {i}: {status}")
        print(f"Input: nums = {test['nums']}, key = {test['key']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}\n")


if __name__ == "__main__":
    main()
