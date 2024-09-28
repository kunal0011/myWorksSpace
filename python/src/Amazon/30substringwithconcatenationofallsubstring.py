from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_length = len(words[0])
        num_words = len(words)
        total_length = word_length * num_words
        # Count the frequency of each word in the list
        word_count = Counter(words)

        result = []

        # Loop over all possible starting points (up to word_length)
        for i in range(word_length):
            left = i
            current_count = Counter()  # To count words in the current window
            count = 0  # Number of valid words in the current window

            # Slide the window over the string
            for right in range(i, len(s) - word_length + 1, word_length):
                # Extract the word at the current position
                word = s[right:right + word_length]

                if word in word_count:
                    current_count[word] += 1
                    count += 1

                    # If a word appears more times than it should, slide the window
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_length]
                        current_count[left_word] -= 1
                        count -= 1
                        left += word_length

                    # If we found a valid window, add the start index to the result
                    if count == num_words:
                        result.append(left)
                else:
                    # Reset if the word is not in words
                    current_count.clear()
                    count = 0
                    left = right + word_length

        return result
