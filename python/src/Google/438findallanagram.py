from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str):
        p_len = len(p)
        s_len = len(s)

        if p_len > s_len:
            return []

        # Frequency map of string p
        p_count = Counter(p)

        # Frequency map of the first window in s
        s_count = Counter(s[:p_len - 1])

        result = []

        # Start sliding the window
        for i in range(p_len - 1, s_len):
            # Include the current character in the window
            s_count[s[i]] += 1

            # If the frequency maps are equal, add the starting index
            if s_count == p_count:
                result.append(i - p_len + 1)

            # Move the window: remove the character that is left out
            s_count[s[i - p_len + 1]] -= 1
            if s_count[s[i - p_len + 1]] == 0:
                del s_count[s[i - p_len + 1]]

        return result
