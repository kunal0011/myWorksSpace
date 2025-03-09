"""
LeetCode 290 - Word Pattern

Problem Statement:
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern 
and a non-empty word in s.  q

Example:
pattern = "abba", s = "dog cat cat dog" -> true
pattern = "abba", s = "dog cat cat fish" -> false

Logic:
1. Use two dictionaries to maintain bidirectional mapping:
   - char_to_word: maps pattern chars to words
   - word_to_char: maps words to pattern chars
2. Check both mappings to ensure bijection:
   - Each char must map to unique word
   - Each word must map to unique char
3. Return false if any mismatch found
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()  # Split the string into words
        if len(pattern) != len(words):  # If lengths differ, they can't match
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            if char in char_to_word:
                # Check if the current character maps to the same word
                if char_to_word[char] != word:
                    return False
            else:
                # Create a new mapping from character to word
                char_to_word[char] = word

            if word in word_to_char:
                # Check if the current word maps to the same character
                if word_to_char[word] != char:
                    return False
            else:
                # Create a new mapping from word to character
                word_to_char[word] = char

        return True

def test_word_pattern():
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("abba", "dog cat cat dog", True),      # Standard matching pattern
        ("abba", "dog cat cat fish", False),    # Words don't match pattern
        ("aaaa", "dog dog dog dog", True),      # Same word repeated
        ("abba", "dog dog dog dog", False),     # Different pattern, same words
        ("abc", "dog cat", False),              # Length mismatch
        ("", "", True),                         # Empty strings
        ("jquery", "jquery", False)             # Single word doesn't match pattern
    ]
    
    for i, (pattern, s, expected) in enumerate(test_cases):
        result = solution.wordPattern(pattern, s)
        assert result == expected, f"Test case {i + 1} failed: pattern='{pattern}', s='{s}', expected {expected}, got {result}"
        print(f"Test case {i + 1} passed: pattern='{pattern}', s='{s}', result={result}")

if __name__ == "__main__":
    test_word_pattern()
    print("All test cases passed!")
