class Solution:
    def longestLine(self, mat):
        if not mat:
            return 0

        m, n = len(mat), len(mat[0])
        # DP array: dp[i][j][k] stores the longest line of 1s ending at (i, j) in direction k
        dp = [[[0] * 4 for _ in range(n)] for _ in range(m)]
        longest = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    # Horizontal
                    dp[i][j][0] = dp[i][j-1][0] + 1 if j > 0 else 1
                    # Vertical
                    dp[i][j][1] = dp[i-1][j][1] + 1 if i > 0 else 1
                    # Diagonal
                    dp[i][j][2] = dp[i-1][j-1][2] + 1 if i > 0 and j > 0 else 1
                    # Anti-diagonal
                    dp[i][j][3] = dp[i-1][j+1][3] + \
                        1 if i > 0 and j < n-1 else 1

                    # Update longest line found
                    longest = max(
                        longest, dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3])

        return longest
