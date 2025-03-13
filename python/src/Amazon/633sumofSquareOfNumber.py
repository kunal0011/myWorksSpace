"""
LeetCode 633 - Sum of Square Numbers

Given a non-negative integer c, decide whether there're two integers a and b such that a² + b² = c.

Example 1:
Input: c = 5
Output: true
Explanation: 1² + 2² = 5

Example 2:
Input: c = 3
Output: false

Constraints:
- 0 <= c <= 2³¹ - 1
"""

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        Optimized two-pointer solution
        Time Complexity: O(sqrt(c))
        Space Complexity: O(1)
        """
        left = 0
        right = int(math.sqrt(c))
        
        while left <= right:
            curr_sum = left * left + right * right
            if curr_sum == c:
                return True
            elif curr_sum < c:
                left += 1
            else:
                right -= 1
        return False
    
    def judgeSquareSum_bruteforce(self, c: int) -> bool:
        """
        Brute force solution for validation
        Time Complexity: O(c)
        Space Complexity: O(1)
        """
        for a in range(int(math.sqrt(c)) + 1):
            b = math.sqrt(c - a * a)
            if b == int(b):
                return True
        return False


def test_judge_square_sum():
    """
    Test function with comprehensive test cases
    """
    solution = Solution()
    
    test_cases = [
        # Basic test cases
        (5, True),    # 1² + 2² = 5
        (3, False),   # No solution
        (4, True),    # 0² + 2² = 4
        
        # Edge cases
        (0, True),    # 0² + 0² = 0
        (1, True),    # 0² + 1² = 1
        (2, True),    # 1² + 1² = 2
        
        # Larger numbers
        (25, True),   # 0² + 5² = 25
        (7, False),   # No solution
        (17, True),   # 1² + 4² = 17
        
        # Very large numbers
        (1000000, True),  # 1000² + 0² = 1000000
        (999999, False),  # No solution
        
        # Numbers requiring both squares
        (50, True),   # 5² + 5² = 50
        (100, True),  # 6² + 8² = 100
    ]
    
    print("Running tests for Sum of Square Numbers...\n")
    
    for i, (c, expected) in enumerate(test_cases, 1):
        # Test optimized solution
        result = solution.judgeSquareSum(c)
        # Test brute force solution for validation
        result_bf = solution.judgeSquareSum_bruteforce(c)
        
        print(f"Test Case {i}:")
        print(f"Input: c = {c}")
        print(f"Expected: {expected}")
        print(f"Optimized Solution: {result} {'✅' if result == expected else '❌'}")
        print(f"Brute Force Solution: {result_bf} {'✅' if result_bf == expected else '❌'}")
        
        if result != expected:
            print(f"❌ Test case failed!")
            print(f"Got: {result}")
            print(f"Expected: {expected}")
        else:
            print("✅ Test case passed!")
        print()


if __name__ == "__main__":
    test_judge_square_sum()
