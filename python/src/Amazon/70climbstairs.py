"""
LeetCode 70. Climbing Stairs

Problem Statement:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n <= 2:
            return n

        # Initialize dp array
        dp = [0] * (n + 1)
        dp[1] = 1  # One way to climb 1 stair
        dp[2] = 2  # Two ways to climb 2 stairs

        # Fill dp array
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]


def explain_dp_climbing_stairs(n: int) -> None:
    """
    Function to explain the DP approach for climbing stairs step by step
    """
    print(f"\nCalculating number of ways to climb {n} stairs using DP")
    print("=" * 50)

    if n <= 2:
        print(f"Input {n} is small, returning {n}")
        return n

    # Initialize dp array
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    print("\nInitializing DP array:")
    print(f"dp[1] = 1 (one way to climb 1 stair)")
    print(f"dp[2] = 2 (two ways to climb 2 stairs)")

    # Fill dp array with explanation
    print("\nFilling DP array:")
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        print(f"\nStep {i}:")
        print(f"Ways to climb {i-1} stairs: {dp[i-1]}")
        print(f"Ways to climb {i-2} stairs: {dp[i-2]}")
        print(f"Total ways to climb {i} stairs: {dp[i]}")
        print("\nCurrent DP array state:")
        print_dp_array(dp, i)

    return dp[n]


def print_dp_array(dp: list, current: int = None) -> None:
    """
    Helper function to print DP array with highlighting
    """
    print("\nIndex:", end=" ")
    for i in range(len(dp)):
        print(f"{i:4}", end=" ")
    print("\nValue:", end=" ")
    for i in range(len(dp)):
        if i == current:
            print(f"\033[92m{dp[i]:4}\033[0m", end=" ")
        else:
            print(f"{dp[i]:4}", end=" ")
    print()


def visualize_dp_solution(n: int) -> None:
    """
    Function to visualize how DP builds the solution
    """
    print(f"\nVisualizing DP solution for n = {n}")
    print("=" * 50)

    # Create a grid to show the building process
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    print("\nDP Array Building Process:")
    print("Each cell shows the number of ways to reach that step")
    print_dp_array(dp)

    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        print(f"\nAfter calculating step {i}:")
        print_dp_array(dp, i)
        print(f"dp[{i}] = dp[{i-1}] + dp[{i-2}] = {dp[i-1]} + {dp[i-2]} = {dp[i]}")


def test_climb_stairs():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "n": 2,
            "expected": 2,
            "description": "Two stairs"
        },
        {
            "n": 3,
            "expected": 3,
            "description": "Three stairs"
        },
        {
            "n": 4,
            "expected": 5,
            "description": "Four stairs"
        },
        {
            "n": 1,
            "expected": 1,
            "description": "One stair"
        },
        {
            "n": 5,
            "expected": 8,
            "description": "Five stairs"
        },
        {
            "n": 6,
            "expected": 13,
            "description": "Six stairs"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        n = test_case["n"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: n = {n}")

        result = solution.climbStairs(n)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_climb_stairs()
        print("\nAll test cases passed successfully! 🎉")

        # Explain and visualize with detailed examples
        explain_dp_climbing_stairs(4)
        visualize_dp_solution(5)
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
