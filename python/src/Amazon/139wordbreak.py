"""
LeetCode 139. Word Break

Problem Statement:
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a 
space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters
- All the strings of wordDict are unique
"""

from typing import List, Set, Dict, Tuple
from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Dynamic Programming approach.
        Time complexity: O(n^2 * k) where n is length of s, k is average word length
        Space complexity: O(n)
        """
        n = len(s)
        dp = [False] * (n + 1)  # dp[i] means s[:i] can be segmented
        dp[0] = True  # Empty string is always valid
        word_set = set(wordDict)  # For O(1) lookup

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]

    def wordBreakWithPath(self, s: str, wordDict: List[str]) -> Tuple[bool, List[str]]:
        """
        Returns both result and the valid segmentation if exists.
        Time complexity: O(n^2 * k)
        Space complexity: O(n)
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        word_set = set(wordDict)

        # Track the word that led to each valid position
        prev = [[] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    prev[i].append((j, s[j:i]))

        # Reconstruct the path if solution exists
        if not dp[n]:
            return False, []

        # BFS to find all valid segmentations
        paths = []
        queue = deque([(n, [])])

        while queue:
            pos, path = queue.popleft()
            if pos == 0:
                paths.append(path[::-1])
                continue

            for prev_pos, word in prev[pos]:
                queue.append((prev_pos, path + [word]))

        return True, paths


def visualize_segmentation(s: str, segmentation: List[str]) -> None:
    """Helper function to visualize word segmentation."""
    if not segmentation:
        print("No valid segmentation")
        return

    print("\nSegmentation visualization:")
    print(f"Original string: {s}")
    print("Segmented as:", " | ".join(segmentation))

    # Show character positions
    pos = 0
    print("\nPosition map:")
    for word in segmentation:
        end = pos + len(word)
        print(f"{word}: positions {pos}-{end-1}")
        pos = end


def test_word_break():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "s": "leetcode",
            "wordDict": ["leet", "code"],
            "expected": True,
            "description": "Basic case"
        },
        {
            "s": "applepenapple",
            "wordDict": ["apple", "pen"],
            "expected": True,
            "description": "Word reuse"
        },
        {
            "s": "catsandog",
            "wordDict": ["cats", "dog", "sand", "and", "cat"],
            "expected": False,
            "description": "Invalid segmentation"
        },
        {
            "s": "aaaaaaa",
            "wordDict": ["aaa", "aaaa"],
            "expected": True,
            "description": "Multiple valid segmentations"
        },
        {
            "s": "a",
            "wordDict": ["b"],
            "expected": False,
            "description": "Single character mismatch"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print(f"String: {test_case['s']}")
        print(f"Dictionary: {test_case['wordDict']}")

        # Test both implementations
        result1 = solution.wordBreak(test_case['s'], test_case['wordDict'])
        result2, paths = solution.wordBreakWithPath(
            test_case['s'], test_case['wordDict'])

        print(f"\nResults:")
        print(f"Can be segmented: {result1}")

        if result1:
            print("\nPossible segmentations:")
            for i, path in enumerate(paths, 1):
                print(f"Solution {i}:")
                visualize_segmentation(test_case['s'], path)

        assert result1 == test_case['expected'], \
            f"Basic approach failed. Expected {test_case['expected']}, got {result1}"
        assert result2 == test_case['expected'], \
            f"Path tracking failed. Expected {test_case['expected']}, got {result2}"

        # Verify segmentations if solution exists
        if result1:
            for path in paths:
                # Verify that concatenated words form the original string
                assert ''.join(path) == test_case['s'], \
                    f"Invalid segmentation: {''.join(path)} != {test_case['s']}"
                # Verify that all words are in dictionary
                assert all(word in test_case['wordDict'] for word in path), \
                    "Segmentation contains words not in dictionary"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_word_break()
