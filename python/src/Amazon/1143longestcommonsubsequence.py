class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        # Initialize a 2D dp array with all zeros
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The answer is in dp[m][n]
        return dp[m][n]

# Test the Solution class


def test_solution():
    sol = Solution()

    # Test case 1
    assert sol.longestCommonSubsequence("abcde", "ace") == 3

    # Test case 2
    assert sol.longestCommonSubsequence("abc", "abc") == 3

    # Test case 3
    assert sol.longestCommonSubsequence("abc", "def") == 0

    print("All test cases passed!")


# Run the tests
test_solution()
