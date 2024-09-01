class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        count = 0
        for word in words:
            # Check if the word is a prefix of the string s
            if s.startswith(word):
                count += 1
        return count
