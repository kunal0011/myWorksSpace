"""
LeetCode 819: Most Common Word

Given a string paragraph and a string array of banned words banned, return the most 
frequent word that is not banned. It is guaranteed there is at least one word that 
is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Constraints:
- 1 <= paragraph.length <= 1000
- paragraph consists of English letters, space ' ', or punctuation only
- 0 <= banned.length <= 100
- 1 <= banned[i].length <= 10
- banned[i] consists of only lowercase English letters
"""

import re
from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        """
        Optimized solution using regex and Counter
        Time: O(n), Space: O(n) where n is length of paragraph
        """
        # Convert to lowercase and split into words, removing punctuation
        words = re.findall(r'\w+', paragraph.lower())
        
        # Use set for O(1) lookup of banned words
        banned_set = set(banned)
        
        # Count non-banned words using Counter
        word_counts = Counter(word for word in words if word not in banned_set)
        
        # Return most common word
        return word_counts.most_common(1)[0][0]
    
    def mostCommonWord_alternative(self, paragraph: str, banned: List[str]) -> str:
        """
        Alternative solution without regex
        More explicit but slower for complex strings
        """
        # Replace punctuation with spaces and convert to lowercase
        for c in "!?',;.":
            paragraph = paragraph.replace(c, ' ')
        
        words = paragraph.lower().split()
        banned_set = set(banned)
        
        counts = {}
        max_count = 0
        result = ""
        
        for word in words:
            if word not in banned_set:
                counts[word] = counts.get(word, 0) + 1
                if counts[word] > max_count:
                    max_count = counts[word]
                    result = word
                    
        return result


def validate_result(paragraph: str, banned: List[str], result: str) -> bool:
    """Validate if the result is correct"""
    # Check if result is banned
    if result in banned:
        return False
        
    # Check if result exists in paragraph (case-insensitive)
    words = re.findall(r'\w+', paragraph.lower())
    if result not in words:
        return False
        
    # Check if it's the most frequent non-banned word
    word_counts = Counter(words)
    max_count = 0
    max_word = ""
    
    for word, count in word_counts.items():
        if word not in banned and count > max_count:
            max_count = count
            max_word = word
            
    return max_word == result


def test_most_common_word():
    """Test function for Most Common Word solutions"""
    test_cases = [
        (
            "Bob hit a ball, the hit BALL flew far after it was hit.",
            ["hit"],
            "ball"
        ),
        (
            "a.",
            [],
            "a"
        ),
        (
            "Bob. hIt, baLl",
            ["bob", "hit"],
            "ball"
        ),
        (
            "a, a, a, a, b,b,b,c, c",
            ["a"],
            "b"
        ),
        (
            "Bob!",
            [],
            "bob"
        ),
        (
            "L, P! X! C; u! P? w! P. G, S? l? X! D. w? m? f? v! i.",
            ["m","i","s","w","y","d","q","l","a","p","n","t","u","b","o","e","f","g","c","x"],
            "v"
        )
    ]
    
    solution = Solution()
    
    for i, (paragraph, banned, expected) in enumerate(test_cases, 1):
        # Test both implementations
        result1 = solution.mostCommonWord(paragraph, banned)
        result2 = solution.mostCommonWord_alternative(paragraph, banned)
        
        print(f"\nTest case {i}:")
        print(f"Paragraph: {paragraph}")
        print(f"Banned words: {banned}")
        print(f"Expected: {expected}")
        print(f"Regex solution: {result1} {'✓' if result1 == expected else '✗'}")
        print(f"Alternative: {result2} {'✓' if result2 == expected else '✗'}")
        
        # Validate result
        is_valid = validate_result(paragraph, banned, result1)
        print(f"Valid solution: {'✓' if is_valid else '✗'}")


if __name__ == "__main__":
    test_most_common_word()
