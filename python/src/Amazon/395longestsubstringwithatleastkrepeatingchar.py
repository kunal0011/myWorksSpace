class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0 or len(s) < k:
            return 0

        # Count the frequency of each character in the string
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        # Find the first character that appears less than k times
        for char in freq:
            if freq[char] < k:
                # Split by the character and recursively solve for each substring
                return max(self.longestSubstring(substring, k) for substring in s.split(char))

        # If all characters appear at least k times, the whole string is valid
        return len(s)
