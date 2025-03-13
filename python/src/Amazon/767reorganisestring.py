"""
LeetCode 767: Reorganize String

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Constraints:
- 1 <= s.length <= 500
- s consists of lowercase English letters
"""

import heapq
from collections import Counter
from typing import List, Tuple


class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        Optimized solution using max heap
        Time: O(n log k) where k is unique chars
        Space: O(k)
        """
        # Early validation
        if not s:
            return ""
            
        # Count frequencies
        counts = Counter(s)
        max_freq = max(counts.values())
        
        # If any character appears more than (n+1)/2 times, impossible to reorganize
        if max_freq > (len(s) + 1) // 2:
            return ""
            
        # Create max heap with (-freq, char) pairs
        heap = [(-freq, char) for char, freq in counts.items()]
        heapq.heapify(heap)
        
        result = []
        
        while len(heap) >= 2:
            # Get two most frequent characters
            freq1, char1 = heapq.heappop(heap)
            freq2, char2 = heapq.heappop(heap)
            
            # Add them to result
            result.extend([char1, char2])
            
            # Update frequencies and add back if needed
            if freq1 + 1 < 0:
                heapq.heappush(heap, (freq1 + 1, char1))
            if freq2 + 1 < 0:
                heapq.heappush(heap, (freq2 + 1, char2))
        
        # Handle last character if any
        if heap:
            freq, char = heapq.heappop(heap)
            if freq < -1:  # If more than one occurrence left, impossible
                return ""
            result.append(char)
        
        return ''.join(result)
    
    def reorganizeString_greedy(self, s: str) -> str:
        """
        Alternative greedy solution
        Time: O(n)
        Space: O(k)
        """
        counts = Counter(s)
        if max(counts.values()) > (len(s) + 1) // 2:
            return ""
            
        # Sort characters by frequency
        chars = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
        result = [''] * len(s)
        
        # Place most frequent chars in even indices
        idx = 0
        for char in chars:
            while counts[char] > 0 and idx < len(s):
                result[idx] = char
                counts[char] -= 1
                idx += 2
                
        # Place remaining chars in odd indices
        idx = 1
        for char in chars:
            while counts[char] > 0 and idx < len(s):
                result[idx] = char
                counts[char] -= 1
                idx += 2
                
        return ''.join(result)


def validate_reorganized_string(original: str, reorganized: str) -> bool:
    """Validate if the reorganized string meets all requirements"""
    if not reorganized:
        return False
    if len(original) != len(reorganized):
        return False
    if sorted(original) != sorted(reorganized):
        return False
    return all(reorganized[i] != reorganized[i+1] for i in range(len(reorganized)-1))


def test_reorganize_string():
    """Comprehensive test function"""
    test_cases = [
        ("aab", True),
        ("aaab", False),
        ("vvvlo", True),
        ("", True),
        ("a", True),
        ("aabbcc", True),
        ("aaaaabc", False),
        ("baaba", True),
        ("aaaaaaaaaaaabbbbbbbbbbbcccccccccc", False)
    ]
    
    solution = Solution()
    
    for i, (s, possible) in enumerate(test_cases, 1):
        print(f"\nTest case {i}:")
        print(f"Input: {s}")
        
        # Test both solutions
        result1 = solution.reorganizeString(s)
        result2 = solution.reorganizeString_greedy(s)
        
        print(f"Heap solution: {result1}")
        print(f"Greedy solution: {result2}")
        
        # Validate results
        valid1 = validate_reorganized_string(s, result1) if result1 else not possible
        valid2 = validate_reorganized_string(s, result2) if result2 else not possible
        
        print(f"Heap solution valid: {'✓' if valid1 else '✗'}")
        print(f"Greedy solution valid: {'✓' if valid2 else '✗'}")


if __name__ == "__main__":
    test_reorganize_string()
