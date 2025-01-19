"""
LeetCode 20. Valid Parentheses

Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
- 1 <= s.length <= 104
- s consists of parentheses only '()[]{}'

Approach:
1. Use a stack to keep track of opening brackets
2. For each closing bracket, check if it matches the last opening bracket
3. Stack should be empty at the end for valid string
4. Time Complexity: O(n)
5. Space Complexity: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Dictionary to hold matching pairs of parentheses
        mapping = {")": "(", "}": "{", "]": "["}

        # Iterate over each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop the top element from the stack (if it exists)
                top_element = stack.pop() if stack else '#'

                # If the popped element doesn't match the corresponding opening bracket
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all brackets were matched
        return not stack


def test_valid_parentheses():
    """
    Test function to verify the isValid solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "input": "()",
            "expected": True,
            "description": "Simple valid case with single pair"
        },
        {
            "input": "()[]{}",
            "expected": True,
            "description": "Valid case with multiple different pairs"
        },
        {
            "input": "(]",
            "expected": False,
            "description": "Invalid case with mismatched brackets"
        },
        {
            "input": "([)]",
            "expected": False,
            "description": "Invalid case with incorrect order"
        },
        {
            "input": "{[]}",
            "expected": True,
            "description": "Valid case with nested brackets"
        },
        {
            "input": "",
            "expected": True,
            "description": "Empty string case"
        },
        {
            "input": "(((",
            "expected": False,
            "description": "Unclosed brackets"
        },
        {
            "input": ")))",
            "expected": False,
            "description": "Extra closing brackets"
        },
        {
            "input": "({[]})",
            "expected": True,
            "description": "Complex nested valid case"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        input_str = test_case["input"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: s='{input_str}'")

        result = solution.isValid(input_str)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_valid_parentheses()
        print("\nAll test cases passed successfully! 🎉")
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
