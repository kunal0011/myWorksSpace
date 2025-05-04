"""
LeetCode 1813. Sentence Similarity III

Problem Statement:
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. 
For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
Two sentences sentence1 and sentence2 are similar if it is possible to insert an arbitrary number 
of words anywhere in sentence1 (possibly none) to make it equal to sentence2.
For example:
- sentence1 = "Hello my name is Jane" and sentence2 = "Hello Jane" are similar
- sentence1 = "My name is John" and sentence2 = "John my name" are not similar
Return true if sentence1 and sentence2 are similar, otherwise return false.

Time Complexity: O(min(n,m)) where n,m are lengths of sentences
Space Complexity: O(n+m) for storing word lists
"""

from typing import List


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Logic:
        # 1. Split sentences into words
        # 2. Compare words from both ends:
        #    - Match prefixes from start until mismatch
        #    - Match suffixes from end until mismatch
        # 3. If matched portions cover entire smaller sentence,
        #    then we can make sentences equal by inserting words

        words1 = sentence1.split()
        words2 = sentence2.split()

        i, j = 0, 0

        # Check prefix
        while i < len(words1) and i < len(words2) and words1[i] == words2[i]:
            i += 1

        # Check suffix
        while j < len(words1) and j < len(words2) and words1[-j-1] == words2[-j-1]:
            j += 1

        # If i + j covers the entire smaller sentence, then it's similar
        return i + j >= min(len(words1), len(words2))


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ("My name is Haley", "My Haley"),                    # Expected: True
        ("of", "A lot of words"),                            # Expected: True
        ("Eating right now", "Eating"),                      # Expected: True
        ("Luky", "Lucccky"),                                # Expected: False
        ("Hello my name is Jane", "Hello Jane"),             # Expected: True
        ("My name is John", "John my name"),                 # Expected: False
        ("A B C D", "A B"),                                  # Expected: True
        ("A B", "A C B")                                     # Expected: False
    ]

    for i, (s1, s2) in enumerate(test_cases):
        result = solution.areSentencesSimilar(s1, s2)
        print(f"Test case {i + 1}:")
        print(f"Sentence 1: '{s1}'")
        print(f"Sentence 2: '{s2}'")
        print(f"Are similar: {result}")
        if result:
            # Show matching parts
            words1, words2 = s1.split(), s2.split()
            matching = []
            j = 0
            while j < len(words1) and j < len(words2) and words1[j] == words2[j]:
                matching.append(words1[j])
                j += 1
            if matching:
                print(f"Matching prefix: {' '.join(matching)}")
            matching = []
            j = 1
            while j <= len(words1) and j <= len(words2) and words1[-j] == words2[-j]:
                matching.insert(0, words1[-j])
                j += 1
            if matching:
                print(f"Matching suffix: {' '.join(matching)}")
        print()
