
class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        sorted_words = sorted(words, key=len)
        rearranged_sentence = ' '.join(sorted_words)
        return rearranged_sentence.capitalize()
