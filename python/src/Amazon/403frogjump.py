"""
LeetCode 403: Frog Jump

Problem Statement:
A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. 
The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by 
landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units.
The frog can only jump in the forward direction.

Example 1:
Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping:
1 unit to stone 1, then 2 units to stone 3, then 2 units to stone 5, then 3 units to stone 8, 
then 4 units to stone 12, then 5 units to stone 17.

Time Complexity: O(n * k) where n is number of stones and k is max jump size
Space Complexity: O(n * k) for the dp dictionary storing jump sizes at each stone
"""

from typing import List, Set, Dict

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # Edge cases
        if not stones or stones[0] != 0 or stones[1] != 1:
            return False
            
        n = len(stones)
        # Create stone set for O(1) lookup
        stone_positions = set(stones)
        
        # dp[stone] = set of possible jump sizes that can reach this stone
        dp: Dict[int, Set[int]] = {stone: set() for stone in stones}
        dp[0].add(0)  # Initial position
        dp[1].add(1)  # First jump must be 1 unit
        
        for stone in stones:
            for jump in dp[stone]:
                # Try all possible next jumps: k-1, k, k+1
                for next_jump in [jump - 1, jump, jump + 1]:
                    if next_jump > 0 and stone + next_jump in stone_positions:
                        dp[stone + next_jump].add(next_jump)
        
        return bool(dp[stones[-1]])
        
    def visualize_jumps(self, stones: List[int]) -> None:
        """Helper method to visualize the jumping process"""
        dp: Dict[int, Set[int]] = {stone: set() for stone in stones}
        dp[0].add(0)
        if len(stones) > 1:
            dp[1].add(1)
            
        print(f"\nJumping sequence for stones {stones}:")
        print("=" * 50)
        
        for stone in stones:
            print(f"\nAt stone {stone} with possible previous jumps: {dp[stone]}")
            for jump in dp[stone]:
                for next_jump in [jump - 1, jump, jump + 1]:
                    next_pos = stone + next_jump
                    if next_jump > 0 and next_pos in dp:
                        dp[next_pos].add(next_jump)
                        print(f"Can jump {next_jump} units to stone {next_pos}")
                        
        if dp[stones[-1]]:
            print(f"\n✓ Success! Can reach the last stone at {stones[-1]}")
            print(f"Final possible jumps: {dp[stones[-1]]}")
        else:
            print(f"\n✗ Failed! Cannot reach the last stone at {stones[-1]}")

def test_frog_jump():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()
    
    test_cases = [
        {
            "stones": [0, 1, 3, 5, 6, 8, 12, 17],
            "expected": True,
            "description": "Basic case with valid path"
        },
        {
            "stones": [0, 1, 2, 3, 4, 8, 9, 11],
            "expected": False,
            "description": "Cannot reach final stone"
        },
        {
            "stones": [0, 1],
            "expected": True,
            "description": "Minimum valid case"
        },
        {
            "stones": [0, 2],
            "expected": False,
            "description": "Invalid first jump"
        },
        {
            "stones": [0, 1, 3, 6, 10, 15, 21, 28],
            "expected": True,
            "description": "Increasing jump distances"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        stones = test_case["stones"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"Stones: {stones}")
        
        result = solution.canCross(stones)
        assert result == expected, f"Expected {expected}, but got {result}"
        print(f"✓ Test case passed!")
        
        # Visualize the jumping process for interesting cases
        if i <= 2:
            solution.visualize_jumps(stones)

if __name__ == "__main__":
    test_frog_jump()
    print("\nAll test cases passed! 🎉")
