class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        if n == 0:
            return ""
        
        # Create a DP table
        dp = [[False] * n for _ in range(n)]
        
        # Initialize variables to track the longest palindrome
        start = 0
        max_length = 1
        
        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True
        
        # Check substrings of length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_length = 2
        
        # Check substrings of length greater than 2
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                # Check if the current substring is a palindrome
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    start = i
                    max_length = length
        
        return s[start:start + max_length]
    
    
class Solution1:
    def longestPalindrome(self, s: str) -> str:
            if not s:
                return ""

            start, end = 0, 0

            def expand_around_center(left, right):
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1
                return left + 1, right - 1

            for i in range(len(s)):
                # Odd length palindromes
                left1, right1 = expand_around_center(i, i)
                # Even length palindromes
                left2, right2 = expand_around_center(i, i + 1)

                if right1 - left1 > end - start:
                    start, end = left1, right1
                if right2 - left2 > end - start:
                    start, end = left2, right2

            return s[start:end + 1]
        
if __name__ == '__main__':
    s = Solution1()
    print(s.longestPalindrome('babad'))