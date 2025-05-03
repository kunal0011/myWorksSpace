"""
LeetCode 313 - Super Ugly Number

A super ugly number is a positive integer whose prime factors are in the array primes.
Given an integer n and an array of integers primes, return the nth super ugly number.

The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

Example 1:
Input: n = 12, primes = [2,7,13,19]
Output: 32
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of super ugly numbers.

Example 2:
Input: n = 1, primes = [2,3,5]
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are in the array primes = [2,3,5].

Constraints:
- 1 <= n <= 106
- 1 <= primes.length <= 100
- 2 <= primes[i] <= 1000
- primes[i] is guaranteed to be a prime number
- All the values of primes are unique and sorted in ascending order
"""

import heapq
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # Initialize the min-heap with the number 1 (the first super ugly number)
        heap = [1]
        # Use a set to avoid duplicate entries in the heap
        seen = set([1])

        # Variable to store the current ugly number
        ugly_number = 1

        for _ in range(n):
            # Get the smallest number from the heap
            ugly_number = heapq.heappop(heap)

            # Generate new ugly numbers by multiplying with each prime
            for prime in primes:
                new_ugly = ugly_number * prime
                # Only add numbers we haven't seen before to maintain uniqueness
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)

        return ugly_number


def test_super_ugly_number():
    solution = Solution()

    # Test cases
    test_cases = [
        (12, [2, 7, 13, 19], 32),
        (1, [2, 3, 5], 1),
        (10, [2, 3, 5], 12),
        (15, [3, 5, 7, 11, 13], 21),
        (20, [2, 3, 5, 7], 28),
    ]

    for i, (n, primes, expected) in enumerate(test_cases):
        result = solution.nthSuperUglyNumber(n, primes)
        assert (
            result == expected
        ), f"Test case {i + 1} failed: got {result}, expected {expected}"
        print(
            f"Test case {i + 1} passed! n={n}, primes={primes}, Output: {result}"
        )


if __name__ == "__main__":
    test_super_ugly_number()
