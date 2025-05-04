"""
LeetCode 1422: Maximum Score After Splitting a String

Problem Statement:
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings.
The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

Logic:
1. Basic Solution (O(n²)):
   - Try each possible split position
   - Count zeros in left part and ones in right part
   - Keep track of maximum score

2. Optimized Solution (O(n)):
   - First count total ones in string
   - Iterate through string once:
     * Keep track of zeros on left
     * Calculate ones on right by subtracting ones seen so far from total ones
     * Update max score if current split is better
   
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def maxScore(self, s: str) -> int:
        # Count total ones in string
        total_ones = s.count('1')

        # Initialize variables
        zeros_left = 0
        ones_seen = 0
        max_score = 0

        # Check each split position except the last character
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros_left += 1
            else:
                ones_seen += 1

            # Ones in right part = total ones - ones seen so far
            ones_right = total_ones - ones_seen
            max_score = max(max_score, zeros_left + ones_right)

        return max_score


def test_max_score():
    solution = Solution()

    # Test case 1: Basic case
    s1 = "011101"
    result1 = solution.maxScore(s1)
    assert result1 == 5, f"Test case 1 failed. Expected 5, got {result1}"
    print(f"Test case 1 passed: {result1}")

    # Test case 2: All zeros on left, all ones on right
    s2 = "00111"
    result2 = solution.maxScore(s2)
    assert result2 == 5, f"Test case 2 failed. Expected 5, got {result2}"
    print(f"\nTest case 2 passed: {result2}")

    # Test case 3: Minimum possible string
    s3 = "01"
    result3 = solution.maxScore(s3)
    assert result3 == 1, f"Test case 3 failed. Expected 1, got {result3}"
    print(f"\nTest case 3 passed: {result3}")

    # Test case 4: All ones except first character
    s4 = "0111"
    result4 = solution.maxScore(s4)
    assert result4 == 3, f"Test case 4 failed. Expected 3, got {result4}"
    print(f"\nTest case 4 passed: {result4}")

    # Test case 5: All zeros except last character
    s5 = "0001"
    result5 = solution.maxScore(s5)
    assert result5 == 4, f"Test case 5 failed. Expected 4, got {result5}"
    print(f"\nTest case 5 passed: {result5}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_max_score()
