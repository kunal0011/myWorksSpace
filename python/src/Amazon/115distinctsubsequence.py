"""
LeetCode 115. Distinct Subsequences

Problem Statement:
Given two strings s and t, return the number of distinct subsequences of s which equals t.
A subsequence of a string is a new string formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters.

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
The three distinct subsequences are:
- "ra_bbit" (remove first 'b')
- "rab_bit" (remove second 'b')
- "rabb_it" (remove third 'b')

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
The five distinct subsequences are:
- "ba_g__g"
- "ba__bag"
- "b__gbag"
- "_abgbag"
- "_ab_bag"

Constraints:
- 1 <= s.length, t.length <= 1000
- s and t consist of English letters.
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        2D Dynamic Programming solution.
        Time: O(mn), Space: O(mn) where m = len(s), n = len(t)
        """
        # Initialize a 2D DP array with dimensions (len(t) + 1) x (len(s) + 1)
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]

        # Base case: an empty t can be formed from any prefix of s
        for j in range(len(s) + 1):
            dp[0][j] = 1

        # Fill the DP table
        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                # If characters match, consider both including and excluding the character
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    # If characters don't match, exclude the character from s
                    dp[i][j] = dp[i][j - 1]

        # The answer is the number of ways to form t from all of s
        return dp[-1][-1]

    def numDistinctOptimized(self, s: str, t: str) -> int:
        """
        Space-optimized Dynamic Programming solution.
        Time: O(mn), Space: O(n) where m = len(s), n = len(t)
        """
        # We only need to keep track of one row at a time
        dp = [0] * (len(t) + 1)
        dp[0] = 1  # Base case: empty string matches empty string once

        # Process each character in s
        for j in range(1, len(s) + 1):
            prev = dp[0]  # Store the previous diagonal value
            for i in range(1, len(t) + 1):
                temp = dp[i]  # Store the current value before updating
                if t[i - 1] == s[j - 1]:
                    dp[i] = dp[i] + prev
                prev = temp  # Update prev for next iteration

        return dp[len(t)]

    def numDistinctRecursive(self, s: str, t: str) -> int:
        """
        Recursive solution with memoization.
        Time: O(mn), Space: O(mn) where m = len(s), n = len(t)
        """
        memo = {}

        def dfs(i: int, j: int) -> int:
            # Base cases
            if j == len(t):  # Found a valid subsequence
                return 1
            if i == len(s):  # Reached end of s without matching
                return 0
            if len(s) - i < len(t) - j:  # Not enough characters left
                return 0

            # Check memoization
            if (i, j) in memo:
                return memo[(i, j)]

            # Calculate result
            result = 0
            if s[i] == t[j]:
                # If characters match, try both including and excluding current char
                result = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                # If characters don't match, can only exclude current char
                result = dfs(i + 1, j)

            memo[(i, j)] = result
            return result

        return dfs(0, 0)


def test_distinct_subsequences():
    """Test function with various test cases"""
    solution = Solution()

    test_cases = [
        {
            "s": "rabbbit",
            "t": "rabbit",
            "expected": 3,
            "description": "Multiple overlapping subsequences"
        },
        {
            "s": "babgbag",
            "t": "bag",
            "expected": 5,
            "description": "Multiple non-overlapping subsequences"
        },
        {
            "s": "abc",
            "t": "abc",
            "expected": 1,
            "description": "Exact match"
        },
        {
            "s": "abc",
            "t": "def",
            "expected": 0,
            "description": "No match possible"
        },
        {
            "s": "",
            "t": "",
            "expected": 1,
            "description": "Empty strings"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        s = test_case["s"]
        t = test_case["t"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"s = '{s}'")
        print(f"t = '{t}'")

        # Test all three implementations
        result1 = solution.numDistinct(s, t)
        result2 = solution.numDistinctOptimized(s, t)
        result3 = solution.numDistinctRecursive(s, t)

        assert result1 == expected, f"2D DP: Expected {expected}, got {result1}"
        assert result2 == expected, f"Optimized DP: Expected {expected}, got {result2}"
        assert result3 == expected, f"Recursive: Expected {expected}, got {result3}"

        print(f"All implementations returned correct result: {result1}")
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_distinct_subsequences()
    print("\nAll test cases passed! 🎉")
