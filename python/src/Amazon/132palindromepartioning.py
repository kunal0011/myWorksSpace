"""
LeetCode 132. Palindrome Partitioning II

Problem Statement:
Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
Input: s = "a"
Output: 0
Explanation: The string is already a palindrome, no cuts needed.

Example 3:
Input: s = "ab"
Output: 1
Explanation: The palindrome partitioning ["a","b"] could be produced using 1 cut.

Constraints:
- 1 <= s.length <= 2000
- s consists of lowercase English letters only
"""

from typing import List, Tuple


class Solution:
    def minCut(self, s: str) -> int:
        """
        Dynamic Programming approach.
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        n = len(s)
        # dp[i][j] indicates if s[i:j+1] is palindrome
        is_palindrome = [[False] * n for _ in range(n)]

        # Initialize single characters as palindromes
        for i in range(n):
            is_palindrome[i][i] = True

        # Fill palindrome table
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                if length == 2:
                    is_palindrome[start][end] = s[start] == s[end]
                else:
                    is_palindrome[start][end] = (s[start] == s[end] and
                                                 is_palindrome[start + 1][end - 1])

        # dp[i] represents minimum cuts needed for s[0:i+1]
        dp = [0] * n

        for i in range(n):
            if is_palindrome[0][i]:
                dp[i] = 0
            else:
                # Initial value: worst case of i cuts
                dp[i] = i
                # Try all possible last cuts
                for j in range(i):
                    if is_palindrome[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)

        return dp[n - 1]

    def minCutWithPath(self, s: str) -> Tuple[int, List[str]]:
        """
        Returns both minimum cuts and the optimal partition.
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

        # Fill palindrome table
        for i in range(n):
            is_palindrome[i][i] = True
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                if length == 2:
                    is_palindrome[start][end] = s[start] == s[end]
                else:
                    is_palindrome[start][end] = (s[start] == s[end] and
                                                 is_palindrome[start + 1][end - 1])

        # dp[i] stores (min_cuts, last_cut_position)
        dp = [(i, -1) for i in range(n)]

        for i in range(n):
            if is_palindrome[0][i]:
                dp[i] = (0, -1)
            else:
                for j in range(i):
                    if is_palindrome[j + 1][i]:
                        if dp[j][0] + 1 < dp[i][0]:
                            dp[i] = (dp[j][0] + 1, j)

        # Reconstruct the partition
        cuts = []
        pos = n - 1
        while pos >= 0:
            last_cut = dp[pos][1]
            cuts.append(s[last_cut + 1:pos + 1])
            pos = last_cut

        return dp[n - 1][0], cuts[::-1]


def visualize_partition(s: str, cuts: List[int]) -> str:
    """Helper function to visualize partition with cuts."""
    result = list(s)
    for cut in sorted(cuts, reverse=True):
        result.insert(cut + 1, '|')
    return ''.join(result)


def test_palindrome_partitioning():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "s": "aab",
            "expected": 1,
            "description": "Basic case"
        },
        {
            "s": "a",
            "expected": 0,
            "description": "Single character"
        },
        {
            "s": "ab",
            "expected": 1,
            "description": "Two different characters"
        },
        {
            "s": "ababbbabbaba",
            "expected": 3,
            "description": "Longer string"
        },
        {
            "s": "aabaa",
            "expected": 1,
            "description": "Multiple palindromes"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print(f"Input string: {test_case['s']}")

        # Test both implementations
        result1 = solution.minCut(test_case['s'])
        min_cuts, partition = solution.minCutWithPath(test_case['s'])

        print(f"\nResults:")
        print(f"Minimum cuts needed: {result1}")
        print(f"Optimal partition: {' | '.join(partition)}")

        # Verify palindrome property
        all_palindromes = all(part == part[::-1] for part in partition)
        print(f"\nVerification:")
        print(f"All parts are palindromes: {all_palindromes}")
        print(f"Number of cuts matches: {len(partition) - 1 == result1}")

        assert result1 == test_case['expected'], \
            f"Basic approach failed. Expected {test_case['expected']}, got {result1}"
        assert min_cuts == test_case['expected'], \
            f"Path tracking failed. Expected {test_case['expected']}, got {min_cuts}"
        assert all_palindromes, "Not all parts are palindromes!"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_palindrome_partitioning()
