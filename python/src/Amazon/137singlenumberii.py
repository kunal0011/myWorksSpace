"""
LeetCode 137. Single Number II

Problem Statement:
Given an integer array nums where every element appears three times except for one,
which appears exactly once. Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,3,2]
Output: 3
Explanation: The element 3 appears only once.

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99
Explanation: The element 99 appears only once.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -2^31 <= nums[i] <= 2^31 - 1
- Each element in nums appears exactly three times except for one element which appears once
"""

from typing import List, Tuple
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Bit manipulation approach.
        Time complexity: O(n)
        Space complexity: O(1)
        """
        ones = 0
        twos = 0

        for num in nums:
            # First appearance: ones = 1, twos = 0
            # Second appearance: ones = 0, twos = 1
            # Third appearance: ones = 0, twos = 0
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones

    def singleNumberWithSteps(self, nums: List[int]) -> Tuple[int, List[Tuple[int, int, int]]]:
        """
        Returns both result and intermediate steps.
        Time complexity: O(n)
        Space complexity: O(n) for tracking steps
        """
        ones = 0
        twos = 0
        steps = []

        for num in nums:
            prev_ones, prev_twos = ones, twos
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
            steps.append((num, ones, twos))

        return ones, steps


def visualize_bits(num: int, width: int = 8) -> str:
    """
    Helper function to visualize binary representation.
    """
    binary = format(num & ((1 << width) - 1), f'0{width}b')
    return ' '.join(binary[i:i+4] for i in range(0, len(binary), 4))


def visualize_steps(steps: List[Tuple[int, int, int]]) -> None:
    """
    Helper function to visualize bit manipulation steps.
    """
    print("\nBit Manipulation Steps:")
    print("Step | Number |   Ones   |   Twos   | Binary (last 8 bits)")
    print("-" * 70)

    for i, (num, ones, twos) in enumerate(steps):
        print(f"{i:4d} | {num:6d} | {ones:8d} | {twos:8d} | "
              f"num: {visualize_bits(num)} | "
              f"ones: {visualize_bits(ones)} | "
              f"twos: {visualize_bits(twos)}")


def test_single_number():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "nums": [2, 2, 3, 2],
            "expected": 3,
            "description": "Basic case"
        },
        {
            "nums": [0, 1, 0, 1, 0, 1, 99],
            "expected": 99,
            "description": "Multiple triplets"
        },
        {
            "nums": [1],
            "expected": 1,
            "description": "Single element"
        },
        {
            "nums": [-2, -2, 1, -2],
            "expected": 1,
            "description": "Negative numbers"
        },
        {
            "nums": [1, 1, 1, 2, 2, 2, 3],
            "expected": 3,
            "description": "Ordered triplets"
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

        # Visualize steps
        visualize_steps(steps)

        # Verify frequency
        frequency = Counter(test_case['nums'])
        print("\nFrequency verification:")
        for num, freq in frequency.items():
            print(f"Number {num}: appears {freq} time(s)")

        assert result1 == test_case['expected'], \
            f"Basic approach failed. Expected {test_case['expected']}, got {result1}"
        assert result2 == test_case['expected'], \
            f"Step tracking failed. Expected {test_case['expected']}, got {result2}"
        assert frequency[result1] == 1, \
            f"Result {result1} appears {frequency[result1]} times, expected once"

        # Verify all other numbers appear exactly three times
        for num, freq in frequency.items():
            if num != result1:
                assert freq == 3, f"Number {num} appears {freq} times, expected 3"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_single_number()
