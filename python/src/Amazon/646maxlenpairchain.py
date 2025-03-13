"""
LeetCode 646: Maximum Length of Pair Chain

You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
Return the length longest chain which can be formed.

You can select pairs in any order.
"""

from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Sort pairs by second element (end point)
        # This is more efficient than sorting by first element
        pairs.sort(key=lambda x: x[1])
        
        curr_end = float('-inf')
        chain_length = 0
        
        # Greedy approach: Take pairs that can extend the chain
        for start, end in pairs:
            if start > curr_end:
                chain_length += 1
                curr_end = end
        
        return chain_length


def test_longest_chain():
    """Test driver for maximum length pair chain"""
    test_cases = [
        ([[1,2], [2,3], [3,4]], 2),
        ([[1,2], [7,8], [4,5]], 3),
        ([[1,2]], 1),
        ([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]], 3),
        ([[1,2], [2,3], [3,4], [4,5], [5,6]], 2),
        ([[1,5], [2,3], [3,4]], 2),
    ]
    
    solution = Solution()
    for i, (pairs, expected) in enumerate(test_cases, 1):
        result = solution.findLongestChain(pairs)
        status = "✓" if result == expected else "✗"
        print(f"\nTest {i}: {status}")
        print(f"Input: {pairs}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")


if __name__ == "__main__":
    test_longest_chain()
