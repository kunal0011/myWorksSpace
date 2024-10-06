import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
    # Convert to lowercase
        s = s.lower()
        left = 0
        right = len(s)-1
        ispalin = True
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                ispalin = False
                return ispalin
        return ispalin
