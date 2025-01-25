"""
LeetCode 97. Interleaving String

Problem Statement:
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
substrings respectively, such that:
- s = s1 + s2 + ... + sn
- t = t1 + t2 + ... + tm
- |n - m| <= 1
- The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c"
Split s2 into s2 = "dbbc" + "a"
Interleaving the two splits: "aa" + "dbbc" + "bc" + "a" + "c"

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Constraints:
- 0 <= s1.length, s2.length <= 100
- 0 <= s3.length <= 200
- s1, s2, and s3 consist of lowercase English letters
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Check if lengths match
        if len(s1) + len(s2) != len(s3):
            return False

        # dp[i][j] represents if s3[0:i+j] can be formed by interleaving
        # s1[0:i] and s2[0:j]
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        # Empty strings case
        dp[0][0] = True

        # Initialize first row (using only s2)
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        # Initialize first column (using only s1)
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]

        # Fill the dp table
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                # Current position in s3
                k = i + j - 1
                # Can use either s1[i-1] or s2[j-1] if they match s3[k]
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[k]) or \
                    (dp[i][j-1] and s2[j-1] == s3[k])

        return dp[len(s1)][len(s2)]


def visualize_dp_table(s1: str, s2: str, s3: str, dp: list[list[bool]]) -> None:
    """Helper function to visualize the DP table"""
    print("\nDP Table:")
    print("   ", end="")
    print("  ε", end="")
    for c in s2:
        print(f"  {c}", end="")
    print("\nε", end="")

    for j in range(len(s2) + 1):
        print(f" {dp[0][j]:^2}", end="")
    print()

    for i in range(1, len(s1) + 1):
        print(s1[i-1], end="")
        for j in range(len(s2) + 1):
            print(f" {dp[i][j]:^2}", end="")
        print()


def test_is_interleave():
    solution = Solution()

    test_cases = [
        {
            "s1": "aabcc",
            "s2": "dbbca",
            "s3": "aadbbcbcac",
            "expected": True,
            "description": "Valid interleaving"
        },
        {
            "s1": "aabcc",
            "s2": "dbbca",
            "s3": "aadbbbaccc",
            "expected": False,
            "description": "Invalid interleaving"
        },
        {
            "s1": "",
            "s2": "",
            "s3": "",
            "expected": True,
            "description": "Empty strings"
        },
        {
            "s1": "a",
            "s2": "",
            "s3": "a",
            "expected": True,
            "description": "One empty string"
        },
        {
            "s1": "abc",
            "s2": "def",
            "s3": "abcdef",
            "expected": True,
            "description": "Sequential interleaving"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        s1 = test_case["s1"]
        s2 = test_case["s2"]
        s3 = test_case["s3"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"s1 = '{s1}'")
        print(f"s2 = '{s2}'")
        print(f"s3 = '{s3}'")

        # Create DP table for visualization
        if len(s1) <= 5 and len(s2) <= 5:  # Only show for small inputs
            dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
            # Fill DP table (same logic as solution)
            dp[0][0] = True
            for j in range(1, len(s2) + 1):
                dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
            for i in range(1, len(s1) + 1):
                dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
            for i in range(1, len(s1) + 1):
                for j in range(1, len(s2) + 1):
                    k = i + j - 1
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[k]) or \
                        (dp[i][j-1] and s2[j-1] == s3[k])
            visualize_dp_table(s1, s2, s3, dp)

        result = solution.isInterleave(s1, s2, s3)

        assert result == expected, \
            f"Expected {expected}, but got {result}"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_is_interleave()
    print("\nAll test cases passed! 🎉")
