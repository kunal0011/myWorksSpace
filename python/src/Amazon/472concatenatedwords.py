"""
LeetCode 472 - Concatenated Words

Problem Statement:
-----------------
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Examples:
--------
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: 
- "catsdogcats" can be concatenated by "cats", "dog" and "cats"
- "dogcatsdog" can be concatenated by "dog", "cats" and "dog"
- "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat"

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]

Constraints:
-----------
* 1 <= words.length <= 10^4
* 1 <= words[i].length <= 30
* words[i] consists of only lowercase English letters
* All the strings of words are unique
* The sum of the length of all words[i] doesn't exceed 10^5
"""

from typing import List
from collections import defaultdict

class TrieNode:
    """Trie data structure for efficient word lookup"""
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        Find all concatenated words in the given list using Trie and DFS.
        
        Algorithm:
        1. Build a Trie with all words for efficient prefix matching
        2. For each word, try to break it into multiple valid words
        3. Use DFS with memoization to check if word can be formed
        
        Time Complexity: O(N * L^2) where N is number of words and L is max word length
        Space Complexity: O(N * L) for Trie storage and memoization
        """
        # Build Trie
        root = TrieNode()
        for word in words:
            if word:  # Skip empty strings
                node = root
                for char in word:
                    node = node.children[char]
                node.is_word = True
        
        def can_form(word: str, start: int, memo: set) -> bool:
            """
            Check if word[start:] can be formed by concatenating other words.
            Uses memoization to avoid redundant computations.
            """
            if start in memo:
                return False
                
            node = root
            for i in range(start, len(word)):
                if word[i] not in node.children:
                    memo.add(start)
                    return False
                    
                node = node.children[word[i]]
                if node.is_word:  # Found a valid word
                    if i == len(word) - 1:  # Reached end
                        return True
                    # Try to form rest of the word
                    if can_form(word, i + 1, memo):
                        return True
                        
            memo.add(start)
            return False
        
        # Find concatenated words
        result = []
        for word in words:
            if not word:  # Skip empty strings
                continue
                
            # Remove current word from Trie
            node = root
            for char in word:
                node = node.children[char]
            is_word = node.is_word
            node.is_word = False
            
            # Check if word can be formed by other words
            if len(word) > 0 and can_form(word, 0, set()):
                result.append(word)
                
            # Restore word in Trie
            node.is_word = is_word
            
        return result


def test_concatenated_words():
    """
    Test driver for concatenated words problem
    """
    test_cases = [
        (
            ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"],
            ["catsdogcats","dogcatsdog","ratcatdogcat"],
            "Basic test case with multiple concatenated words"
        ),
        (
            ["cat","dog","catdog"],
            ["catdog"],
            "Simple case with one concatenated word"
        ),
        (
            ["cat","cats","dog","dogcat"],
            ["dogcat"],
            "Case with similar prefixes"
        ),
        (
            [],
            [],
            "Empty input array"
        ),
        (
            ["a", "b", "ab", "abc"],
            ["ab"],
            "Case with short words"
        ),
        (
            ["a","aa","aaa","aaaa"],
            ["aa","aaa","aaaa"],
            "Case with repeated character words"
        ),
        (
            ["cat","cats","dog","dogcat","catdog","dogcatdog"],
            ["catdog","dogcat","dogcatdog"],
            "Complex case with multiple possible combinations"
        ),
        (
            ["a"],
            [],
            "Single word case"
        )
    ]
    
    solution = Solution()
    
    for i, (words, expected, description) in enumerate(test_cases, 1):
        result = solution.findAllConcatenatedWordsInADict(words)
        # Sort both lists for comparison since order doesn't matter
        result.sort()
        expected.sort()
        status = "PASSED" if result == expected else "FAILED"
        print(f"\nTest case {i}: {status}")
        print(f"Description: {description}")
        print(f"Input words: {words}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        if result != expected:
            print(f"Note: Check word concatenation logic")
        print("-" * 40)

if __name__ == "__main__":
    test_concatenated_words()
