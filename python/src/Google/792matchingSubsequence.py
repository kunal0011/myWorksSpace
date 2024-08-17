from collections import defaultdict, deque
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Create a dictionary to hold the words in the form of a deque
        waiting = defaultdict(deque)

        # Populate the dictionary with words, grouped by their first character
        for word in words:
            waiting[word[0]].append(word)

        # Result variable to count subsequences
        count = 0

        # Iterate over each character in the string s
        for char in s:
            # Get the deque of words that are waiting for this character
            current_words = waiting[char]
            # Reset the entry in the dictionary
            waiting[char] = deque()

            # Process each word
            while current_words:
                word = current_words.popleft()
                # Move to the next character in the word
                if len(word) == 1:
                    # If this is the last character, it means the whole word is a subsequence
                    count += 1
                else:
                    # Otherwise, move the remaining part of the word to the next bucket
                    waiting[word[1]].append(word[1:])

        return count
