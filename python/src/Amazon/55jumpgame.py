from typing import List

"""
LeetCode 55. Jump Game

Problem Statement:
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0,
which makes it impossible to reach the last index.

Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Maximum reachable position
        max_reach = 0
        target = len(nums) - 1

        # Check each position until we either can't move forward
        # or we've checked all reachable positions
        for i in range(len(nums)):
            # If we can't reach current position, return False
            if i > max_reach:
                return False

            # Update maximum reachable position
            max_reach = max(max_reach, i + nums[i])

            # If we can reach the target, return True
            if max_reach >= target:
                return True

        return max_reach >= target


def explain_jumps(nums: List[int]) -> None:
    """
    Function to explain the jump game process step by step
    """
    print(f"\nAnalyzing jump possibilities for: {nums}")
    print("=" * 50)

    max_reach = 0
    target = len(nums) - 1

    print(f"Target position: {target}")
    print("\nStarting analysis:")

    for i in range(len(nums)):
        print(f"\nAt position {i} with value {nums[i]}")
        print(f"Current max reach: {max_reach}")

        # Check if we can reach current position
        if i > max_reach:
            print(f"❌ Cannot reach position {i}")
            print("Game Over - Cannot proceed further")
            return False

        # Calculate new max reach
        prev_reach = max_reach
        max_reach = max(max_reach, i + nums[i])

        if max_reach > prev_reach:
            print(f"Updated max reach: {max_reach}")

        # Check if we can reach target
        if max_reach >= target:
            print(
                f"✓ Can reach target! Maximum reach ({max_reach}) >= target ({target})")
            return True

        print(f"Current reachable positions: {list(range(max_reach + 1))}")

    result = max_reach >= target
    if result:
        print(f"✓ Success! Can reach target")
    else:
        print(f"❌ Failed! Cannot reach target")
    return result


def test_jump_game():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "nums": [2, 3, 1, 1, 4],
            "expected": True,
            "description": "Basic case - can reach end"
        },
        {
            "nums": [3, 2, 1, 0, 4],
            "expected": False,
            "description": "Cannot pass zero"
        },
        {
            "nums": [0],
            "expected": True,
            "description": "Single element"
        },
        {
            "nums": [1, 1, 1, 0],
            "expected": True,
            "description": "Exactly enough jumps"
        },
        {
            "nums": [1, 0, 1, 0],
            "expected": False,
            "description": "Trapped by zero"
        },
        {
            "nums": [2, 0, 0],
            "expected": True,
            "description": "Can jump over zeros"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        nums = test_case["nums"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: nums = {nums}")

        result = solution.canJump(nums.copy())

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_jump_game()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_jumps([2, 3, 1, 1, 4])
        explain_jumps([3, 2, 1, 0, 4])
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
