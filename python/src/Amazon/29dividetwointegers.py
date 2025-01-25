"""
LeetCode 29. Divide Two Integers

Problem Statement:
Given two integers dividend and divisor, divide two integers without using multiplication,
division, and mod operator. The integer division should truncate toward zero and return 
the quotient.

Note: Assume we are dealing with an environment that could only store integers within 
the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, if the quotient 
is strictly greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly 
less than -2^31, then return -2^31.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Constraints:
- -2^31 <= dividend, divisor <= 2^31 - 1
- divisor != 0

Approach:
1. Use bit manipulation and repeated subtraction
2. Optimize by using exponential search with left shift
3. Handle edge cases and signs separately
4. Time Complexity: O(log n)
5. Space Complexity: O(1)
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle special cases
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        # Handle overflow case
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # Get sign of result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Convert to positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp = divisor
            multiple = 1

            # Find largest multiple of divisor <= dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        # Apply sign and handle overflow
        result = sign * quotient
        return min(max(result, MIN_INT), MAX_INT)


def test_divide():
    """
    Test function to verify the divide solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "dividend": 10,
            "divisor": 3,
            "expected": 3,
            "description": "Basic positive division"
        },
        {
            "dividend": 7,
            "divisor": -3,
            "expected": -2,
            "description": "Division with negative divisor"
        },
        {
            "dividend": -7,
            "divisor": 3,
            "expected": -2,
            "description": "Division with negative dividend"
        },
        {
            "dividend": -2147483648,  # MIN_INT
            "divisor": -1,
            "expected": 2147483647,  # MAX_INT
            "description": "Overflow case"
        },
        {
            "dividend": 1,
            "divisor": 1,
            "expected": 1,
            "description": "Division by 1"
        },
        {
            "dividend": 0,
            "divisor": 1,
            "expected": 0,
            "description": "Zero dividend"
        },
        {
            "dividend": 2147483647,  # MAX_INT
            "divisor": 1,
            "expected": 2147483647,
            "description": "Maximum dividend"
        },
        {
            "dividend": 2147483647,  # MAX_INT
            "divisor": 2,
            "expected": 1073741823,
            "description": "Large number division"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        dividend = test_case["dividend"]
        divisor = test_case["divisor"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: dividend = {dividend}, divisor = {divisor}")

        result = solution.divide(dividend, divisor)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_divide()
        print("\nAll test cases passed successfully! 🎉")
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
