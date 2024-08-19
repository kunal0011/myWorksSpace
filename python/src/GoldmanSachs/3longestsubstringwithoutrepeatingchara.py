class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # To store the last seen index of characters
        left = 0  # Left boundary of the window
        max_length = 0  # Maximum length of substring without repeating characters

        for right in range(len(s)):
            if s[right] in char_map:
                # Move the left boundary to the right of the last seen index
                left = max(left, char_map[s[right]] + 1)
            # Update the last seen index of the current character
            char_map[s[right]] = right
            # Calculate the length of the current window
            max_length = max(max_length, right - left + 1)

        return max_length
