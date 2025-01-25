"""
LeetCode 50. Pow(x, n)

Problem Statement:
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25

Constraints:
- -100.0 < x < 100.0
- -2^31 <= n <= 2^31-1
- n is an integer
- -10^4 <= x^n <= 10^4
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle edge cases
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x

        # Use binary exponentiation
        # If n is even: x^n = (x^2)^(n/2)
        # If n is odd:  x^n = x * (x^2)^((n-1)/2)

        # Handle negative power
        if n < 0:
            x = 1/x
            n = -n

        # Calculate power using binary exponentiation
        result = 1
        current_product = x

        while n > 0:
            # If n is odd, multiply result with current_product
            if n % 2 == 1:
                result *= current_product
            # Square the current_product for next iteration
            current_product *= current_product
            # Integer division by 2
            n //= 2

        return result


def explain_power(x: float, n: int) -> None:
    """
    Function to explain the power calculation process step by step
    """
    print(f"\nCalculating {x}^{n}")
    print("=" * 50)

    if n == 0:
        print("n = 0, result is 1")
        return 1

    if n == 1:
        print("n = 1, result is x")
        return x

    if n == -1:
        print("n = -1, result is 1/x")
        return 1/x

    # Handle negative power
    original_n = n
    if n < 0:
        print(f"Negative power: converting to positive")
        print(f"x = 1/{x}, n = {-n}")
        x = 1/x
        n = -n

    print("\nUsing binary exponentiation:")
    result = 1
    current_product = x

    print(f"Initial state:")
    print(f"result = {result}")
    print(f"current_product = {current_product}")

    step = 1
    while n > 0:
        print(f"\nStep {step}:")
        print(f"n = {n}")

        if n % 2 == 1:
            prev_result = result
            result *= current_product
            print(
                f"n is odd, multiply result: {prev_result} * {current_product} = {result}")

        prev_product = current_product
        current_product *= current_product
        print(
            f"Square current_product: {prev_product} * {prev_product} = {current_product}")

        n //= 2
        print(f"Divide n by 2: {n}")
        step += 1

    print(f"\nFinal result for {x}^{original_n} = {result}")
    return result


def test_power():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "x": 2.00000,
            "n": 10,
            "expected": 1024.00000,
            "description": "Positive power"
        },
        {
            "x": 2.10000,
            "n": 3,
            "expected": 9.26100,
            "description": "Decimal base"
        },
        {
            "x": 2.00000,
            "n": -2,
            "expected": 0.25000,
            "description": "Negative power"
        },
        {
            "x": 1.00000,
            "n": 2147483647,
            "expected": 1.00000,
            "description": "Large power"
        },
        {
            "x": 0.00001,
            "n": 2147483647,
            "expected": 0.00000,
            "description": "Small base, large power"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        x = test_case["x"]
        n = test_case["n"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: x = {x}, n = {n}")

        result = solution.myPow(x, n)

        # Use approximate equality for floating point comparison
        assert abs(result - expected) < 1e-5, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_power()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_power(2.0, 10)
        explain_power(2.0, -2)
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
