"""
LeetCode 408 - Valid Word Abbreviation

A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths.
The length should have valid digits - no leading zeros.

For example:
- "substitution" could be abbreviated as:
  - "s10n" ("s ubstitutio n")
  - "sub4u4" ("sub stit utio n")
  - "12" ("substitution")
  - "su3i1u2on" ("su bst i t u ti on")

Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

Example 1:
Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n")

Example 2:
Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
"""

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0  # i for word, j for abbr
        
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                # Check for leading zero
                if abbr[j] == '0':
                    return False
                
                # Get the complete number
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                
                # Skip characters in word
                i += num
            else:
                # Compare characters
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        
        # Both strings should be exhausted
        return i == len(word) and j == len(abbr)


# Test driver
def main():
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("internationalization", "i12iz4n"),  # Should return True
        ("apple", "a2e"),                     # Should return False
        ("substitution", "s10n"),             # Should return True
        ("substitution", "sub4u4"),           # Should return True
        ("apple", "a3"),                      # Should return True
        ("apple", "05"),                      # Should return False
        ("hi", "2"),                          # Should return True
        ("hi", "1i"),                         # Should return True
    ]
    
    for word, abbr in test_cases:
        result = solution.validWordAbbreviation(word, abbr)
        print(f"\nInput: word = {word}, abbr = {abbr}")
        print(f"Output: {result}")


if __name__ == "__main__":
    main()