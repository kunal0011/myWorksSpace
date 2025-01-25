"""
LeetCode 44. Wildcard Matching

Problem Statement:
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second character is 'a', which does not match 'b'.

Constraints:
- 0 <= s.length, p.length <= 2000
- s contains only lowercase English letters
- p contains only lowercase English letters, '?' or '*'
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Get lengths of string and pattern
        m, n = len(s), len(p)

        # Create DP table
        # dp[i][j] represents if s[0:i] matches p[0:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty pattern matches empty string
        dp[0][0] = True

        # Handle patterns starting with *
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # * can match current char or be empty
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    # Current characters match
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]


def explain_matching(s: str, p: str) -> None:
    """
    Function to explain the wildcard matching process step by step
    """
    print(f"\nMatching string '{s}' with pattern '{p}'")
    print("=" * 50)

    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    print("\nInitializing DP table:")
    print("- Empty pattern matches empty string")

    # Handle patterns starting with *
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
            print(
                f"- Pattern prefix '{p[:j]}' matching empty string: {dp[0][j]}")

    print("\nFilling DP table:")
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                print(
                    f"Position ({i},{j}): '*' matches '{s[i-1]}' or empty dp[i][j]={dp[i-1][j]} {dp[i][j-1]}")
            elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                print(
                    f"Position ({i},{j}): '{p[j-1]}' matches '{s[i-1]}' dp[i][j]={dp[i-1][j-1]}")
            print(
                f"Current state: s[:{i}]='{s[:i]}' matches p[:{j}]='{p[:j]}': {dp[i][j]}")

    print("\nFinal DP table:")
    for row in dp:
        print(row)

    print(f"\nResult: {dp[m][n]}")
    return dp[m][n]


def test_wildcard_matching():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "s": "aa",
            "p": "a",
            "expected": False,
            "description": "Basic non-matching case"
        },
        {
            "s": "aa",
            "p": "*",
            "expected": True,
            "description": "Single wildcard matching all"
        },
        {
            "s": "cb",
            "p": "?a",
            "expected": False,
            "description": "Question mark with mismatch"
        },
        {
            "s": "adceb",
            "p": "*a*b",
            "expected": True,
            "description": "Multiple wildcards"
        },
        {
            "s": "acdcb",
            "p": "a*c?b",
            "expected": False,
            "description": "Complex pattern with mismatch"
        },
        {
            "s": "",
            "p": "*",
            "expected": True,
            "description": "Empty string with wildcard"
        },
        {
            "s": "",
            "p": "",
            "expected": True,
            "description": "Empty string and pattern"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        s = test_case["s"]
        p = test_case["p"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: s = '{s}', p = '{p}'")

        result = solution.isMatch(s, p)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_wildcard_matching()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_matching("adceb", "*a*b")
        explain_matching("aa", "*")
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
