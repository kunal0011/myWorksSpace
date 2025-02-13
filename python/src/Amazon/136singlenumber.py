"""
LeetCode 136. Single Number

Problem Statement:
Given a non-empty array of integers nums, every element appears twice except for one.
Find that single element.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4
- Each element in the array appears twice except for one element which appears only once
"""

from typing import List, Tuple
from functools import reduce
from operator import xor


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        XOR approach - most efficient solution.
        Time complexity: O(n)
        Space complexity: O(1)

        Properties of XOR used:
        1. a ^ a = 0 (number XOR itself = 0)
        2. a ^ 0 = a (number XOR 0 = number)
        3. a ^ b ^ a = b (XOR is associative)
        """
        return reduce(xor, nums)

    def singleNumberWithSteps(self, nums: List[int]) -> Tuple[int, List[Tuple[int, int]]]:
        """
        Returns both result and intermediate XOR steps.
        Time complexity: O(n)
        Space complexity: O(n) for tracking steps
        """
        steps = []
        result = 0

        for num in nums:
            prev_result = result
            result ^= num
            steps.append((num, result))

        return result, steps


def visualize_xor_steps(steps: List[Tuple[int, int]]) -> None:
    """
    Helper function to visualize XOR operation steps.
    """
    print("\nXOR Operation Steps:")
    print("Step | Number | Running XOR | Binary Representation")
    print("-" * 60)

    for i, (num, running_xor) in enumerate(steps):
        # Get binary representations
        num_binary = format(num & 0xFFFFFFFF, '032b')
        xor_binary = format(running_xor & 0xFFFFFFFF, '032b')

        # Truncate binary for display
        num_binary = "..." + num_binary[-8:]
        xor_binary = "..." + xor_binary[-8:]

        print(f"{i:4d} | {num:6d} | {running_xor:10d} | {num_binary} -> {xor_binary}")


def test_single_number():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "nums": [2, 2, 1],
            "expected": 1,
            "description": "Basic case"
        },
        {
            "nums": [4, 1, 2, 1, 2],
            "expected": 4,
            "description": "Multiple pairs"
        },
        {
            "nums": [1],
            "expected": 1,
            "description": "Single element"
        },
        {
            "nums": [-1, -1, -2],
            "expected": -2,
            "description": "Negative numbers"
        },
        {
            "nums": [1, 1, 2, 2, 3, 3, 4],
            "expected": 4,
            "description": "Ordered pairs"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print(f"Input array: {test_case['nums']}")

        # Test both implementations
        result1 = solution.singleNumber(test_case['nums'])
        result2, steps = solution.singleNumberWithSteps(test_case['nums'])

        print(f"\nResults:")
        print(f"Single number: {result1}")

        # Visualize XOR steps
        visualize_xor_steps(steps)

        # Verify frequency
        frequency = {}
        for num in test_case['nums']:
            frequency[num] = frequency.get(num, 0) + 1

        print("\nFrequency verification:")
        for num, freq in frequency.items():
            print(f"Number {num}: appears {freq} time(s)")

        assert result1 == test_case['expected'], \
            f"Basic approach failed. Expected {test_case['expected']}, got {result1}"
        assert result2 == test_case['expected'], \
            f"Step tracking failed. Expected {test_case['expected']}, got {result2}"
        assert frequency[result1] == 1, \
            f"Result {result1} appears {frequency[result1]} times, expected once"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_single_number()
