class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        n = len(s)

        # Check missing types
        has_lower = any(c.islower() for c in s)
        has_upper = any(c.isupper() for c in s)
        has_digit = any(c.isdigit() for c in s)
        missing_types = 3 - (has_lower + has_upper + has_digit)

        # Check repeats and categorize them by length modulo 3
        change = 0
        one_mod = two_mod = 0
        i = 2

        while i < n:
            if s[i] == s[i-1] == s[i-2]:
                length = 2
                while i < n and s[i] == s[i-1]:
                    length += 1
                    i += 1
                if length % 3 == 0:
                    one_mod += 1
                elif length % 3 == 1:
                    two_mod += 1
                change += length // 3
            else:
                i += 1

        if n < 6:
            return max(missing_types, 6 - n)
        elif n <= 20:
            return max(missing_types, change)
        else:
            delete = n - 20
            change -= min(delete, one_mod * 1) // 1
            change -= min(max(delete - one_mod, 0), two_mod * 2) // 2
            change -= max(delete - one_mod - 2 * two_mod, 0) // 3
            return delete + max(missing_types, change)


# Example usage:
solution = Solution()
print(solution.strongPasswordChecker("a"))         # Output: 5
print(solution.strongPasswordChecker("aA1"))       # Output: 3
print(solution.strongPasswordChecker("1337C0d3"))  # Output: 0
