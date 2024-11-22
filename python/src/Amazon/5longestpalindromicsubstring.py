# ### Problem Statement
# LeetCode Problem 5: Longest Palindromic Substring

# Given a string `s`, return the longest palindromic substring in `s`.

# ### Logic
# 1. **Expand Around Center**: The idea is to consider every character and every pair of consecutive characters as the center of a palindrome and expand around them as long as the characters on both sides are equal.
# 2. **Track Longest Palindrome**: Keep track of the longest palindrome found during the expansion process.
# 3. **Return Result**: Return the longest palindrome substring.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            # Odd length palindromes
            left1, right1 = expand_around_center(i, i)
            # Even length palindromes
            left2, right2 = expand_around_center(i, i + 1)

            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2

        return s[start:end + 1]


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ("babad", "bab"),  # "aba" is also a valid answer
        ("cbbd", "bb"),
        ("a", "a"),
        ("ac", "a"),  # "c" is also a valid answer
        ("", ""),
        ("racecar", "racecar"),
        ("abccba", "abccba"),
        ("forgeeksskeegfor", "geeksskeeg")
    ]

    for s, expected in test_cases:
        result = solution.longestPalindrome(s)
        print(f"Input: {s}\nOutput: {result}\nExpected: {expected}\n")
        assert result == expected or result == expected[::-
                                                        1], f"Test failed for input: {s}"

    print("All tests passed!")
