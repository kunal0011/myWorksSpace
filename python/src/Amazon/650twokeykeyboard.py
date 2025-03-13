"""
LeetCode 650: Two Key Keyboard

Problem Statement:

Initially you have 1 character 'A' on screen. You can perform two operations:
1. Copy All: Copy all characters present on the screen
2. Paste: Paste characters copied in the last copy operation

Given an integer n, return the minimum number of operations needed to get exactly n 'A's on the screen.
"""

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        # Use dp to optimize - dp[i] represents min steps to get i 'A's
        dp = [float('inf')] * (n + 1)
        dp[1] = 0  # Base case: 1 'A'
        
        for i in range(2, n + 1):
            # Try all possible factors
            for j in range(1, i):
                if i % j == 0:
                    # dp[j] steps to get j 'A's
                    # (i/j - 1) paste operations after copying j 'A's once
                    dp[i] = min(dp[i], dp[j]+1+(i/j-1))
        
        return int(dp[n])


def test_solution():
    """Test driver with various test cases"""
    solution = Solution()
    
    test_cases = [
        (1, 0),    # Base case: already have 1 'A'
        (2, 2),    # Copy + Paste = 2 steps
        (3, 3),    # Copy + Paste + Paste = 3 steps
        (4, 4),    # Copy + Paste + Copy + Paste = 4 steps
        (6, 5),    # Copy + Paste + Copy + Paste + Paste = 5 steps
        (9, 6),    # Optimal way to get 9 'A's
        (15, 8)    # Complex case
    ]
    
    for n, expected in test_cases:
        result = solution.minSteps(n)
        print(f"n = {n}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 30)

if __name__ == "__main__":
    test_solution()
