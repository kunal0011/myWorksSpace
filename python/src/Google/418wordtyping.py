"""
LeetCode 418 - Sentence Screen Fitting

Given a rows x cols screen and a sentence represented as a list of strings, return the number 
of times the given sentence can be fitted on the screen.

A sentence can be fitted on the screen if:
- All words can be placed on the screen
- All words must be placed in the correct order
- There must be at least one space between adjacent words on the same line
- The last word on each line can be immediately followed by the first word on the next line

Example 1:
Input: sentence = ["hello","world"], rows = 2, cols = 8
Output: 1
Explanation:
hello---
world---
The character '-' signifies an empty space on the screen.

Example 2:
Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
Output: 2
Explanation:
a-bcd-
e-a---
bcd-e-
The character '-' signifies an empty space on the screen.
"""

from typing import List

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        # Combine sentence into a single string with spaces
        s = ' '.join(sentence) + ' '
        n = len(s)
        start = 0  # Position in the sentence string
        
        # For each row
        for i in range(rows):
            start += cols  # Move pointer by column width
            
            # If we land on a space, we can start next line
            if s[start % n] == ' ':
                start += 1
                continue
            
            # If we land in middle of a word, move backward to find last space
            while start > 0 and s[(start-1) % n] != ' ':
                start -= 1
        
        # Number of complete sentences is start divided by length of sentence string
        return start // n


# Test driver
def main():
    solution = Solution()
    
    # Test cases
    test_cases = [
        (["hello", "world"], 2, 8),              # Should return 1
        (["a", "bcd", "e"], 3, 6),               # Should return 2
        (["i", "had", "apple", "pie"], 4, 5),    # Should return 1
        (["a", "b", "c"], 3, 1),                 # Should return 1
        (["try", "to", "be", "better"], 10, 4),  # Should return 1
    ]
    
    for sentence, rows, cols in test_cases:
        result = solution.wordsTyping(sentence, rows, cols)
        print(f"\nInput: sentence = {sentence}, rows = {rows}, cols = {cols}")
        print(f"Output: {result}")


if __name__ == "__main__":
    main()