class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Concatenate the string with itself
        doubled_s = s + s

        # Check if the original string is in the doubled string, excluding the first and last characters
        return s in doubled_s[1:-1]
