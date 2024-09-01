class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_words = 0

        for sentence in sentences:
            words = sentence.split()
            max_words = max(max_words, len(words))

        return max_words
