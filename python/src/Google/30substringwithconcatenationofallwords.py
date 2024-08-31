from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_length = len(words[0])
        num_words = len(words)
        substring_length = word_length * num_words

        # Create a frequency counter for the words
        word_count = Counter(words)
        result = []

        # Iterate over every possible starting position
        for i in range(word_length):
            left = i
            right = i
            current_count = Counter()

            while right + word_length <= len(s):
                # Extract the current word from the string
                word = s[right:right + word_length]

                # Move the right pointer to the next word
                right += word_length

                if word in word_count:
                    current_count[word] += 1

                    # If the count exceeds the expected count, move the left pointer
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_length]
                        current_count[left_word] -= 1
                        left += word_length

                    # Check if the current window matches the word count
                    if right - left == substring_length:
                        result.append(left)
                else:
                    # If the word is not in the list, reset the window
                    current_count.clear()
                    left = right

        return result
