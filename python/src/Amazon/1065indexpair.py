class Solution:
    def indexPairs(self, text: str, words: list[str]) -> list[list[int]]:
        result = []

        # For each word in words, find its occurrences in the text
        for word in words:
            start = text.find(word)
            while start != -1:
                # Add the index pair [start, start + len(word) - 1]
                result.append([start, start + len(word) - 1])
                # Look for the next occurrence of the word
                start = text.find(word, start + 1)

        # Sort the result by the first index and then by the second index
        result.sort()
        return result
