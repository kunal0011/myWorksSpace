class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Initialize a 2D DP array with dimensions (len(t) + 1) x (len(s) + 1)
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]

        # Base case: an empty t can be formed from any prefix of s
        for j in range(len(s) + 1):
            dp[0][j] = 1

        # Fill the DP table
        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                # If characters match, consider both including and excluding the character
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    # If characters don't match, exclude the character from s
                    dp[i][j] = dp[i][j - 1]

        # The answer is the number of ways to form t from all of s
        return dp[-1][-1]
