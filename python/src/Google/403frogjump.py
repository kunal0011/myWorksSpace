"""
LeetCode 403 - Frog Jump

A frog is crossing a river. The river is divided into some number of units, and at each unit, 
there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can 
cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes 
the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. 
The frog can only jump in the forward direction.

Example 1:
Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping:
1 unit from stone 0 to stone 1
2 units from stone 1 to stone 3
2 units from stone 3 to stone 5
1 unit from stone 5 to stone 6
2 units from stone 6 to stone 8
4 units from stone 8 to stone 12
5 units from stone 12 to stone 17

Example 2:
Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
"""

from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # Create a hash map to store stone positions for O(1) lookup
        stone_positions = set(stones)
        
        # Create a dictionary to store possible jumps at each stone
        # Key: stone position, Value: set of possible jump distances
        dp = {stone: set() for stone in stones}
        dp[0].add(1)  # Initial condition: first jump must be 1
        
        # For each stone
        for stone in stones:
            # For each possible jump from this stone
            for jump in dp[stone]:
                # Try landing at next position
                next_stone = stone + jump
                
                # If we can land on a stone
                if next_stone in stone_positions:
                    # Add possible next jumps (k-1, k, k+1)
                    if jump > 0:
                        dp[next_stone].add(jump - 1)
                    dp[next_stone].add(jump)
                    dp[next_stone].add(jump + 1)
        
        # Check if last stone has any possible jumps (means we can reach it)
        return len(dp[stones[-1]]) > 0


# Test driver
def main():
    solution = Solution()
    
    # Test cases
    test_cases = [
        [0,1,3,5,6,8,12,17],  # Should return True
        [0,1,2,3,4,8,9,11],   # Should return False
        [0,1],                # Should return True
        [0,2],                # Should return False
        [0,1,3,6,10,15,21],  # Should return True
    ]
    
    for stones in test_cases:
        result = solution.canCross(stones)
        print(f"\nInput: stones = {stones}")
        print(f"Output: {result}")


if __name__ == "__main__":
    main()