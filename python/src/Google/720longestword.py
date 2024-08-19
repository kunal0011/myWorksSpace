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


print(Solution().longestWord(["w", "wo", "wor", "worl", "world"]))
