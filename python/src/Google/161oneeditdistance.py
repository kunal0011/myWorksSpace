class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        # Ensure that s is the shorter string
        if m > n:
            return self.isOneEditDistance(t, s)

        # If the length difference is more than 1, return False
        if n - m > 1:
            return False

        for i in range(m):
            if s[i] != t[i]:
                # Case 1: Replace character
                if m == n:
                    return s[i+1:] == t[i+1:]
                # Case 2: Insert character in s or remove character in t
                else:
                    return s[i:] == t[i+1:]

        # Case 3: If all previous characters are the same, the strings are one edit apart
        # only if the lengths differ by 1 (i.e., one extra character at the end of t)
        return m + 1 == n


# Example usage
solution = Solution()
s = "abc"
t = "ab"
print(solution.isOneEditDistance(s, t))  # Output: True
