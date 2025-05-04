"""
LeetCode 788: Rotated Digits

Problem Statement:
An integer x is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from x.
Each digit must be rotated - we cannot choose to leave it alone.
A number is valid if each digit remains a digit after rotation.
- 2, 5, 6, 9 rotate to a different digit
- 0, 1, 8 rotate to themselves
- 3, 4, 7 are invalid after rotation
Return the number of good integers in the range [1, n].

Logic:
1. We need two sets:
   - valid: digits that remain valid after rotation (0,1,2,5,6,8,9)
   - different: digits that change after rotation (2,5,6,9)
2. For each number from 1 to N:
   - Convert to string and check each digit
   - Must contain only valid digits (subset check)
   - Must contain at least one digit that changes (different set)
3. Count numbers that satisfy both conditions

Time Complexity: O(N * log N) since we process each number and its digits
Space Complexity: O(1) since sets are fixed size
"""

from typing import List


class Solution:
    def rotatedDigits(self, N: int) -> int:
        good_count = 0

        # Define the sets of digits
        valid = {'0', '1', '8', '2', '5', '6', '9'}
        different = {'2', '5', '6', '9'}

        # Iterate through each number from 1 to N
        for i in range(1, N + 1):
            s = str(i)
            if set(s).issubset(valid) and any(d in s for d in different):
                good_count += 1

        return good_count


def test_rotated_digits():
    solution = Solution()

    # Test case 1: Basic case
    n1 = 10
    result1 = solution.rotatedDigits(n1)
    assert result1 == 4, f"Test case 1 failed. Expected 4, got {result1}"
    print(f"Test case 1 passed: N={n1}, result={result1}")

    # Test case 2: Small number
    n2 = 2
    result2 = solution.rotatedDigits(n2)
    assert result2 == 1, f"Test case 2 failed. Expected 1, got {result2}"
    print(f"\nTest case 2 passed: N={n2}, result={result2}")

    # Test case 3: Contains invalid digits
    n3 = 20
    result3 = solution.rotatedDigits(n3)
    assert result3 == 9, f"Test case 3 failed. Expected 9, got {result3}"
    print(f"\nTest case 3 passed: N={n3}, result={result3}")

    # Test case 4: Single digit
    n4 = 1
    result4 = solution.rotatedDigits(n4)
    assert result4 == 0, f"Test case 4 failed. Expected 0, got {result4}"
    print(f"\nTest case 4 passed: N={n4}, result={result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_rotated_digits()
