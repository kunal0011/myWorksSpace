"""
LeetCode 1249: Minimum Remove to Make Valid Parentheses

Problem Statement:
Given a string s of '(' , ')' and lowercase English characters.
Remove the minimum number of parentheses to make the input string valid.
A string is valid if it has equal number of opening and closing parentheses and every opening
parenthesis has a matching closing parenthesis.
Return any valid string after removing the minimum number of parentheses.

Logic:
1. Use stack to track indices of opening parentheses
2. Two-pass approach:
   - First pass: Remove unmatched closing parentheses
   - Keep track of opening parentheses indices in stack
   - Remove closing parentheses that have no matching opening
3. After first pass:
   - Any remaining indices in stack are unmatched opening parentheses
   - Add these to removal set
4. Build final string excluding characters at removal indices

Time Complexity: O(n) where n is length of string
Space Complexity: O(n) for stack and removal set
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # First pass to remove invalid closing parentheses
        stack = []
        to_remove = set()

        # Identify unmatched closing parentheses
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)

        # Add remaining unmatched opening parentheses to removal set
        to_remove.update(stack)

        # Build result string excluding characters in removal set
        return ''.join(char for i, char in enumerate(s) if i not in to_remove)


def test_min_remove_to_make_valid():
    solution = Solution()

    # Test case 1: Basic case
    s1 = "lee(t(c)o)de)"
    result1 = solution.minRemoveToMakeValid(s1)
    assert result1 == "lee(t(c)o)de", f"Test case 1 failed. Expected 'lee(t(c)o)de', got {result1}"
    print(f"Test case 1 passed: {s1} -> {result1}")

    # Test case 2: Unmatched opening parentheses
    s2 = "((("
    result2 = solution.minRemoveToMakeValid(s2)
    assert result2 == "", f"Test case 2 failed. Expected '', got {result2}"
    print(f"\nTest case 2 passed: {s2} -> {result2}")

    # Test case 3: Unmatched closing parentheses
    s3 = ")))"
    result3 = solution.minRemoveToMakeValid(s3)
    assert result3 == "", f"Test case 3 failed. Expected '', got {result3}"
    print(f"\nTest case 3 passed: {s3} -> {result3}")

    # Test case 4: Already valid string
    s4 = "a(b)c"
    result4 = solution.minRemoveToMakeValid(s4)
    assert result4 == "a(b)c", f"Test case 4 failed. Expected 'a(b)c', got {result4}"
    print(f"\nTest case 4 passed: {s4} -> {result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_min_remove_to_make_valid()
