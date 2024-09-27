from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)  # Count characters in s
        count_t = Counter(t)  # Count characters in t

        # Find the character that appears one more time in t
        for char in count_t:
            if count_t[char] != count_s.get(char, 0):
                return char
