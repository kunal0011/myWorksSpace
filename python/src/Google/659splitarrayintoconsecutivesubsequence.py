"""
LeetCode 659 - Split Array into Consecutive Subsequences

Problem Statement:
Given an integer array nums sorted in ascending order, return true if it is possible
to split nums into one or more subsequences such that:
- Each subsequence has a length of 3 or more
- All subsequences consist of consecutive integers

Logic:
1. Use greedy approach with two hash maps:
   - freq: tracks remaining frequency of each number
   - append: tracks number of sequences ending at each number
2. For each number, either:
   - Append it to existing sequence ending at num-1
   - Start new sequence of length 3 with num, num+1, num+2
3. If neither is possible, return False

Time Complexity: O(n) where n is length of nums
Space Complexity: O(n) for hash maps
"""

from collections import defaultdict


class Solution:
    def isPossible(self, nums: list[int]) -> bool:
        # Frequency map to count occurrences of each number in nums
        freq = defaultdict(int)
        # Append map to track the number of subsequences that can be extended with a given number
        append = defaultdict(int)

        # Populate the frequency map
        for num in nums:
            freq[num] += 1

        # Iterate through the array to build subsequences
        for num in nums:
            if freq[num] == 0:
                continue

            # If we can append `num` to an existing subsequence ending in `num-1`
            if append[num - 1] > 0:
                append[num - 1] -= 1
                append[num] += 1
            # Otherwise, try to start a new subsequence with `num, num+1, num+2`
            elif freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                append[num + 2] += 1
            else:
                return False

            # Decrement the frequency of `num` as it is used
            freq[num] -= 1

        return True


def test_split_array():
    solution = Solution()

    test_cases = [
        {
            'nums': [1, 2, 3, 3, 4, 5],
            'expected': True,
            'description': "Can be split into [1,2,3], [3,4,5]"
        },
        {
            'nums': [1, 2, 3, 3, 4, 4, 5, 5],
            'expected': True,
            'description': "Can be split into [1,2,3,4,5], [3,4,5]"
        },
        {
            'nums': [1, 2, 3, 4, 4, 5],
            'expected': False,
            'description': "Cannot be split into valid subsequences"
        },
        {
            'nums': [1, 2, 3, 4, 5, 6, 7, 8, 9],
            'expected': True,
            'description': "Can be split into [1,2,3], [4,5,6], [7,8,9]"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.isPossible(test['nums'])
        print(f"\nTest Case {i} ({test['description']}):")
        print(f"Input array: {test['nums']}")
        print(f"Expected: {test['expected']}")
        print(f"Result: {result}")
        print(
            f"Status: {'PASSED' if result == test['expected'] else 'FAILED'}")


if __name__ == "__main__":
    test_split_array()
