"""
LeetCode 131. Palindrome Partitioning

Problem Statement:
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Explanation:
- "a|a|b" produces ["a","a","b"]
- "aa|b" produces ["aa","b"]

Example 2:
Input: s = "a"
Output: [["a"]]

Example 3:
Input: s = "aabb"
Output: [["a","a","b","b"],["a","a","bb"],["aa","b","b"],["aa","bb"]]

Constraints:
- 1 <= s.length <= 16
- s contains only lowercase English letters
"""

from typing import List, Dict, Set
from collections import defaultdict


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Backtracking approach with palindrome memoization.
        Time: O(N * 2^N) where N is the length of string
        Space: O(N) for recursion stack
        """
        def is_palindrome(start: int, end: int) -> bool:
            """Check if substring s[start:end+1] is palindrome using memoization."""
            if (start, end) in palindrome_memo:
                return palindrome_memo[(start, end)]

            # Single character or empty string is palindrome
            if start >= end:
                palindrome_memo[(start, end)] = True
                return True

            # Check if outer characters match and inner substring is palindrome
            if s[start] == s[end] and is_palindrome(start + 1, end - 1):
                palindrome_memo[(start, end)] = True
                return True

            palindrome_memo[(start, end)] = False
            return False

        def backtrack(start: int, path: List[str]) -> None:
            """Backtracking function to find all palindrome partitions."""
            # If we reached end of string, we found a valid partition
            if start >= len(s):
                result.append(path[:])
                return

            # Try all possible substrings starting from current position
            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    # Add current palindrome substring to path
                    path.append(s[start:end + 1])
                    # Recursively partition remaining string
                    backtrack(end + 1, path)
                    # Backtrack by removing current substring
                    path.pop()

        result = []
        palindrome_memo = {}  # Memoization for palindrome checks
        backtrack(0, [])
        return result

    def partitionDP(self, s: str) -> List[List[str]]:
        """
        Dynamic Programming approach.
        Time: O(N * 2^N)
        Space: O(N^2) for DP table
        """
        n = len(s)
        # dp[i][j] indicates if s[i:j+1] is palindrome
        dp = [[False] * n for _ in range(n)]

        # All single characters are palindromes
        for i in range(n):
            dp[i][i] = True

        # Fill DP table for palindrome substrings
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                if length == 2:
                    dp[start][end] = s[start] == s[end]
                else:
                    dp[start][end] = s[start] == s[end] and dp[start + 1][end - 1]

        def generate_partitions(start: int) -> List[List[str]]:
            if start >= n:
                return [[]]

            partitions = []
            for end in range(start, n):
                if dp[start][end]:
                    for partition in generate_partitions(end + 1):
                        partitions.append([s[start:end + 1]] + partition)
            return partitions

        return generate_partitions(0)


def visualize_partition(partition: List[str]) -> str:
    """Helper function to visualize a partition with separators."""
    return " | ".join(partition)


def test_palindrome_partitioning():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "s": "aab",
            "expected": [["a", "a", "b"], ["aa", "b"]],
            "description": "Basic case"
        },
        {
            "s": "a",
            "expected": [["a"]],
            "description": "Single character"
        },
        {
            "s": "aabb",
            "expected": [["a", "a", "b", "b"], ["a", "a", "bb"], ["aa", "b", "b"], ["aa", "bb"]],
            "description": "Multiple palindromes"
        },
        {
            "s": "aba",
            "expected": [["a", "b", "a"], ["aba"]],
            "description": "Palindrome with odd length"
        },
        {
            "s": "abba",
            "expected": [["a", "b", "b", "a"], ["a", "bb", "a"], ["abba"]],
            "description": "Palindrome with even length"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print(f"Input string: {test_case['s']}")

        # Test both implementations
        result1 = solution.partition(test_case['s'])
        result2 = solution.partitionDP(test_case['s'])

        # Sort results for comparison
        result1.sort()
        result2.sort()
        expected = sorted(test_case['expected'])

        print("\nPartitions found:")
        for partition in result1:
            print(f"- {visualize_partition(partition)}")

        assert result1 == expected, \
            f"Backtracking approach failed. Expected {expected}, got {result1}"
        assert result2 == expected, \
            f"DP approach failed. Expected {expected}, got {result2}"

        print("✓ Test case passed!")

        # Additional statistics
        print(f"\nStatistics:")
        print(f"Number of partitions: {len(result1)}")
        print(f"Longest partition: {max(len(p) for p in result1)} parts")
        print(f"Shortest partition: {min(len(p) for p in result1)} parts")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_palindrome_partitioning()
