"""
LeetCode 877: Stone Game

Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row,
and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones. The total number of stones is odd, so there are no ties.

Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile 
either from the beginning or from the end of the row. This continues until there are no more piles left.

Return true if Alice wins the game, false if Bob wins.

Constraints:
- 2 <= piles.length <= 500
- piles.length is even
- 1 <= piles[i] <= 500
- sum(piles) is odd
"""

from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """
        Mathematical solution: Alice always wins because:
        1. Length is even, sum is odd (no ties possible)
        2. Alice can always choose all even or all odd indexed piles
        3. One of these groups must be larger (sum is odd)
        4. Alice can force this strategy by picking ends appropriately
        """
        return True
        
    def stoneGameDP(self, piles: List[int]) -> bool:
        """
        Educational DP solution showing the actual game strategy
        Time: O(n^2), Space: O(n^2)
        """
        n = len(piles)
        dp = {}  # (left, right) -> max score difference
        
        def play(left: int, right: int) -> int:
            if left > right:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]
                
            # Take left or right pile
            take_left = piles[left] - play(left + 1, right)
            take_right = piles[right] - play(left, right - 1)
            
            dp[(left, right)] = max(take_left, take_right)
            return dp[(left, right)]
            
        return play(0, n-1) > 0

def validate_piles(piles: List[int]) -> bool:
    """Validate input according to constraints"""
    if not 2 <= len(piles) <= 500:
        return False
    if len(piles) % 2 != 0:
        return False
    if not all(1 <= x <= 500 for x in piles):
        return False
    if sum(piles) % 2 == 0:
        return False
    return True

def test_stone_game():
    """Test function for Stone Game"""
    test_cases = [
        ([5,3,4,5], True),
        ([3,7,2,3], True),
        ([1,3,5,7], True),
        ([1,5,2,4], True),
        ([7,8,8,10], True)
    ]
    
    solution = Solution()
    
    for i, (piles, expected) in enumerate(test_cases, 1):
        is_valid = validate_piles(piles)
        result = solution.stoneGame(piles)
        dp_result = solution.stoneGameDP(piles)
        
        print(f"\nTest case {i}:")
        print(f"Piles: {piles}")
        print(f"Sum: {sum(piles)}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Mathematical solution: {result}")
        print(f"DP solution: {dp_result}")
        
        # Show possible first moves for Alice
        print("\nPossible first moves for Alice:")
        print(f"Take left ({piles[0]}): remaining {piles[1:]} ")
        print(f"Take right ({piles[-1]}): remaining {piles[:-1]}")
        
        # Show even/odd sums
        even_sum = sum(piles[i] for i in range(0, len(piles), 2))
        odd_sum = sum(piles[i] for i in range(1, len(piles), 2))
        print(f"\nEven-indexed piles sum: {even_sum}")
        print(f"Odd-indexed piles sum: {odd_sum}")
        print(f"Optimal choice: {'even' if even_sum > odd_sum else 'odd'} indices")

if __name__ == "__main__":
    test_stone_game()
