class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # There's one way to decode an empty string

        for i in range(1, n + 1):
            # Check the last one digit
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            # Check the last two digits
            if i > 1 and s[i-2:i] >= "10" and s[i-2:i] <= "26":
                dp[i] += dp[i-2]

        return dp[n]


s1 = Solution()
s = "11106"
print(f"The number of ways to decode '{s}' is: {s1.numDecodings(s)}")
