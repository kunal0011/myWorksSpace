class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string by whitespace and filter out empty strings
        words = s.split()

        # Reverse the list of words
        words.reverse()

        # Join the words into a single string with single space separator
        return ' '.join(words)
