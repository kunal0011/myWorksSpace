"""
LeetCode 485 - Max Consecutive Ones

Problem Statement:
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. 
The maximum number of consecutive 1s is 3.

Time Complexity: O(n) where n is the length of the array
Space Complexity: O(1) as we only use two variables
"""


def findMaxConsecutiveOnes(nums: list[int]) -> int:
    max_ones = 0  # stores the maximum consecutive ones seen so far
    current_ones = 0  # stores the current streak of ones

    for num in nums:
        if num == 1:
            current_ones += 1  # increment streak for 1
            max_ones = max(max_ones, current_ones)  # update max if needed
        else:
            current_ones = 0  # reset streak when we see 0

    return max_ones

# Test driver


def run_tests():
    test_cases = [
        ([1, 1, 0, 1, 1, 1], 3),
        ([1, 0, 1, 1, 0, 1], 2),
        ([0, 0, 0], 0),
        ([1, 1, 1, 1], 4),
        ([], 0)
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = findMaxConsecutiveOnes(nums)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status}")
        print(f"Input: {nums}")
        print(f"Expected: {expected}")
        print(f"Got: {result}\n")


if __name__ == "__main__":
    run_tests()
