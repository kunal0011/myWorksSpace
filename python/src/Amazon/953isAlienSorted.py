"""
LeetCode 953: Verifying an Alien Dictionary

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet,
return true if and only if the given words are sorted lexicographically in this alien language.

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 20
- order.length == 26
- All characters in words[i] and order are lowercase English letters
- All the strings of words are unique
"""

from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Create character to index mapping for O(1) lookups
        char_map = {c: i for i, c in enumerate(order)}
        
        def is_sorted(word1: str, word2: str) -> bool:
            # Compare characters until we find a difference
            for c1, c2 in zip(word1, word2):
                if char_map[c1] != char_map[c2]:
                    return char_map[c1] < char_map[c2]
            # If we get here, one word might be a prefix of another
            return len(word1) <= len(word2)
        
        # Check if adjacent words are sorted
        return all(is_sorted(words[i], words[i+1]) 
                  for i in range(len(words)-1))

def validate_input(words: List[str], order: str) -> bool:
    """Validate input according to constraints"""
    if not 1 <= len(words) <= 100:
        return False
    if not all(1 <= len(word) <= 20 for word in words):
        return False
    if len(order) != 26:
        return False
    if not all(c.islower() for word in words for c in word):
        return False
    if not all(c.islower() for c in order):
        return False
    if len(set(words)) != len(words):
        return False
    return True

def visualize_comparison(word1: str, word2: str, order: str) -> str:
    """Create visual representation of word comparison"""
    char_map = {c: i for i, c in enumerate(order)}
    result = []
    
    for i in range(max(len(word1), len(word2))):
        if i < len(word1) and i < len(word2):
            c1, c2 = word1[i], word2[i]
            order_info = "=" if char_map[c1] == char_map[c2] else "<" if char_map[c1] < char_map[c2] else ">"
            result.append(f"{c1} {order_info} {c2} ({char_map[c1]} vs {char_map[c2]})")
        else:
            result.append("Length difference")
            break
            
    return "\n".join(result)

def test_alien_dictionary():
    """Test function for Verifying an Alien Dictionary"""
    test_cases = [
        (["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
        (["word","world","row"], "worldabcefghijkmnpqstuvxyz", False),
        (["apple","app"], "abcdefghijklmnopqrstuvwxyz", False),
        (["kuvp","q"], "ngxlkthsjuoqcpavbfdermiywz", True),
        (["hello","hello"], "abcdefghijklmnopqrstuvwxyz", True)
    ]
    
    solution = Solution()
    
    for i, (words, order, expected) in enumerate(test_cases, 1):
        is_valid = validate_input(words, order)
        result = solution.isAlienSorted(words, order)
        
        print(f"\nTest case {i}:")
        print(f"Words: {words}")
        print(f"Alphabet order: {order}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        # Show detailed comparison for adjacent words
        print("\nWord comparisons:")
        for j in range(len(words)-1):
            print(f"\nComparing {words[j]} with {words[j+1]}:")
            print(visualize_comparison(words[j], words[j+1], order))
        
        # Additional statistics
        print("\nStatistics:")
        print(f"Number of words: {len(words)}")
        print(f"Word lengths: {[len(w) for w in words]}")
        unique_chars = set(c for word in words for c in word)
        print(f"Unique characters used: {len(unique_chars)} {sorted(unique_chars)}")

if __name__ == "__main__":
    test_alien_dictionary()
