from typing import List

"""
LeetCode 66. Plus One

Problem Statement:
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123. Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321. Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9. Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Constraints:
- 1 <= digits.length <= 100
- 0 <= digits[i] <= 9
- digits does not contain any leading 0's
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # Start from the rightmost digit
        for i in range(n - 1, -1, -1):
            # If digit is less than 9, simply increment and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If digit is 9, set it to 0 and continue to next digit
            digits[i] = 0

        # If we're here, all digits were 9
        return [1] + digits


def explain_plus_one(digits: List[int]) -> None:
    """
    Function to explain the plus one process step by step
    """
    print(f"\nAdding one to number represented by: {digits}")
    print("=" * 50)

    print(f"Original number: {''.join(map(str, digits))}")

    n = len(digits)
    result = digits.copy()

    for i in range(n - 1, -1, -1):
        print(f"\nProcessing digit at position {i}: {result[i]}")

        if result[i] < 9:
            result[i] += 1
            print(f"Digit < 9, incrementing to {result[i]}")
            print(f"Final result: {result}")
            return result

        print(f"Digit is 9, setting to 0 and carrying over")
        result[i] = 0
        print(f"Current state: {result}")

    # If we get here, all digits were 9
    result = [1] + result
    print(f"\nAll digits were 9, adding leading 1")
    print(f"Final result: {result}")
    return result


def test_plus_one():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "digits": [1, 2, 3],
            "expected": [1, 2, 4],
            "description": "Basic case"
        },
        {
            "digits": [4, 3, 2, 1],
            "expected": [4, 3, 2, 2],
            "description": "Four digits"
        },
        {
            "digits": [9],
            "expected": [1, 0],
            "description": "Single 9"
        },
        {
            "digits": [9, 9, 9],
            "expected": [1, 0, 0, 0],
            "description": "All nines"
        },
        {
            "digits": [0],
            "expected": [1],
            "description": "Single zero"
        },
        {
            "digits": [1, 9, 9],
            "expected": [2, 0, 0],
            "description": "Multiple nines"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        digits = test_case["digits"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input digits: {digits}")

        result = solution.plusOne(digits.copy())

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")
        print(f"Result: {result}")


if __name__ == "__main__":
    try:
        test_plus_one()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_plus_one([1, 2, 3])
        explain_plus_one([9, 9, 9])
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
