"""
LeetCode 150. Evaluate Reverse Polish Notation

Problem Statement:
Evaluate the value of an arithmetic expression in Reverse Polish Notation (RPN).
Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
Division between two integers should truncate toward zero.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Constraints:
- 1 <= tokens.length <= 10^4
- tokens[i] is either an operator: "+", "-", "*", "/", or an integer in range [-200, 200]
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        stack = []
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            # Using int() for truncation toward zero
            '/': lambda x, y: int(x / y)
        }

        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                result = operators[token](a, b)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]


def test_eval_rpn():
    """Test function with various test cases."""
    solution = Solution()

    test_cases = [
        {
            "tokens": ["2", "1", "+", "3", "*"],
            "expected": 9,
            "description": "Basic addition and multiplication"
        },
        {
            "tokens": ["4", "13", "5", "/", "+"],
            "expected": 6,
            "description": "Division and addition"
        },
        {
            "tokens": ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
            "expected": 22,
            "description": "Complex expression"
        },
        {
            "tokens": ["3", "11", "+", "5", "-"],
            "expected": 9,
            "description": "Addition followed by subtraction"
        },
        {
            "tokens": ["15", "7", "/"],
            "expected": 2,
            "description": "Simple division with truncation"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        result = solution.evalRPN(test_case["tokens"])
        assert result == test_case["expected"], \
            f'Test case {i} failed. Expected {test_case["expected"]}, got {result}'
        print(f'Test case {i} passed: {test_case["description"]}')

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_eval_rpn()
