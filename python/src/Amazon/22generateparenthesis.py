from typing import List

"""
LeetCode 22. Generate Parentheses

Problem Statement:
Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
- 1 <= n <= 8

Approach:
1. Use backtracking with two parameters:
   - open: count of opening brackets used
   - close: count of closing brackets used
2. Add opening bracket if open < n
3. Add closing bracket if close < open
4. Base case: when string length equals 2*n
5. Time Complexity: O(4^n / sqrt(n)) - nth Catalan number
6. Space Complexity: O(n) for recursion stack
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(open_count: int, close_count: int, current: str, result: List[str]):
            # Base case: if current string length is 2*n, we have a valid combination
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add opening parenthesis if we still have some left
            if open_count < n:
                backtrack(open_count + 1, close_count, current + "(", result)

            # Add closing parenthesis if it's valid (more open than closed)
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current + ")", result)

        result = []
        backtrack(0, 0, "", result)
        return result


def test_generate_parenthesis():
    """
    Test function to verify the generateParenthesis solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "input": 1,
            "expected": ["()"],
            "description": "Single pair"
        },
        {
            "input": 2,
            "expected": ["(())", "()()"],
            "description": "Two pairs"
        },
        {
            "input": 3,
            "expected": ["((()))", "(()())", "(())()", "()(())", "()()()"],
            "description": "Three pairs"
        },
        {
            "input": 4,
            "expected": [
                "(((())))", "((()()))", "((())())", "((()))()", "(()(()))",
                "(()()())", "(()())()", "(())(())", "(())()()", "()((()))",
                "()(()())", "()(())()", "()()(())", "()()()()"
            ],
            "description": "Four pairs"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        n = test_case["input"]
        expected = sorted(test_case["expected"])
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: n={n}")

        result = sorted(solution.generateParenthesis(n))

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")
        print(f"Generated {len(result)} valid combinations")


if __name__ == "__main__":
    try:
        test_generate_parenthesis()
        print("\nAll test cases passed successfully! 🎉")
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
