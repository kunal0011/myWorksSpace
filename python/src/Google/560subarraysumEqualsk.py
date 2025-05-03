"""
LeetCode 560 - Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals k.
A subarray is a contiguous non-empty sequence of elements within an array.

Logic:
1. Use prefix sum technique with a hash map to store running sums
2. For each position, calculate cumulative sum and check if (current_sum - k) exists in map
3. If it exists, add its frequency to the count as those positions form valid subarrays
4. Store current_sum in the map with its frequency

Time Complexity: O(n) where n is length of nums
Space Complexity: O(n) for storing prefix sums
"""

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_sums = defaultdict(int)
        # To handle the case when subarray starts from index 0
        prefix_sums[0] = 1

        for num in nums:
            current_sum += num
            # Check if there is a prefix sum that we can subtract to get k
            if (current_sum - k) in prefix_sums:
                count += prefix_sums[current_sum - k]
            # Add the current prefix sum to the map
            prefix_sums[current_sum] += 1

        return count


def run_test_cases():
    solution = Solution()
    test_cases = [
        {
            "nums": [1, 1, 1],
            "k": 2,
            "expected": 2,
            "explanation": "Subarrays [1,1] at two positions sum to 2"
        },
        {
            "nums": [1, 2, 3],
            "k": 3,
            "expected": 2,
            "explanation": "Subarrays [1,2] and [3] sum to 3"
        },
        {
            "nums": [1],
            "k": 0,
            "expected": 0,
            "explanation": "No subarray sums to 0"
        },
        {
            "nums": [-1, -1, 1],
            "k": 0,
            "expected": 1,
            "explanation": "Subarray [-1,1] sums to 0"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.subarraySum(test["nums"], test["k"])
        print(f"\nTest Case {i}:")
        print(f"Array: {test['nums']}")
        print(f"k: {test['k']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"Explanation: {test['explanation']}")
        print(f"{'✓ Passed' if result == test['expected'] else '✗ Failed'}")


if __name__ == "__main__":
    run_test_cases()
