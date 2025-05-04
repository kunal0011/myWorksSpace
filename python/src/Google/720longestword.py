"""
LeetCode 720: Longest Word in Dictionary

Problem Statement:
Given an array of strings words, return the longest word that can be built one character at a time by other words in the array.
If there is more than one possible answer, return the lexicographically smallest one.
If there is no answer, return an empty string.

Logic:
1. Sort the array lexicographically to handle the case of multiple possible answers
2. Use a set to keep track of buildable words, initialize with empty string
3. For each word, check if its prefix (word without last char) exists in set
4. If prefix exists, word can be built character by character, so add to set
5. Update longest word if current word is longer
6. Return the longest buildable word found

Time Complexity: O(nlogn) for sorting + O(n*k) for iteration where k is avg word length
Space Complexity: O(n*k) for storing words in set
"""

from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()  # Step 1: Sort words lexicographically
        # Step 2: Initialize a set with an empty string to help build valid words
        word_set = set([""])
        longest_word = ""

        for word in words:
            if word[:-1] in word_set:  # Step 3: Check if the prefix exists in the set
                word_set.add(word)  # If yes, add the word to the set
                # Step 4: Check if the current word is longer than the current longest word
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word


# Test cases
def test_longest_word():
    solution = Solution()

    # Test case 1: Basic case
    test1 = ["w", "wo", "wor", "worl", "world"]
    assert solution.longestWord(test1) == "world", "Test case 1 failed"
    print("Test case 1: Input:", test1)
    print("Output:", solution.longestWord(test1))

    # Test case 2: Multiple possible answers, return lexicographically smallest
    test2 = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    assert solution.longestWord(test2) == "apple", "Test case 2 failed"
    print("\nTest case 2: Input:", test2)
    print("Output:", solution.longestWord(test2))

    # Test case 3: No valid answer
    test3 = ["xyz", "xz", "z"]
    assert solution.longestWord(test3) == "", "Test case 3 failed"
    print("\nTest case 3: Input:", test3)
    print("Output:", solution.longestWord(test3))

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_longest_word()
