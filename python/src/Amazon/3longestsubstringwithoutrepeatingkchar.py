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
