class Solution:
    def encode(self, s: str) -> str:
        def get_encoded_length(s):
            n = len(s)
            dp = [[float('inf')] * n for _ in range(n)]

            for i in range(n):
                dp[i][i] = 1  # Single character case

            for length in range(2, n + 1):  # Substring lengths from 2 to n
                for i in range(n - length + 1):
                    j = i + length - 1
                    substring = s[i:j + 1]

                    # Check if the substring can be compressed
                    for k in range(1, length):
                        dp[i][j] = min(
                            dp[i][j], dp[i][i + k - 1] + dp[i + k][j])

                    # Check for encoding pattern k[substring]
                    for k in range(1, length // 2 + 1):
                        if length % k == 0:
                            repeat = substring[:k]
                            if repeat * (length // k) == substring:
                                dp[i][j] = min(dp[i][j], len(
                                    f"{length // k}[{dp[i][i + k - 1]}]"))

            return dp[0][n - 1]

        return get_encoded_length(s)
