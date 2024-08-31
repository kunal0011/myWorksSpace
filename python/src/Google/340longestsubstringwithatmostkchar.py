class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or not s:
            return 0

        # Dictionary to store the count of characters in the current window
        char_count = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            # Add the current character to the dictionary
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            # If the number of distinct characters exceeds k, shrink the window
            while len(char_count) > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            # Update the maximum length of the substring
            max_len = max(max_len, right - left + 1)

        return max_len
