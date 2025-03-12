"""
LeetCode 438 - Find All Anagrams in a String

Problem Statement:
-----------------
Given two strings s and p, return an array of all the start indices of p's anagrams in s.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Key Points:
----------
1. Need to find all anagrams of p in s
2. Uses sliding window technique with character frequency counting
3. Window size is fixed (length of p)
4. Order of characters doesn't matter (anagram property)
5. Multiple anagrams may exist in s

Examples:
--------
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
- "cba" at index 0 is an anagram of "abc"
- "bac" at index 6 is an anagram of "abc"

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation: Each substring "ab", "ba", "ab" is an anagram of "ab"

Constraints:
-----------
* 1 <= s.length, p.length <= 3 * 10^4
* s and p consist of lowercase English letters
"""

from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Find all starting indices of anagrams of p in s using sliding window.
        
        Algorithm:
        1. Create frequency map for pattern p
        2. Use sliding window of size len(p) to check anagrams
        3. Maintain frequency map of current window
        4. Compare window frequencies with pattern frequencies
        
        Time Complexity: O(n) where n is length of string s
        Space Complexity: O(k) where k is size of character set (26 for lowercase letters)
        """
        p_len = len(p)
        s_len = len(s)

        if p_len > s_len:
            return []

        # Create frequency maps
        p_count = Counter(p)
        s_count = Counter(s[:p_len - 1])
        result = []

        # Slide window and check for anagrams
        for i in range(p_len - 1, s_len):
            # Add current character to window
            s_count[s[i]] += 1

            # If frequencies match, we found an anagram
            if s_count == p_count:
                result.append(i - p_len + 1)

            # Remove leftmost character of window
            s_count[s[i - p_len + 1]] -= 1
            if s_count[s[i - p_len + 1]] == 0:
                del s_count[s[i - p_len + 1]]

        return result


def test_find_anagrams():
    """
    Test driver for finding all anagrams in a string
    """
    test_cases = [
        (
            "cbaebabacd", "abc",
            [0, 6]  # Basic case with multiple anagrams
        ),
        (
            "abab", "ab",
            [0, 1, 2]  # Overlapping anagrams
        ),
        (
            "hello", "oll",
            [2]  # Single anagram at end
        ),
        (
            "aaaaaaa", "aa",
            [0, 1, 2, 3, 4, 5]  # Multiple overlapping with same character
        ),
        (
            "abc", "def",
            []  # No anagrams found
        ),
        (
            "abc", "abcd",
            []  # Pattern longer than string
        ),
        (
            "aaabaaa", "aa",
            [0, 1, 4, 5]  # Multiple anagrams with gaps
        ),
        (
            "acdcaeccde", "cde",
            [6, 7]  # Complex case with multiple characters
        )
    ]
    
    solution = Solution()
    
    for i, (s, p, expected) in enumerate(test_cases, 1):
        result = solution.findAnagrams(s, p)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test case {i}: {status}")
        print(f"String: {s}")
        print(f"Pattern: {p}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print("-" * 40)

if __name__ == "__main__":
    test_find_anagrams()
