class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()  # Split the string into words
        if len(pattern) != len(words):  # If lengths differ, they can't match
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            if char in char_to_word:
                # Check if the current character maps to the same word
                if char_to_word[char] != word:
                    return False
            else:
                # Create a new mapping from character to word
                char_to_word[char] = word

            if word in word_to_char:
                # Check if the current word maps to the same character
                if word_to_char[word] != char:
                    return False
            else:
                # Create a new mapping from word to character
                word_to_char[word] = char

        return True
