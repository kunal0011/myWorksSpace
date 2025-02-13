"""
LeetCode 159. Longest Substring with At Most Two Distinct Characters

Problem Statement:
Given a string s, return the length of the longest substring that contains at most two distinct characters.

Example 1:
Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.

Example 2:
Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.

Constraints:
- 1 <= s.length <= 10^5
- s consists of English letters
"""

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1) - at most 3 characters in the hash map
        Uses sliding window with a character frequency map
        """
        if not s:
            return 0

        char_count = defaultdict(int)
        max_length = 0
        left = 0

        # Expand window to the right
        for right in range(len(s)):
            char_count[s[right]] += 1

            # Shrink window from left while we have more than 2 distinct chars
            while len(char_count) > 2:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            # Update max_length after window is valid
            max_length = max(max_length, right - left + 1)

        return max_length


def test_longest_substring_two_distinct():
    """Test function with various test cases."""
    solution = Solution()

    test_cases = [
        {
            "s": "eceba",
            "expected": 3,
            "description": "Basic case with substring 'ece'"
        },
        {
            "s": "ccaabbb",
            "expected": 5,
            "description": "Substring with consecutive characters"
        },
        {
            "s": "a",
            "expected": 1,
            "description": "Single character"
        },
        {
            "s": "aaa",
            "expected": 3,
            "description": "Same character repeated"
        },
        {
            "s": "abcabcabc",
            "expected": 2,
            "description": "Pattern repeated"
        },
        {
            "s": "aabbaaccbbaa",
            "expected": 4,
            "description": "Alternating pairs"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        result = solution.lengthOfLongestSubstringTwoDistinct(test_case["s"])
        assert result == test_case["expected"], \
            f'Test case {i} failed. Expected {test_case["expected"]}, got {result}'
        print(f'Test case {i} passed: {test_case["description"]}')

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_longest_substring_two_distinct()
