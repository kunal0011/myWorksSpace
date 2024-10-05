class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # dp[i][j] will store the length of the longest palindromic subsequence in s[i:j+1]
        dp = [[0] * n for _ in range(n)]

        # Every single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1

        # Fill the dp table, starting with shorter substrings and expanding to longer ones
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    # Characters match, extend the subsequence
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # Try removing either end and take the maximum
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # The result is in the first row and last column (whole string)
        return dp[0][n - 1]
