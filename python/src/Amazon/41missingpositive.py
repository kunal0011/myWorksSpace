from typing import List

"""
LeetCode 41. First Missing Positive

Problem Statement:
Given an unsorted integer array nums, find the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

Constraints:
- 1 <= nums.length <= 5 * 10^5
- -2^31 <= nums[i] <= 2^31 - 1
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Place each number in its correct position if possible
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the number at its correct position
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Step 2: Find the first position where number doesn't match index+1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all positions are correct, the missing number is n + 1
        return n + 1


def explain_solution(nums: List[int]) -> None:
    """
    Function to explain the solution process step by step
    """
    print(f"\nFinding first missing positive in: {nums}")
    print("=" * 50)

    n = len(nums)
    nums = nums.copy()  # Make a copy to not modify original

    print("\nStep 1: Place numbers in correct positions")
    print(f"Initial array: {nums}")

    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            print(f"Current array: {nums}")
            print(
                f"Swapping nums[{i}]={nums[i]} with nums[{nums[i]-1}]={nums[nums[i]-1]}")
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    print(f"\nAfter placement: {nums}")

    print("\nStep 2: Check each position")
    for i in range(n):
        print(f"Position {i}: expecting {i+1}, found {nums[i]}")
        if nums[i] != i + 1:
            print(f"First mismatch found: {i+1} is missing")
            return i + 1

    print(f"All positions matched, so {n+1} is missing")
    return n + 1


def test_first_missing_positive():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "nums": [1, 2, 0],
            "expected": 3,
            "description": "Basic case with zero"
        },
        {
            "nums": [3, 4, -1, 1],
            "expected": 2,
            "description": "Array with negative number"
        },
        {
            "nums": [7, 8, 9, 11, 12],
            "expected": 1,
            "description": "Missing one"
        },
        {
            "nums": [1],
            "expected": 2,
            "description": "Single element array"
        },
        {
            "nums": [1, 1],
            "expected": 2,
            "description": "Array with duplicates"
        },
        {
            "nums": [-1, -2, -3],
            "expected": 1,
            "description": "All negative numbers"
        },
        {
            "nums": [1, 2, 3, 4, 5],
            "expected": 6,
            "description": "All consecutive numbers"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        nums = test_case["nums"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: nums = {nums}")

        result = solution.firstMissingPositive(nums.copy())

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_first_missing_positive()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_solution([3, 4, -1, 1])
        explain_solution([1, 2, 0])
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
