class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # If the string length is odd, it can never be a valid parentheses string.
        if len(s) % 2 != 0:
            return False

        # Left-to-right scan
        open_count = 0  # Tracks the balance between '(' and ')'
        # Tracks the number of flexible positions ('0' in locked)
        flexible_count = 0

        for i in range(len(s)):
            if locked[i] == '0':
                flexible_count += 1  # Treat flexible positions as '(' or ')'
            elif s[i] == '(':
                open_count += 1
            else:
                open_count -= 1

            if open_count < -flexible_count:
                return False

        # Right-to-left scan
        close_count = 0  # Tracks the balance between ')' and '('
        flexible_count = 0

        for i in range(len(s)-1, -1, -1):
            if locked[i] == '0':
                flexible_count += 1
            elif s[i] == ')':
                close_count += 1
            else:
                close_count -= 1

            if close_count < -flexible_count:
                return False

        return True


# Test case
sol = Solution()
s = "())()"
locked = "00000"
print(sol.canBeValid(s, locked))  # Expected output: True
