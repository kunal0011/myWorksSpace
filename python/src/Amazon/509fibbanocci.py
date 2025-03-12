"""
LeetCode 509 - Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
"""

from typing import Dict
from functools import lru_cache

class Solution:
    def fib(self, n: int) -> int:
        """Iterative solution with O(1) space complexity"""
        if n == 0:
            return 0
        elif n == 1:
            return 1

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    @lru_cache(maxsize=None)
    def fib_recursive(self, n: int) -> int:
        """Recursive solution with memoization using lru_cache"""
        if n <= 1:
            return n
        return self.fib_recursive(n-1) + self.fib_recursive(n-2)

    def fib_matrix(self, n: int) -> int:
        """Matrix exponentiation solution with O(log n) time complexity"""
        if n <= 1:
            return n

        def matrix_multiply(a: list, b: list) -> list:
            return [
                [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
                [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]
            ]

        def matrix_power(matrix: list, power: int) -> list:
            if power == 0:
                return [[1, 0], [0, 1]]
            if power == 1:
                return matrix
            
            half = matrix_power(matrix, power // 2)
            if power % 2 == 0:
                return matrix_multiply(half, half)
            return matrix_multiply(matrix_multiply(half, half), matrix)

        base_matrix = [[1, 1], [1, 0]]
        result_matrix = matrix_power(base_matrix, n - 1)
        return result_matrix[0][0]


def test_fibonacci():
    """Test function to verify all solution approaches"""
    solution = Solution()
    
    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (10, 55),
        (20, 6765)
    ]
    
    for i, (n, expected) in enumerate(test_cases, 1):
        # Test all three solutions
        result_iterative = solution.fib(n)
        result_recursive = solution.fib_recursive(n)
        result_matrix = solution.fib_matrix(n)
        
        print(f"\nTest {i}: n = {n}")
        print(f"Expected: {expected}")
        print(f"Iterative Solution: {result_iterative} {'✓' if result_iterative == expected else '✗'}")
        print(f"Recursive Solution: {result_recursive} {'✓' if result_recursive == expected else '✗'}")
        print(f"Matrix Solution: {result_matrix} {'✓' if result_matrix == expected else '✗'}")


if __name__ == "__main__":
    test_fibonacci()
