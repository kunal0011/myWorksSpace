"""
LeetCode 756: Pyramid Transition Matrix

You are given a bottom row of blocks, bottom, and a list of allowed blocks allowed. 
Each allowed[i] = [left, right, top] represents that if you have the positional bottom 
left and right blocks, you can place the top block on top of them.

Return true if you can build a pyramid starting from the bottom row; otherwise, return false.

A pyramid is a structure:
- Where each upper layer block sits on exactly two bottom layer blocks
- The upper block must be allowed according to allowed list
- May not use all blocks from bottom row

Constraints:
- 2 <= bottom.length <= 8
- 0 <= allowed.length <= 200
- allowed[i].length == 3
- The values in allowed[i] and bottom are single lowercase English letters
- All strings in allowed are unique
"""

from collections import defaultdict
from typing import List, Set


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        """
        Optimized solution using DFS with memoization
        Time: O(A * N^N) where A = len(allowed), N = len(bottom)
        Space: O(A + N)
        """
        # Build transitions map for O(1) lookup
        transitions = defaultdict(list)
        for triple in allowed:
            base = triple[:2]
            top = triple[2]
            transitions[base].append(top)
            
        def build_next_level(current: str, next_level: str, pos: int, cache: Set[str]) -> bool:
            # Base case: reached top of pyramid
            if len(current) == 1:
                return True
            
            # Current level complete, try building next level
            if pos >= len(current) - 1:
                return build_next_level(next_level, "", 0, cache)
            
            # Get base pair for current position
            base = current[pos:pos+2]
            
            # Try each possible top block
            for top in transitions[base]:
                new_next = next_level + top
                if new_next not in cache:
                    cache.add(new_next)
                    if build_next_level(current, new_next, pos + 1, cache):
                        return True
                    
            return False
            
        return build_next_level(bottom, "", 0, set())


def test_pyramid_transition():
    """Test function for Pyramid Transition Matrix"""
    test_cases = [
        ("BCD", ["BCC","CDE","CEA","FFF"], True),
        ("AABA", ["AAA","AAB","ABA","ABB","BAC"], True),
        ("AAAA", ["AAB","AAC","BCD","BBE","DEF"], False),
        ("AB", ["AA","AB","BC"], True),
        ("ABCD", [], False),
        ("XYZ", ["XYA","YZB","ZXC","ABC"], False),
    ]
    
    solution = Solution()
    
    for i, (bottom, allowed, expected) in enumerate(test_cases, 1):
        result = solution.pyramidTransition(bottom, allowed)
        
        print(f"\nTest case {i}:")
        print(f"Bottom: {bottom}")
        print(f"Allowed: {allowed}")
        print(f"Expected: {expected}")
        print(f"Result: {result} {'✓' if result == expected else '✗'}")
        
        # Visualize the pyramid if possible
        if result and len(bottom) <= 5:
            print("\nPossible pyramid structure:")
            current = bottom
            while len(current) > 1:
                print(" " * (len(bottom) - len(current)), current)
                current = current[:-1]


if __name__ == "__main__":
    test_pyramid_transition()
