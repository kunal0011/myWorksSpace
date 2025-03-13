"""
LeetCode 763: Partition Labels

You are given a string s. We want to partition the string into as many parts as possible 
so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, 
the resultant string should be s.

Return a list of integers representing the size of these parts.

Constraints:
- 1 <= s.length <= 500
- s consists of lowercase English letters
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Optimized solution using last occurrence tracking
        Time complexity: O(n)
        Space complexity: O(1) since we store at most 26 characters
        """
        # Track the last occurrence of each character
        last_pos = {char: idx for idx, char in enumerate(s)}
        
        partitions = []
        start = end = 0
        
        for idx, char in enumerate(s):
            # Extend the current partition if needed
            end = max(end, last_pos[char])
            
            # If we've reached the end of current partition
            if idx == end:
                partitions.append(end - start + 1)
                start = idx + 1
                
        return partitions
    
    def partitionLabels_alternative(self, s: str) -> List[int]:
        """
        Alternative solution using set tracking
        Slightly less efficient but more intuitive
        """
        result = []
        while s:
            # Find the position where first partition ends
            pos = len(set(s[:s.find(s[0]) + 1]))
            i = 0
            
            # Extend partition if needed
            while i < pos:
                pos = max(pos, s.rfind(s[i]) + 1)
                i += 1
                
            result.append(pos)
            s = s[pos:]
        return result


def validate_partition(s: str, partition_sizes: List[int]) -> bool:
    """Helper function to validate partition result"""
    if not partition_sizes or sum(partition_sizes) != len(s):
        return False
        
    start = 0
    seen_chars = set()
    
    for size in partition_sizes:
        current_chars = set(s[start:start + size])
        # Check if any character in current partition appears in other partitions
        if any(s.find(c, start + size) != -1 or c in seen_chars for c in current_chars):
            return False
        seen_chars.update(current_chars)
        start += size
        
    return True


def test_partition_labels():
    """Test function for Partition Labels solutions"""
    test_cases = [
        ("ababcbacadefegdehijhklij", [9, 7, 8]),
        ("eccbbbbdec", [10]),
        ("abc", [1, 1, 1]),
        ("abca", [4]),
        ("aaaa", [4]),
        ("caedbdedda", [1, 9]),
        ("vhaagbqkaqtctq", [1, 1, 12])
    ]
    
    solution = Solution()
    
    for i, (s, expected) in enumerate(test_cases, 1):
        # Test optimized solution
        result1 = solution.partitionLabels(s)
        # Test alternative solution
        result2 = solution.partitionLabels_alternative(s)
        
        print(f"\nTest case {i}:")
        print(f"Input string: {s}")
        print(f"Expected: {expected}")
        print(f"Optimized: {result1} {'✓' if result1 == expected else '✗'}")
        print(f"Alternative: {result2} {'✓' if result2 == expected else '✗'}")
        
        # Validate the solution
        is_valid = validate_partition(s, result1)
        print(f"Valid partition: {'✓' if is_valid else '✗'}")


if __name__ == "__main__":
    test_partition_labels()
