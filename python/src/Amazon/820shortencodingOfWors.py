"""
LeetCode 820: Short Encoding of Words

A valid encoding of an array of words is any reference string s and array of indices indices such that:
- words.length == indices.length
- The reference string s ends with the '#' character
- For each index indices[i], the substring s[indices[i]] ending at the '#' character equals words[i]
- Each substring of s that ends with '#' occurs exactly once in s

Return the length of the shortest reference string s possible of any valid encoding of words.

Constraints:
- 1 <= words.length <= 2000
- 1 <= words[i].length <= 7
- words[i] consists of only lowercase letters
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """
        Optimized solution using Trie
        Time: O(∑w[i].length)
        Space: O(∑w[i].length)
        """
        # Remove duplicates and sort by length in descending order
        words = sorted(set(words), key=len, reverse=True)
        
        # Build trie
        root = TrieNode()
        total_length = 0
        
        for word in words:
            curr = root
            is_new_word = False
            # Insert word in reverse
            for c in reversed(word):
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                    is_new_word = True
                curr = curr.children[c]
            if is_new_word:
                total_length += len(word) + 1  # +1 for '#'
                
        return total_length
    
    def minimumLengthEncoding_set(self, words: List[str]) -> int:
        """
        Alternative solution using set operations
        Time: O(∑w[i].length)
        Space: O(∑w[i].length)
        """
        good = set(words)
        for word in words:
            for i in range(1, len(word)):
                good.discard(word[i:])
        return sum(len(word) + 1 for word in good)


def validate_encoding(words: List[str], length: int) -> bool:
    """Validate if the encoding length is possible"""
    if not 1 <= len(words) <= 2000:
        return False
        
    if any(not (1 <= len(w) <= 7) for w in words):
        return False
        
    if any(not w.islower() for w in words):
        return False
        
    # Check if length is sufficient to encode all words
    min_length = sum(len(w) + 1 for w in set(words))
    return length <= min_length


def test_minimum_length_encoding():
    """Test function for Short Encoding of Words"""
    test_cases = [
        (["time", "me", "bell"], 10),
        (["t"], 2),
        (["me", "time"], 5),
        (["feipyxx", "e"], 10),
        (["time", "time", "time", "time"], 5),
        (["p", "grah", "qwosp"], 15)
    ]
    
    solution = Solution()
    
    for i, (words, expected) in enumerate(test_cases, 1):
        # Test both implementations
        result1 = solution.minimumLengthEncoding(words)
        result2 = solution.minimumLengthEncoding_set(words)
        
        print(f"\nTest case {i}:")
        print(f"Words: {words}")
        print(f"Expected length: {expected}")
        print(f"Trie solution: {result1} {'✓' if result1 == expected else '✗'}")
        print(f"Set solution: {result2} {'✓' if result2 == expected else '✗'}")
        
        # Validate the solution
        is_valid = validate_encoding(words, result1)
        print(f"Valid encoding: {'✓' if is_valid else '✗'}")
        
        # Show possible encoding
        if result1 == expected:
            encoding = "#".join(sorted(set(words), key=len, reverse=True)) + "#"
            print(f"Possible encoding: {encoding}")


if __name__ == "__main__":
    test_minimum_length_encoding()
