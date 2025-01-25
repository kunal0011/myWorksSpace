"""
LeetCode 67. Add Binary

Problem Statement:
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
- 1 <= a.length, b.length <= 104
- a and b consist only of '0' or '1' characters
- Each string does not contain leading zeros except for the zero itself
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize result and carry
        result = []
        carry = 0

        # Get lengths and pad shorter string with zeros
        i = len(a) - 1
        j = len(b) - 1

        # Process both strings from right to left
        while i >= 0 or j >= 0 or carry:
            # Get current digits, use 0 if exhausted
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            # Calculate sum and new carry
            current_sum = digit_a + digit_b + carry
            carry = current_sum // 2
            digit = current_sum % 2

            # Add current digit to result
            result.append(str(digit))

            # Move pointers
            i -= 1
            j -= 1

        # Reverse and join result
        return ''.join(result[::-1])


def explain_binary_addition(a: str, b: str) -> None:
    """
    Function to explain the binary addition process step by step
    """
    print(f"\nAdding binary numbers:")
    print(f"  {a}")
    print(f"+ {b}")
    print("=" * max(len(a), len(b) + 2))

    result = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    # Print aligned numbers
    max_len = max(len(a), len(b))
    print("\nAligned numbers:")
    print(" " * (max_len - len(a)) + a)
    print(" " * (max_len - len(b)) + b)
    print("-" * max_len)

    while i >= 0 or j >= 0 or carry:
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0

        current_sum = digit_a + digit_b + carry
        carry = current_sum // 2
        digit = current_sum % 2

        print(f"\nPosition {max(i, j)}:")
        print(f"Digit from a: {digit_a}")
        print(f"Digit from b: {digit_b}")
        print(f"Carry in: {carry}")
        print(f"Sum: {current_sum}")
        print(f"New digit: {digit}")
        print(f"Carry out: {carry}")

        result.append(str(digit))
        i -= 1
        j -= 1

    final_result = ''.join(result[::-1])
    print("\nFinal result:")
    print(" " * (max_len - len(a)) + a)
    print(" " * (max_len - len(b)) + b)
    print("-" * max_len)
    print(final_result)

    return final_result


def test_add_binary():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "a": "11",
            "b": "1",
            "expected": "100",
            "description": "Basic case"
        },
        {
            "a": "1010",
            "b": "1011",
            "expected": "10101",
            "description": "Equal length strings"
        },
        {
            "a": "0",
            "b": "0",
            "expected": "0",
            "description": "Both zero"
        },
        {
            "a": "1111",
            "b": "1111",
            "expected": "11110",
            "description": "All ones"
        },
        {
            "a": "1",
            "b": "111",
            "expected": "1000",
            "description": "Different lengths"
        },
        {
            "a": "1010",
            "b": "0",
            "expected": "1010",
            "description": "Adding zero"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        a = test_case["a"]
        b = test_case["b"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: a = {a}, b = {b}")

        result = solution.addBinary(a, b)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_add_binary()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_binary_addition("11", "1")
        explain_binary_addition("1010", "1011")
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
