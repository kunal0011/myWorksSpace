class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp[i][j] will represent the minimum amount of money needed to guarantee a win
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # Fill the DP table
        for length in range(2, n + 1):  # length of the range
            for i in range(1, n - length + 2):  # start of the range
                j = i + length - 1  # end of the range
                dp[i][j] = float('inf')  # Initialize with a large number

                # Try every possible guess in the range [i, j]
                for x in range(i, j):
                    cost = x + max(dp[i][x - 1], dp[x + 1][j])
                    dp[i][j] = min(dp[i][j], cost)

        # Return the minimum amount of money needed to guarantee a win for the range [1, n]
        return dp[1][n]
