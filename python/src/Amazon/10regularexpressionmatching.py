# Problem Statement:

# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Example 1:
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

# Example 3:
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".

# Constraints:

# 1 <= s.length <= 20
# 1 <= p.length <= 30
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # Create a DP table with default False values
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Base case: empty string and empty pattern are a match
        dp[0][0] = True

        # Fill in the DP table
        for j in range(2, n + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j -
                                     2] or (dp[i-1][j] and (p[j-2] == s[i-1] or p[j-2] == '.'))

        return dp[m][n]


def test_regex_matching():
    solution = Solution()

    # Test cases as tuples of (string, pattern, expected_result, description)
    test_cases = [
        ("aa", "a", False, "Basic matching - should fail"),
        ("aa", "a*", True, "Star operator - zero or more 'a's"),
        ("ab", ".*", True, "Dot-star combination - matches anything"),
        ("", "", True, "Empty string and pattern"),
        ("", "a*", True, "Empty string with star pattern"),
        ("aab", "c*a*b", True, "Complex pattern with multiple stars"),
        ("mississippi", "mis*is*ip*.", True, "Long string with mixed pattern"),
        ("ab", ".*c*", True, "Pattern ending with star"),
        ("aaa", "a*a", True, "Multiple characters with star"),
        ("a", "ab*", True, "Optional character with star"),
    ]

    # Run tests and collect results
    passed = 0
    total = len(test_cases)

    print("\nRunning Regular Expression Matching Tests:")
    print("=" * 50)

    for i, (s, p, expected, desc) in enumerate(test_cases, 1):
        result = solution.isMatch(s, p)
        status = "PASS" if result == expected else "FAIL"
        # Green for pass, Red for fail
        color = "\033[92m" if status == "PASS" else "\033[91m"

        print(f"\nTest Case {i}: {desc}")
        print(f"Input String: '{s}'")
        print(f"Pattern: '{p}'")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Status: {color}{status}\033[0m")

        if result == expected:
            passed += 1

    print("\n" + "=" * 50)
    print(f"\nTest Summary:")
    print(f"Total Tests: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {total - passed}")
    success_rate = (passed / total) * 100
    print(f"Success Rate: {success_rate:.2f}%")


if __name__ == "__main__":
    test_regex_matching()
