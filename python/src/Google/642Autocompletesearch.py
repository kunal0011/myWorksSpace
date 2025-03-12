"""
LeetCode 642: Design Search Autocomplete System

Problem Statement:
Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#').

You are given a string array sentences and array times which contain historical data:
- sentences[i] is a previously typed sentence
- times[i] is the corresponding number of times the sentence was typed
Your system should suggest at most 3 historical hot sentences that have the same prefix as the part of sentence already typed.

Here are the specific rules:
1. The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
2. The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). 
   If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
3. If less than 3 hot sentences exist, return as many as you can.
4. When the input is a special character, it means the sentence ends, and you need to return an empty list.

Time Complexity:
- Constructor: O(N * L) where N is number of sentences and L is average length of sentence
- Input: O(N * L) where N is number of sentences and L is length of current search
Space Complexity: O(N * L) where N is number of sentences and L is average length of sentence
"""

from collections import defaultdict
import heapq
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.freq_map = defaultdict(int)


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.keyword = ""
        self.cur_node = self.root

        # Build the Trie
        for sentence, time in zip(sentences, times):
            self.add_sentence(sentence, time)

    def add_sentence(self, sentence: str, time: int):
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.freq_map[sentence] += time

    def search_top_3(self, node: TrieNode) -> List[str]:
        # Get all sentences with their frequencies and sort
        sentences = [(freq, sentence) for sentence, freq in node.freq_map.items()]
        # Sort by frequency (descending) and sentence (ascending)
        sentences.sort(key=lambda x: (-x[0], x[1]))
        return [sentence for _, sentence in sentences[:3]]

    def input(self, c: str) -> List[str]:
        if c == '#':
            # End of input, add the keyword to Trie
            self.add_sentence(self.keyword, 1)
            self.keyword = ""
            self.cur_node = self.root
            return []

        self.keyword += c

        if self.cur_node and c in self.cur_node.children:
            self.cur_node = self.cur_node.children[c]
            return self.search_top_3(self.cur_node)
        else:
            self.cur_node = None
            return []


def test_autocomplete_system():
    # Test Case 1: Basic functionality
    print("Test Case 1: Basic functionality")
    auto = AutocompleteSystem(
        ["i love you", "island", "iroman", "i love leetcode"], 
        [5, 3, 2, 2]
    )
    
    # Test input 'i'
    result = auto.input('i')
    expected = ["i love you", "island", "i love leetcode"]
    assert result == expected, f"Expected {expected}, but got {result}"
    print(f"Input 'i': {result}")
    
    # Test input ' '
    result = auto.input(' ')
    expected = ["i love you", "i love leetcode"]
    assert result == expected, f"Expected {expected}, but got {result}"
    print(f"Input ' ': {result}")
    
    # Test input 'a'
    result = auto.input('a')
    expected = []
    assert result == expected, f"Expected {expected}, but got {result}"
    print(f"Input 'a': {result}")
    
    # Test input '#'
    result = auto.input('#')
    expected = []
    assert result == expected, f"Expected {expected}, but got {result}"
    print(f"Input '#': {result}")
    
    # Test Case 2: New sentence frequency
    print("\nTest Case 2: New sentence frequency")
    result = auto.input('i')
    print(f"Input 'i' after adding 'i a': {result}")
    
    # Test Case 3: Empty system
    print("\nTest Case 3: Empty system")
    empty_auto = AutocompleteSystem([], [])
    result = empty_auto.input('a')
    assert result == [], "Empty system should return empty list"
    print(f"Input 'a' in empty system: {result}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_autocomplete_system()
