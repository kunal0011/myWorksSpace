"""
LeetCode 935: Knight Dialer

The chess knight has a unique movement, it may move two squares vertically and one square horizontally, 
or two squares horizontally and one square vertically (with both forming the shape of an L).

We have a phone dial pad with numbers from 0-9:
1 2 3
4 5 6
7 8 9
* 0 #

Given an integer n, return how many distinct phone numbers of length n we can dial,
where the knight can start from any numeric cell initially.
Since the answer may be too large, return it modulo 10^9 + 7.

Constraints:
- 1 <= n <= 5000
"""

from typing import List, Dict
from collections import defaultdict

class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Optimize moves dictionary for faster lookup
        moves = {
            0: (4, 6),
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (0, 3, 9),
            5: tuple(),
            6: (0, 1, 7),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4)
        }
        
        # Use array instead of dict for dp
        dp = [1] * 10
        
        # Iterate n-1 times as we already handled length 1
        for _ in range(n - 1):
            next_dp = [0] * 10
            for digit in range(10):
                for next_digit in moves[digit]:
                    next_dp[digit] = (next_dp[digit] + dp[next_digit]) % MOD
            dp = next_dp
            
        return sum(dp) % MOD

def validate_input(n: int) -> bool:
    """Validate input according to constraints"""
    return 1 <= n <= 5000

def visualize_moves() -> None:
    """Visualize knight's possible moves on dialpad"""
    moves = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }
    
    dialpad = """
    1 2 3
    4 5 6
    7 8 9
    * 0 #
    """
    print("Dialpad:")
    print(dialpad)
    
    for digit in range(10):
        moves_str = ", ".join(map(str, moves[digit]))
        print(f"From {digit}: can move to [{moves_str}]")

def test_knight_dialer():
    """Test function for Knight Dialer"""
    test_cases = [
        (1, 10),    # All digits are valid starting positions
        (2, 20),    # Knight can move to 20 different positions
        (3, 46),    # More combinations possible
        (4, 104),   # Grows exponentially
        (3131, 136006598)  # Large input
    ]
    
    solution = Solution()
    
    print("\nKnight's possible moves on dialpad:")
    visualize_moves()
    
    for i, (n, expected) in enumerate(test_cases, 1):
        is_valid = validate_input(n)
        
        print(f"\nTest case {i}:")
        print(f"Length n: {n}")
        
        if is_valid:
            result = solution.knightDialer(n)
            print(f"Number of possible combinations: {result}")
            print(f"Expected: {expected}")
            print(f"Test passed: {'✓' if result == expected else '✗'}")
            
            # Additional analysis for small n
            if n <= 3:
                # Show growth pattern
                pattern = [solution.knightDialer(x) for x in range(1, n+1)]
                print(f"Growth pattern: {pattern}")
                print(f"Growth rate: {[pattern[i]/pattern[i-1] for i in range(1, len(pattern))]}")
        
        print(f"Valid input: {'✓' if is_valid else '✗'}")

if __name__ == "__main__":
    test_knight_dialer()
