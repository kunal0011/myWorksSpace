
# The problem statement for LeetCode problem 3, "Longest Substring Without Repeating Characters," is as follows:

# Given a string

# s

# , find the length of the longest substring without repeating characters.

# ### Example 1:
# ```
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# ```

# ### Example 2:
# ```
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# ```

# ### Example 3:
# ```
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
# ```

# ### Constraints:
# - `0 <= s.length <= 5 * 10^4`
# -

# s

#  consists of English letters, digits, symbols, and spaces.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # Set to store characters in the current window
        left = 0  # Left pointer of the sliding window
        max_length = 0  # Result to store the maximum length of substring

        for right in range(len(s)):
            # Expand the window by including s[right]
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3)
    ]

    for s, expected in test_cases:
        result = sol.lengthOfLongestSubstring(s)
        print(f"Input: {s}, Expected: {expected}, Got: {result}")
        assert result == expected, f"Test failed for input: {s}"
