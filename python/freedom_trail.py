"""
LeetCode 514 - Freedom Trail

Problem Statement:
In the video game "Freedom Trail", the player's task is to find a path from the starting position (at 'S') 
to the ending position (at 'E') while collecting all required keys. Here's a simplification of the game:

Given a string ring that represents characters engraved clockwise on a ring from position 0, and another string key 
that represents a string of keys we need to spell. Initially, the first character of ring is aligned at 12:00 direction.
You need to spell all characters in key one by one by rotating ring clockwise or anticlockwise to align each character 
of key at 12:00 and then pressing the center button.

Return the minimum number of steps to spell all characters in key.
The answer is the sum of:
1. The minimum rotations (clockwise or anticlockwise) needed for each character.
2. The number of key presses (one press for each character).
"""

from typing import List
from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # Create a dictionary to store positions of each character in ring
        char_positions = defaultdict(list)
        for i, char in enumerate(ring):
            char_positions[char].append(i)
        
        # Cache for dynamic programming
        # dp[i][j] represents minimum steps needed to spell key[i:] when ring position is at j
        dp = {}
        
        def min_steps(key_idx: int, ring_idx: int) -> int:
            # Base case: if we've spelled all characters
            if key_idx == len(key):
                return 0
                
            # If already calculated
            if (key_idx, ring_idx) in dp:
                return dp[(key_idx, ring_idx)]
            
            result = float('inf')
            curr_char = key[key_idx]
            n = len(ring)
            
            # Try all positions of current character
            for next_pos in char_positions[curr_char]:
                # Calculate clockwise and counterclockwise distances
                dist = abs(next_pos - ring_idx)
                steps = min(dist, n - dist)  # Take minimum of clockwise and counterclockwise
                
                # Add 1 for button press and recurse for remaining characters
                total = steps + 1 + min_steps(key_idx + 1, next_pos)
                result = min(result, total)
            
            dp[(key_idx, ring_idx)] = result
            return result
        
        return min_steps(0, 0)  # Start from key index 0 and ring position 0

def run_tests():
    solution = Solution()
    
    # Test Case 1
    ring1 = "godding"
    key1 = "gd"
    print("Test Case 1:")
    print(f"Ring: {ring1}")
    print(f"Key: {key1}")
    print(f"Result: {solution.findRotateSteps(ring1, key1)}")  # Expected: 4
    
    # Test Case 2
    ring2 = "godding"
    key2 = "godding"
    print("\nTest Case 2:")
    print(f"Ring: {ring2}")
    print(f"Key: {key2}")
    print(f"Result: {solution.findRotateSteps(ring2, key2)}")  # Expected: 13
    
    # Test Case 3
    ring3 = "abcde"
    key3 = "ade"
    print("\nTest Case 3:")
    print(f"Ring: {ring3}")
    print(f"Key: {key3}")
    print(f"Result: {solution.findRotateSteps(ring3, key3)}")  # Expected: 6

if __name__ == "__main__":
    run_tests()