"""
LeetCode 168. Excel Sheet Column Title

Problem Statement:
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 1:
Input: columnNumber = 1
Output: "A"

Example 2:
Input: columnNumber = 28
Output: "AB"

Example 3:
Input: columnNumber = 701
Output: "ZY"

Constraints:
- 1 <= columnNumber <= 2^31 - 1
"""

from typing import List, Tuple


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """
        Convert number to Excel column title.
        Time complexity: O(log n) where n is the column number
        Space complexity: O(1)
        """
        result = []

        while columnNumber > 0:
            # Subtract 1 because Excel column titles are 1-based
            columnNumber -= 1
            # Get remainder and convert to character
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26

        return ''.join(reversed(result))

    def convertToTitleWithSteps(self, columnNumber: int) -> Tuple[str, List[dict]]:
        """
        Convert number to Excel column title with detailed steps.
        Time complexity: O(log n)
        Space complexity: O(log n) for tracking steps
        """
        steps = []
        result = []
        original = columnNumber

        steps.append({
            "action": "Start",
            "number": columnNumber
        })

        while columnNumber > 0:
            # Subtract 1 for 1-based indexing
            columnNumber -= 1

            # Get character
            remainder = columnNumber % 26
            char = chr(remainder + ord('A'))
            result.append(char)

            steps.append({
                "action": "Process digit",
                "current_number": columnNumber,
                "remainder": remainder,
                "character": char,
                "current_result": ''.join(reversed(result))
            })

            # Update number
            columnNumber //= 26

        final_result = ''.join(reversed(result))
        steps.append({
            "action": "Final result",
            "input": original,
            "output": final_result
        })

        return final_result, steps


def visualize_steps(steps: List[dict]) -> None:
    """Helper function to visualize conversion steps."""
    print("\nConversion Steps:")
    for i, step in enumerate(steps, 1):
        print(f"\nStep {i}: {step['action']}")

        if step['action'] == "Start":
            print(f"Input number: {step['number']}")

        elif step['action'] == "Process digit":
            print(f"Current number: {step['current_number']}")
            print(f"Remainder: {step['remainder']}")
            print(f"Character: {step['character']}")
            print(f"Current result: {step['current_result']}")

        elif step['action'] == "Final result":
            print(f"Input: {step['input']}")
            print(f"Output: {step['output']}")


def test_convert_to_title():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "columnNumber": 1,
            "expected": "A",
            "description": "Single letter"
        },
        {
            "columnNumber": 28,
            "expected": "AB",
            "description": "Two letters"
        },
        {
            "columnNumber": 701,
            "expected": "ZY",
            "description": "End of alphabet"
        },
        {
            "columnNumber": 52,
            "expected": "AZ",
            "description": "First and last letters"
        },
        {
            "columnNumber": 1000,
            "expected": "ALL",
            "description": "Three letters"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print(f"Column number: {test_case['columnNumber']}")

        # Test both implementations
        result1 = solution.convertToTitle(test_case['columnNumber'])
        result2, steps = solution.convertToTitleWithSteps(
            test_case['columnNumber'])

        print(f"\nResults:")
        print(f"Column title: {result1}")

        visualize_steps(steps)

        assert result1 == test_case['expected'], \
            f"Basic approach failed. Expected {test_case['expected']}, got {result1}"
        assert result2 == test_case['expected'], \
            f"Step tracking failed. Expected {test_case['expected']}, got {result2}"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_convert_to_title()
