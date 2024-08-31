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
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)

        return ugly_number
