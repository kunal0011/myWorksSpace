"""
LeetCode 1002: Find Common Characters

Given a string array words, return an array of all characters that show up in all strings
within the words (including duplicates). You may return the answer in any order.

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists of lowercase English letters
"""

from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []
            
        # Start with frequencies of first word
        result = Counter(words[0])
        
        # Intersect with each subsequent word
        for word in words[1:]:
            result &= Counter(word)
            
        # Convert counter to list of characters
        return list(result.elements())

def validate_words(words: List[str]) -> bool:
    """Validate input according to constraints"""
    if not 1 <= len(words) <= 100:
        return False
    return all(1 <= len(w) <= 100 and w.islower() for w in words)

def visualize_frequencies(words: List[str], common: List[str]) -> None:
    """Create visual representation of character frequencies"""
    # Get frequency for each word
    freqs = [Counter(word) for word in words]
    all_chars = set(''.join(words))
    
    print("\nCharacter frequencies:")
    print("Char |", end=" ")
    for i in range(len(words)):
        print(f"Word{i:2d} |", end=" ")
    print("Common")
    print("-" * (7 + 8 * len(words) + 7))
    
    for char in sorted(all_chars):
        print(f"  {char}  |", end=" ")
        for freq in freqs:
            print(f"  {freq[char]:2d}  |", end=" ")
        print(f"  {Counter(common)[char]:2d}")

def test_common_chars():
    """Test function for Find Common Characters"""
    test_cases = [
        (["bella", "label", "roller"], ["e","l","l"]),
        (["cool", "lock", "cook"], ["c","o"]),
        (["hello", "world", "letter"], ["l","e"]),
        (["acabcddd", "bcbdbcbd", "baddbadb"], ["b","d"]),
        (["abc", "bcd", "cde"], ["c"])
    ]
    
    solution = Solution()
    
    for i, (words, expected) in enumerate(test_cases, 1):
        is_valid = validate_words(words)
        result = solution.commonChars(words)
        
        print(f"\nTest case {i}:")
        print(f"Input words: {words}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if sorted(result) == sorted(expected) else '✗'}")
        
        visualize_frequencies(words, result)
        
        # Additional statistics
        print("\nStats:")
        print(f"Number of words: {len(words)}")
        print(f"Word lengths: {[len(w) for w in words]}")
        print(f"Unique characters: {len(set(''.join(words)))}")
        print(f"Common characters: {len(result)}")

if __name__ == "__main__":
    test_common_chars()
