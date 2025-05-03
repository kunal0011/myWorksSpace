"""
LeetCode 375 - Guess Number Higher or Lower II

Problem Statement:
We are playing a game where we pick a number from 1 to n. You have to guess which number we picked.
Every time you guess wrong, we'll tell you whether the number is higher or lower.
However, when you guess a particular number x, and you guess wrong, you pay $x.
Return the minimum amount of money you need to guarantee a win regardless of what number we picked.

Time Complexity: O(n^3)
Space Complexity: O(n^2)
"""

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp[i][j] represents minimum cost to guarantee win for range i to j
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Build dp table for different ranges
        for length in range(2, n + 1):  # length of the range
            for start in range(1, n - length + 2):
                end = start + length - 1
                min_cost = float('inf')
                
                # Try each number as the first guess
                for guess in range(start, end + 1):
                    # Maximum of left and right ranges plus current guess value
                    cost = guess + max(
                        dp[start][guess-1] if guess > start else 0,
                        dp[guess+1][end] if guess < end else 0
                    )
                    min_cost = min(min_cost, cost)
                
                dp[start][end] = min_cost
        
        return dp[1][n]


def test_get_money_amount():
    solution = Solution()
    
    # Test cases
    test_cases = [
        (1, 0),       # Only one number, no cost needed
        (2, 1),       # For range [1,2], guess 1 first
        (3, 2),       # For range [1,3], optimal strategy costs 2
        (4, 4),       # For range [1,4]
        (5, 6),       # For range [1,5]
        (10, 16),     # For range [1,10]
    ]
    
    for i, (n, expected) in enumerate(test_cases, 1):
        result = solution.getMoneyAmount(n)
        print(f"Test case {i}:")
        print(f"n = {n}")
        print(f"Expected minimum cost: {expected}")
        print(f"Got: {result}")
        print(f"Pass: {result == expected}\n")
        
        # Additional validation
        if result < 0:
            print(f"Error: Cost cannot be negative! Got {result}")


if __name__ == "__main__":
    test_get_money_amount()