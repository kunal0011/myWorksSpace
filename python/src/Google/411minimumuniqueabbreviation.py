"""
LeetCode 411 - Minimum Unique Word Abbreviation

A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths.
The length should have valid digits (1-9 and no leading zeros).

For example, a string such as "substitution" could be abbreviated as:
- "s10n" ("s ubstitutio n")
- "sub4u4" ("sub stit utio n")
- "12" ("substitution")
- "su3i1u2on" ("su bst i t u ti on")

Given a target string and a set of strings in a dictionary, find an abbreviation of the target string 
that is not an abbreviation of any string in the dictionary. Return the shortest possible abbreviation.

Example 1:
Input: target = "apple", dictionary = ["blade"]
Output: "a4"
Explanation: "a4" is the shortest abbreviation of "apple" that isn't an abbreviation of "blade".

Example 2:
Input: target = "apple", dictionary = ["plain", "amber", "blade"]
Output: "1p3"
Explanation: "ap3", "a3e", "2p2", "3le", "1p3" are all valid abbreviations of "apple", 
but "1p3" is the shortest that isn't an abbreviation of any dictionary word.
"""

from typing import List

class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        n = len(target)
        
        # Filter dictionary to keep only words of same length
        dictionary = [word for word in dictionary if len(word) == n]
        if not dictionary:
            return str(n)
        
        def abbr_len(mask: int) -> int:
            """Calculate length of abbreviation for given bit mask"""
            count = 0
            length = 0
            i = 0
            while i < n:
                if mask & (1 << i):
                    count = 0
                    length += 1
                else:
                    count += 1
                    if i == n - 1 or mask & (1 << (i + 1)):
                        length += len(str(count))
                i += 1
            return length
        
        def get_abbr(mask: int) -> str:
            """Generate abbreviation string from bit mask"""
            result = []
            count = 0
            for i in range(n):
                if mask & (1 << i):
                    if count > 0:
                        result.append(str(count))
                        count = 0
                    result.append(target[i])
                else:
                    count += 1
            if count > 0:
                result.append(str(count))
            return ''.join(result)
        
        def is_conflict(mask: int, word: str) -> bool:
            """Check if abbreviation conflicts with a dictionary word"""
            for i in range(n):
                if mask & (1 << i) and target[i] != word[i]:
                    return False
            return True
        
        # Generate all possible masks
        min_len = float('inf')
        best_mask = 0
        
        for mask in range(1 << n):
            # Skip if current abbreviation length is not shorter
            curr_len = abbr_len(mask)
            if curr_len >= min_len:
                continue
                
            # Check conflicts with dictionary words
            valid = True
            for word in dictionary:
                if is_conflict(mask, word):
                    valid = False
                    break
            
            if valid:
                min_len = curr_len
                best_mask = mask
        
        return get_abbr(best_mask)


# Test driver
def main():
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("apple", ["blade"]),                          # Should return "a4"
        ("apple", ["plain", "amber", "blade"]),        # Should return "1p3"
        ("apple", []),                                 # Should return "5"
        ("internationalization", ["international"]),    # Should return "i18n"
        ("python", ["ponder", "powers"]),              # Should return "py4"
    ]
    
    for target, dictionary in test_cases:
        result = solution.minAbbreviation(target, dictionary)
        print(f"\nInput: target = {target}, dictionary = {dictionary}")
        print(f"Output: {result}")


if __name__ == "__main__":
    main()