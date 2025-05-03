"""
LeetCode 521 - Longest Uncommon Subsequence I

Given two strings a and b, return the length of the longest uncommon subsequence between a and b.
If the longest uncommon subsequence does not exist, return -1.

An uncommon subsequence is a string that is a subsequence of one string but not the other.
A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.

Logic:
- If both strings are identical, there is no uncommon subsequence, return -1
- Otherwise, the longer string itself will be the longest uncommon subsequence
  because it cannot be a subsequence of the shorter string

Time Complexity: O(min(len(a), len(b))) for string comparison
Space Complexity: O(1)
"""


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        else:
            return max(len(a), len(b))


def run_test_cases():
    solution = Solution()
    test_cases = [
        ("aba", "cdc"),     # Expected: 3
        ("aaa", "bbb"),     # Expected: 3
        ("aaa", "aaa"),     # Expected: -1
        ("", "abc"),        # Expected: 3
        ("abc", ""),        # Expected: 3
        ("", ""),          # Expected: -1
    ]

    for a, b in test_cases:
        result = solution.findLUSlength(a, b)
        print(f'Input: a = "{a}", b = "{b}" -> Output: {result}')


if __name__ == "__main__":
    run_test_cases()
