class Solution:
    def numSquares(self, n: int) -> int:
        # Initialize DP array with a large number (infinity)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case: 0 can be represented as 0 perfect squares

        # List of all perfect squares less than or equal to n
        squares = [i * i for i in range(1, int(n**0.5) + 1)]

        # Fill the DP array
        for i in range(1, n + 1):
            for square in squares:
                if i >= square:
                    dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[n]
