"""
LeetCode 673 - Number of Longest Increasing Subsequence

Problem Statement:
Given an integer array nums, return the number of longest increasing subsequences.
Notice that the sequence has to be strictly increasing.

Logic:
1. Use Dynamic Programming with two arrays:
   - lengths[i]: length of LIS ending at index i
   - counts[i]: number of LIS ending at index i
2. For each position i:
   - Compare with all previous positions j
   - If nums[i] > nums[j]:
     * If we find longer sequence: update length and reset count
     * If we find same length: add to count
3. Finally:
   - Find max length
   - Sum counts of all positions with max length

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # lengths[i] will be the length of the LIS ending at index i
        lengths = [1] * n
        # counts[i] will be the number of LIS ending at index i
        counts = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        # reset count because we found a longer sequence
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        # found another sequence of the same length
                        counts[i] += counts[j]

        # Find the length of the longest increasing subsequence
        longest = max(lengths)

        # Sum up the counts of the subsequences that have the longest length
        return sum(count for length, count in zip(lengths, counts) if length == longest)


def test_number_of_lis():
    solution = Solution()

    test_cases = [
        {
            'nums': [1, 3, 5, 4, 7],
            'expected': 2,
            'description': "Two LIS: [1,3,4,7] and [1,3,5,7]"
        },
        {
            'nums': [2, 2, 2, 2, 2],
            'expected': 5,
            'description': "Five LIS of length 1"
        },
        {
            'nums': [1, 2, 4, 3, 5, 4, 7, 2],
            'expected': 3,
            'description': "Complex case with multiple sequences"
        },
        {
            'nums': [3, 1, 2],
            'expected': 1,
            'description': "Single LIS [1,2]"
        }
    ]

    print("Testing Number of Longest Increasing Subsequences:")
    for i, test in enumerate(test_cases, 1):
        result = solution.findNumberOfLIS(test['nums'])
        print(f"\nTest Case {i} ({test['description']}):")
        print(f"Input array: {test['nums']}")
        print(f"Expected number of LIS: {test['expected']}")
        print(f"Result: {result}")
        print(
            f"Status: {'PASSED' if result == test['expected'] else 'FAILED'}")


if __name__ == "__main__":
    test_number_of_lis()
