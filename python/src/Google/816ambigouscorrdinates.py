"""
LeetCode 816: Ambiguous Coordinates

Problem Statement:
Given a string s that represents coordinates "(x, y)", where x and y can have digits separated by a decimal point.
We can add one comma and one decimal point (or neither) to each coordinate. Return all possible coordinates such that 
each component is valid. A valid number has at most one decimal point, with no leading zeros before the decimal point 
and no trailing zeros after it.

Logic:
1. Strip outer parentheses and split string into two parts for x and y coordinates
2. For each part, generate all valid numbers by:
   - Trying as integer if valid (no leading zeros except single 0)
   - Trying all possible decimal positions if valid (no leading/trailing zeros)
3. Combine all valid x and y pairs into final coordinates
4. Helper function get_valid_numbers handles number validation:
   - Checks for valid integers
   - Checks for valid decimals with proper formatting

Time Complexity: O(n^3) where n is the length of input string
Space Complexity: O(n^3) for storing all possible combinations
"""

from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        def get_valid_numbers(s: str) -> list[str]:
            n = len(s)
            results = []
            # Check if s can be a valid integer without decimal
            if s == "0" or s[0] != '0':
                results.append(s)
            # Check if s can be a valid float with decimal
            for i in range(1, n):
                left, right = s[:i], s[i:]
                if (left == "0" or left[0] != '0') and right[-1] != '0':
                    results.append(left + "." + right)
            return results

        s = s[1:-1]  # Strip out the outer parentheses
        n = len(s)
        result = []

        # Split s into two parts, left and right
        for i in range(1, n):
            left_candidates = get_valid_numbers(s[:i])
            right_candidates = get_valid_numbers(s[i:])
            # Combine valid left and right pairs
            for left in left_candidates:
                for right in right_candidates:
                    result.append(f"({left}, {right})")

        return result


def test_ambiguous_coordinates():
    solution = Solution()

    # Test case 1: Basic case
    s1 = "(123)"
    result1 = solution.ambiguousCoordinates(s1)
    expected1 = ["(1, 23)", "(1.2, 3)", "(12, 3)"]
    assert sorted(result1) == sorted(
        expected1), f"Test case 1 failed. Expected {expected1}, got {result1}"
    print(f"Test case 1 passed: s={s1}\nOutput: {result1}")

    # Test case 2: With zeros
    s2 = "(00011)"
    result2 = solution.ambiguousCoordinates(s2)
    expected2 = ["(0, 0.011)", "(0.001, 1)"]
    assert sorted(result2) == sorted(
        expected2), f"Test case 2 failed. Expected {expected2}, got {result2}"
    print(f"\nTest case 2 passed: s={s2}\nOutput: {result2}")

    # Test case 3: Single digits
    s3 = "(0123)"
    result3 = solution.ambiguousCoordinates(s3)
    expected3 = ["(0, 123)", "(0, 12.3)", "(0, 1.23)",
                 "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
    assert sorted(result3) == sorted(
        expected3), f"Test case 3 failed. Expected {expected3}, got {result3}"
    print(f"\nTest case 3 passed: s={s3}\nOutput: {result3}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_ambiguous_coordinates()
