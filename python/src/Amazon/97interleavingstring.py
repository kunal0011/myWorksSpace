class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2, len3 = len(s1), len(s2), len(s3)

        if len1 + len2 != len3:
            return False

        dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]

        dp[0][0] = True

        # Fill the first row (s1 empty)
        for j in range(1, len2 + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        # Fill the first column (s2 empty)
        for i in range(1, len1 + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]

        # Fill the rest of the table
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]
                            ) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[len1][len2]
