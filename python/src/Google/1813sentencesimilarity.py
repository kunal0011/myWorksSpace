class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
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
