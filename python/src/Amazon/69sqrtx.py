"""
LeetCode 69. Sqrt(x)

Problem Statement:
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Constraints:
- 0 <= x <= 2^31 - 1
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1

        return right


def explain_sqrt(x: int) -> None:
    """
    Function to explain the square root calculation process step by step
    """
    print(f"\nCalculating square root of {x}")
    print("=" * 50)

    if x < 2:
        print(f"Input {x} is less than 2, returning {x}")
        return x

    left, right = 1, x // 2
    print(f"Initial search range: [{left}, {right}]")

    iteration = 1
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        print(f"\nIteration {iteration}:")
        print(f"Current range: [{left}, {right}]")
        print(f"Middle value: {mid}")
        print(f"Square of middle value: {square}")

        if square == x:
            print(f"Found exact square root: {mid}")
            return mid
        elif square < x:
            print(f"Square is too small, searching in upper half")
            left = mid + 1
        else:
            print(f"Square is too large, searching in lower half")
            right = mid - 1

        iteration += 1

    print(f"\nFinal result (rounded down): {right}")
    return right


def test_sqrt():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "x": 4,
            "expected": 2,
            "description": "Perfect square"
        },
        {
            "x": 8,
            "expected": 2,
            "description": "Non-perfect square"
        },
        {
            "x": 0,
            "expected": 0,
            "description": "Zero input"
        },
        {
            "x": 1,
            "expected": 1,
            "description": "Input of one"
        },
        {
            "x": 16,
            "expected": 4,
            "description": "Larger perfect square"
        },
        {
            "x": 2147395600,
            "expected": 46340,
            "description": "Large input"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        x = test_case["x"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: x = {x}")

        result = solution.mySqrt(x)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_sqrt()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_sqrt(4)
        explain_sqrt(8)
        explain_sqrt(16)
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
