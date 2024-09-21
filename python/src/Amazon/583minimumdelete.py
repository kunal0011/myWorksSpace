class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # dp[i][j] will hold the length of LCS of word1[0:i] and word2[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Build the dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The number of deletions required is the sum of the lengths of the strings
        # minus twice the length of their LCS
        lcs_length = dp[m][n]
        return (m - lcs_length) + (n - lcs_length)


# Test case
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    word1 = "sea"
    word2 = "eat"
    print(sol.minDistance(word1, word2))  # Expected output: 2

    # Test case 2
    word1 = "leetcode"
    word2 = "etco"
    print(sol.minDistance(word1, word2))  # Expected output: 4
