"""
LeetCode 279 - Perfect Squares

Problem Statement:
Given an integer n, return the least number of perfect square numbers that sum to n.
A perfect square is an integer that is the square of an integer; in other words,
it is the product of some integer with itself.

Logic:
1. Use Dynamic Programming approach
2. Create dp array of size n+1 initialized with infinity
3. For each number i from 1 to n:
   - Consider all perfect squares <= i
   - For each square j, dp[i] = min(dp[i], dp[i-j] + 1)
4. Return dp[n] which contains minimum perfect squares needed
"""

class Solution:
    def numSquares(self, n: int) -> int:
        # Initialize DP array with a large number (infinity)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case: 0 can be represented as 0 perfect squares

        # List of all perfect squares less than or equal to n
        squares = [i * i for i in range(1, int(n**0.5) + 1)]

        # Fill the DP array
        for i in range(1, n + 1):
            for square in squares:
                if i >= square:
                    dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[n]

def test_num_squares():
    solution = Solution()
    
    # Test cases
    test_cases = [
        (12, 3),    # 12 = 4 + 4 + 4
        (13, 2),    # 13 = 4 + 9
        (1, 1),     # 1 = 1
        (16, 1),    # 16 = 16
        (7, 4),     # 7 = 4 + 1 + 1 + 1
        (0, 0)      # Edge case
    ]
    
    for i, (n, expected) in enumerate(test_cases):
        result = solution.numSquares(n)
        assert result == expected, f"Test case {i + 1} failed: n={n}, expected {expected}, got {result}"
        print(f"Test case {i + 1} passed: n={n}, least number of perfect squares={result}")

if __name__ == "__main__":
    test_num_squares()
    print("All test cases passed!")
