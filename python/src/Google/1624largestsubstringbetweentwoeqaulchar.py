class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # Dictionary to store the first occurrence of each character
        first_occurrence = {}
        max_length = -1

        # Traverse the string
        for i, char in enumerate(s):
            # If the character has been seen before
            if char in first_occurrence:
                # Calculate the length of the substring between two equal characters
                current_length = i - first_occurrence[char] - 1
                # Update max_length if the current length is larger
                max_length = max(max_length, current_length)
            else:
                # Store the first occurrence of the character
                first_occurrence[char] = i

        return max_length
