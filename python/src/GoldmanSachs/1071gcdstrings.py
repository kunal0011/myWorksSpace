import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Helper function to check if a string can be constructed by repeating another string
        def canConstruct(s: str, t: str) -> bool:
            return s == t * (len(s) // len(t))

        # Find the greatest common divisor of lengths of the two strings
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        # Check if one string is a prefix of the other
        if str1 + str2 != str2 + str1:
            return ""

        # Compute the GCD of lengths
        gcd_len = gcd(len(str1), len(str2))

        # Return the substring that corresponds to the GCD length
        return str1[:gcd_len]
