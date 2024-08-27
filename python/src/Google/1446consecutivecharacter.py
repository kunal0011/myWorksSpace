class Solution:
    def maxPower(self, s: str) -> int:
        # Initialize max_len and current_len
        max_len = 1
        current_len = 1

        # Iterate over the string starting from the second character
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current_len += 1
            else:
                # Update the max_len and reset current_len
                max_len = max(max_len, current_len)
                current_len = 1

        # Final check to ensure we account for the last sequence
        return max(max_len, current_len)
