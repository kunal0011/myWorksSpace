class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # Create a set to store unique characters
        unique_chars = set(sentence)
        # Check if the number of unique characters is at least 26
        return len(unique_chars) >= 26
