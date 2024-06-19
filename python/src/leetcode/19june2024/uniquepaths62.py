class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        # Base cases
        dp[0][0] = 1  # Starting point

        # Fill the dp array
        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] += dp[i-1][j]  # Add paths from above
                if j > 0:
                    dp[i][j] += dp[i][j-1]  # Add paths from left

        return dp[m-1][n-1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 3))
