"""
LeetCode 140. Word Break II

Problem Statement:
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence 
where each word is a valid dictionary word. Return all such possible sentences in any order.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple"]

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

Constraints:
- 1 <= s.length <= 20
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 10
- s and wordDict[i] consist of only lowercase English letters
- All the strings of wordDict are unique
"""

from typing import List, Dict, Set
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        Dynamic Programming with memoization approach.
        Time complexity: O(n * 2^n) in worst case
        Space complexity: O(n * 2^n) for storing all possible combinations
        """
        def backtrack(start: int) -> List[str]:
            # If we've seen this start position before, return cached results
            if start in memo:
                return memo[start]

            # If we've reached end of string, return empty list
            if start == len(s):
                return [""]

            results = []
            # Try all possible words that can start at current position
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    # Recursively solve for remaining string
                    sub_sentences = backtrack(end)
                    # Combine current word with all sub-solutions
                    for sub in sub_sentences:
                        results.append((word + " " + sub).strip())

            memo[start] = results
            return results

        word_set = set(wordDict)
        memo = {}  # Memoization cache
        return backtrack(0)

    def wordBreakTrie(self, s: str, wordDict: List[str]) -> List[str]:
        """
        Trie-based solution for efficient prefix matching.
        Time complexity: O(n * 2^n)
        Space complexity: O(n * 2^n)
        """
        # Build Trie
        trie = {}
        for word in wordDict:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['$'] = word  # Mark end of word

        def search_words(pos: int) -> List[str]:
            if pos in memo:
                return memo[pos]

            if pos == len(s):
                return [""]

            results = []
            node = trie
            for i in range(pos, len(s)):
                if s[i] not in node:
                    break
                node = node[s[i]]
                if '$' in node:  # Found a word
                    word = node['$']
                    sub_sentences = search_words(i + 1)
                    for sub in sub_sentences:
                        results.append((word + " " + sub).strip())

            memo[pos] = results
            return results

        memo = {}
        return search_words(0)


def visualize_sentence(sentence: str) -> None:
    """Helper function to visualize sentence structure."""
    print("\nSentence structure:")
    print(f"Complete: {sentence}")
    print("Words:", " | ".join(sentence.split()))
    print("Length:", len(sentence))
    print("Word count:", len(sentence.split()))


def test_word_break():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "s": "catsanddog",
            "wordDict": ["cat", "cats", "and", "sand", "dog"],
            "expected": ["cats and dog", "cat sand dog"],
            "description": "Multiple valid solutions"
        },
        {
            "s": "pineapplepenapple",
            "wordDict": ["apple", "pen", "applepen", "pine", "pineapple"],
            "expected": ["pine apple pen apple", "pineapple pen apple"],
            "description": "Overlapping words"
        },
        {
            "s": "catsandog",
            "wordDict": ["cats", "dog", "sand", "and", "cat"],
            "expected": [],
            "description": "No valid solutions"
        },
        {
            "s": "a",
            "wordDict": ["a"],
            "expected": ["a"],
            "description": "Single character"
        },
        {
            "s": "aaaa",
            "wordDict": ["a", "aa", "aaa"],
            "expected": ["a a a a", "a a aa", "a aa a", "aa a a", "aa aa", "aaa a", "a aaa"],
            "description": "Multiple overlapping solutions"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print(f"String: {test_case['s']}")
        print(f"Dictionary: {test_case['wordDict']}")

        # Test both implementations
        result1 = sorted(solution.wordBreak(
            test_case['s'], test_case['wordDict']))
        result2 = sorted(solution.wordBreakTrie(
            test_case['s'], test_case['wordDict']))
        expected = sorted(test_case['expected'])

        print(f"\nResults:")
        if result1:
            print(f"Found {len(result1)} valid sentences:")
            for j, sentence in enumerate(result1, 1):
                print(f"\nSolution {j}:")
                visualize_sentence(sentence)
        else:
            print("No valid sentences found")

        assert result1 == expected, \
            f"DP approach failed. Expected {expected}, got {result1}"
        assert result2 == expected, \
            f"Trie approach failed. Expected {expected}, got {result2}"

        # Verify solutions
        for sentence in result1:
            # Verify that all words are in dictionary
            words = sentence.split()
            assert all(word in test_case['wordDict'] for word in words), \
                f"Solution contains invalid words: {sentence}"
            # Verify that concatenated words form the original string
            assert ''.join(words) == test_case['s'], \
                f"Solution doesn't match original string: {sentence}"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_word_break()
