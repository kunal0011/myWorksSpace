from typing import List

"""
LeetCode 45. Jump Game II

Problem Statement:
Given an array of non-negative integers nums, you are initially positioned at the first index.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 1000
- It's guaranteed that you can reach the last index
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        jumps = 0
        current_max_reach = 0  # The farthest we can reach with current jumps
        next_max_reach = 0     # The farthest we can reach with one more jump

        # We don't need to check the last element since we're guaranteed to reach it
        for i in range(n - 1):
            # Update the farthest we can reach with one more jump
            next_max_reach = max(next_max_reach, i + nums[i])

            # If we've reached the current maximum, we must jump
            if i == current_max_reach:
                jumps += 1
                current_max_reach = next_max_reach

                # If we can already reach the end, break
                if current_max_reach >= n - 1:
                    break

        return jumps


def explain_jumps(nums: List[int]) -> None:
    """
    Function to explain the jump process step by step
    """
    print(f"\nFinding minimum jumps for array: {nums}")
    print("=" * 50)

    n = len(nums)
    if n == 1:
        print("Array has only one element, no jumps needed")
        return 0

    jumps = 0
    current_max_reach = 0
    next_max_reach = 0

    print("\nStarting jump analysis:")
    print(f"Initial position: index 0, value {nums[0]}")

    for i in range(n - 1):
        prev_next_max = next_max_reach
        next_max_reach = max(next_max_reach, i + nums[i])

        if next_max_reach > prev_next_max:
            print(f"\nAt index {i}, found new max reach: {next_max_reach}")
            print(f"Can jump {nums[i]} steps to reach index {i + nums[i]}")

        if i == current_max_reach:
            jumps += 1
            current_max_reach = next_max_reach
            print(f"\nMust jump! Current position: {i}")
            print(f"Jump #{jumps}: Can now reach index {current_max_reach}")

            if current_max_reach >= n - 1:
                print(f"Can reach the end ({n-1}), no more jumps needed")
                break

    print(f"\nMinimum number of jumps required: {jumps}")
    return jumps


def test_jump():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "nums": [2, 3, 1, 1, 4],
            "expected": 2,
            "description": "Basic case"
        },
        {
            "nums": [2, 3, 0, 1, 4],
            "expected": 2,
            "description": "Case with zero"
        },
        {
            "nums": [1],
            "expected": 0,
            "description": "Single element"
        },
        {
            "nums": [1, 2, 3],
            "expected": 2,
            "description": "Short array"
        },
        {
            "nums": [1, 1, 1, 1],
            "expected": 3,
            "description": "Minimum jumps"
        },
        {
            "nums": [3, 2, 1],
            "expected": 1,
            "description": "Can reach end in one jump"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        nums = test_case["nums"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: nums = {nums}")

        result = solution.jump(nums.copy())

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_jump()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_jumps([2, 3, 1, 1, 4])
        explain_jumps([2, 3, 0, 1, 4])
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
