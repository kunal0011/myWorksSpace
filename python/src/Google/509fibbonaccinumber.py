"""
LeetCode 509 - Fibonacci Number

Problem Statement:
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).
"""


class Solution:
    def fib(self, n: int) -> int:
        # Base cases
        if n <= 1:
            return n

        # Initialize variables for previous two numbers
        prev2, prev1 = 0, 1

        # Calculate Fibonacci iteratively
        for _ in range(2, n + 1):
            # Current number is sum of previous two
            curr = prev1 + prev2
            # Update previous numbers
            prev2, prev1 = prev1, curr

        return prev1


def run_tests():
    solution = Solution()

    # Test Case 1
    n1 = 2
    print(f"Test Case 1: n = {n1}")
    print(f"Result: {solution.fib(n1)}")  # Expected: 1

    # Test Case 2
    n2 = 3
    print(f"\nTest Case 2: n = {n2}")
    print(f"Result: {solution.fib(n2)}")  # Expected: 2

    # Test Case 3
    n3 = 4
    print(f"\nTest Case 3: n = {n3}")
    print(f"Result: {solution.fib(n3)}")  # Expected: 3

    # Test Case 4
    n4 = 10
    print(f"\nTest Case 4: n = {n4}")
    print(f"Result: {solution.fib(n4)}")  # Expected: 55


if __name__ == "__main__":
    run_tests()
