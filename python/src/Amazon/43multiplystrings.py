"""
LeetCode 43. Multiply Strings

Problem Statement:
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, 
also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:
- 1 <= num1.length, num2.length <= 200
- num1 and num2 consist of digits only
- Both num1 and num2 do not contain any leading zero, except the number 0 itself
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # Initialize result array with zeros
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        # Multiply each digit and add to result
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Calculate product and positions
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1

                # Add to existing values
                total = mul + result[p2]

                # Update result array
                result[p2] = total % 10
                result[p1] += total // 10

        # Convert result to string, removing leading zeros
        result_str = ''.join(map(str, result)).lstrip('0')

        return result_str if result_str else "0"


def explain_multiplication(num1: str, num2: str) -> None:
    """
    Function to explain the string multiplication process step by step
    """
    print(f"\nMultiplying {num1} × {num2}")
    print("=" * 50)

    if num1 == "0" or num2 == "0":
        print("One number is 0, result is 0")
        return "0"

    m, n = len(num1), len(num2)
    result = [0] * (m + n)

    print("\nStep-by-step multiplication:")
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            # Show current digits being multiplied
            mul = int(num1[i]) * int(num2[j])
            p1, p2 = i + j, i + j + 1

            print(f"\nMultiplying {num1[i]} × {num2[j]} = {mul}")
            print(f"Positions: p1={p1}, p2={p2}")

            # Show current state
            print(f"Current result: {result}")

            # Calculate and show addition
            total = mul + result[p2]
            print(f"Adding to existing value: {mul} + {result[p2]} = {total}")

            # Update result
            result[p2] = total % 10
            result[p1] += total // 10
            print(f"After update: {result}")

    # Show final conversion
    result_str = ''.join(map(str, result)).lstrip('0')
    print(f"\nFinal result array: {result}")
    print(f"Final string result: {result_str if result_str else '0'}")

    return result_str if result_str else "0"


def test_multiply():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "num1": "2",
            "num2": "3",
            "expected": "6",
            "description": "Single digit multiplication"
        },
        {
            "num1": "123",
            "num2": "456",
            "expected": "56088",
            "description": "Multi-digit multiplication"
        },
        {
            "num1": "0",
            "num2": "0",
            "expected": "0",
            "description": "Zero multiplication"
        },
        {
            "num1": "9999",
            "num2": "9999",
            "expected": "99980001",
            "description": "Large numbers"
        },
        {
            "num1": "1",
            "num2": "1",
            "expected": "1",
            "description": "Unit multiplication"
        },
        {
            "num1": "99",
            "num2": "0",
            "expected": "0",
            "description": "Multiplication by zero"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        num1 = test_case["num1"]
        num2 = test_case["num2"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: num1 = {num1}, num2 = {num2}")

        result = solution.multiply(num1, num2)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_multiply()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_multiplication("123", "456")
        explain_multiplication("99", "99")
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
