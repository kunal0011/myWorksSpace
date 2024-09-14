class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        max_vowels = 0
        current_vowels = 0

        # Count vowels in the first window
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1

        max_vowels = current_vowels

        # Slide the window across the string
        for i in range(k, len(s)):
            # Remove the character going out of the window
            if s[i - k] in vowels:
                current_vowels -= 1
            # Add the character coming into the window
            if s[i] in vowels:
                current_vowels += 1

            # Update max vowels count
            max_vowels = max(max_vowels, current_vowels)

        return max_vowels
