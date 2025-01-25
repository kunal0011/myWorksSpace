"""
LeetCode 28. Find the Index of the First Occurrence in a String

Problem Statement:
Given two strings needle and haystack, return the index of the first occurrence of needle 
in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
- 1 <= haystack.length, needle.length <= 104
- haystack and needle consist of only lowercase English characters

Approach:
1. Use KMP (Knuth-Morris-Pratt) pattern matching algorithm
2. Build LPS (Longest Proper Prefix which is also Suffix) array
3. Use LPS to avoid unnecessary comparisons
4. Time Complexity: O(n + m) where n = len(haystack), m = len(needle)
5. Space Complexity: O(m) for LPS array
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # Build LPS array for KMP algorithm
        def build_lps(pattern):
            m = len(pattern)
            lps = [0] * m
            length = 0  # Length of previous longest prefix suffix

            i = 1
            while i < m:
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        # KMP search
        lps = build_lps(needle)
        i = 0  # Index for haystack
        j = 0  # Index for needle

        while i < len(haystack):
            if needle[j] == haystack[i]:
                i += 1
                j += 1

                if j == len(needle):
                    return i - j
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1


def test_str_str():
    """
    Test function to verify the strStr solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "haystack": "sadbutsad",
            "needle": "sad",
            "expected": 0,
            "description": "Pattern at the beginning"
        },
        {
            "haystack": "leetcode",
            "needle": "leeto",
            "expected": -1,
            "description": "Pattern not found"
        },
        {
            "haystack": "hello",
            "needle": "ll",
            "expected": 2,
            "description": "Pattern in the middle"
        },
        {
            "haystack": "aaaaa",
            "needle": "bba",
            "expected": -1,
            "description": "Pattern not present"
        },
        {
            "haystack": "mississippi",
            "needle": "issip",
            "expected": 4,
            "description": "Overlapping pattern"
        },
        {
            "haystack": "aaa",
            "needle": "aaaa",
            "expected": -1,
            "description": "Pattern longer than haystack"
        },
        {
            "haystack": "hello",
            "needle": "o",
            "expected": 4,
            "description": "Pattern at the end"
        },
        {
            "haystack": "abc",
            "needle": "abc",
            "expected": 0,
            "description": "Pattern equals haystack"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        haystack = test_case["haystack"]
        needle = test_case["needle"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: haystack = '{haystack}', needle = '{needle}'")

        result = solution.strStr(haystack, needle)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_str_str()
        print("\nAll test cases passed successfully! 🎉")
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
