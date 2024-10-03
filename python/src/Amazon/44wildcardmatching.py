class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # DP table, dp[i][j] will be True if s[0..i-1] matches p[0..j-1]
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty string matches empty pattern
        dp[0][0] = True

        # Initialize first row (pattern matching empty string)
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]

# Test the Solution class


def test_solution():
    sol = Solution()

    # Test case 1
    assert sol.isMatch("aa", "a") == False

    # Test case 2
    assert sol.isMatch("aa", "*") == True

    # Test case 3
    assert sol.isMatch("cb", "?a") == False

    # Test case 4
    assert sol.isMatch("adceb", "*a*b") == True

    # Test case 5
    assert sol.isMatch("acdcb", "a*c?b") == False

    print("All test cases passed!")


# Run the tests
test_solution()
