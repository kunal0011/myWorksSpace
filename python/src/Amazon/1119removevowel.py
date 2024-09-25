class Solution:
    def removeVowels(self, s: str) -> str:
        # Define a set of vowels
        vowels = set('aeiouAEIOU')

        # Create a new string with only non-vowel characters
        result = [char for char in s if char not in vowels]

        # Join the characters to form the final string
        return ''.join(result)
