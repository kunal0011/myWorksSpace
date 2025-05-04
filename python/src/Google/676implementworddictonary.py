"""
LeetCode 676 - Implement Magic Dictionary

Problem Statement:
Design a data structure that supports adding new words and finding if a string matches any previously added string with exactly one character difference.
Implement the MagicDictionary class:
- MagicDictionary() Initializes the object.
- void buildDict(String[] dictionary) Sets the data structure with an array of distinct strings dictionary.
- bool search(String searchWord) Returns true if there is a string in the data structure that equals searchWord 
  after replacing exactly one character with another character, and false otherwise.

Logic:
1. Store dictionary words in a set for O(1) lookup
2. For each search:
   - Compare searchWord with each dictionary word of same length
   - Count character differences
   - Return true if exactly one difference found
   - Otherwise continue searching

Time Complexity:
- buildDict: O(n) where n is total length of all words
- search: O(n*k) where n is number of words and k is average word length

Space Complexity: O(n) for storing dictionary words
"""

from typing import List


class MagicDictionary:

    def __init__(self):
        self.words = set()

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = set(dictionary)

    def search(self, searchWord: str) -> bool:
        for word in self.words:
            if len(word) != len(searchWord):
                continue
            # Count the number of differences between the two words
            diff_count = 0
            for i in range(len(word)):
                if word[i] != searchWord[i]:
                    diff_count += 1
                if diff_count > 1:
                    break
            if diff_count == 1:
                return True
        return False


def test_magic_dictionary():
    test_cases = [
        {
            'dictionary': ["hello", "leetcode"],
            'searches': ["hello", "hhllo", "hell", "leetcoded"],
            'expected': [False, True, False, False],
            'description': "Basic test case"
        },
        {
            'dictionary': ["abc", "abd", "def"],
            'searches': ["abf", "abc", "acc"],
            'expected': [True, False, True],
            'description': "Multiple similar words"
        },
        {
            'dictionary': ["a"],
            'searches': ["a", "b", "ab"],
            'expected': [False, True, False],
            'description': "Single character words"
        },
        {
            'dictionary': ["hello", "world"],
            'searches': ["hallo", "hollo", "worl"],
            'expected': [True, True, False],
            'description': "Multiple character differences"
        }
    ]

    print("Testing Magic Dictionary Implementation:")
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest Case {i} ({test['description']}):")
        print(f"Dictionary: {test['dictionary']}")

        # Initialize and build dictionary
        magic_dict = MagicDictionary()
        magic_dict.buildDict(test['dictionary'])

        # Test each search word
        for word, expected in zip(test['searches'], test['expected']):
            result = magic_dict.search(word)
            print(f"Search '{word}': {result} (Expected: {expected})")
            print(f"Status: {'PASSED' if result == expected else 'FAILED'}")


if __name__ == "__main__":
    test_magic_dictionary()
