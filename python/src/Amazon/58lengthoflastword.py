class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Trim any trailing spaces
        s = s.strip()

        # Split the string into words by spaces
        words = s.split(' ')

        # Return the length of the last word
        return len(words[-1])
