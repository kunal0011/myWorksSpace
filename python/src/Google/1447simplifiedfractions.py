"""
LeetCode 1447. Simplified Fractions

Problem Statement:
Given an integer n, return a list of all simplified fractions between 0 and 1 (exclusive) 
such that the denominator is less-than-or-equal-to n. The fractions can be in any order.
A simplified fraction is a fraction where GCD of numerator and denominator is 1.

Time Complexity: O(n^2 * log(min(num,d))) where n is the input number
Space Complexity: O(n^2) for storing the result
"""

import math
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        # Logic:
        # 1. For each denominator d from 2 to n:
        #    - For each numerator from 1 to d-1:
        #      * Check if fraction is simplified (GCD = 1)
        #      * If simplified, add to result list
        # 2. Use math.gcd to check if fraction is in its simplest form
        # 3. Return list of simplified fractions as strings

        result = []

        # Iterate over all possible denominators from 2 to n
        for d in range(2, n + 1):
            # Iterate over possible numerators from 1 to d-1
            for num in range(1, d):
                # Check if gcd of num and d is 1
                if math.gcd(num, d) == 1:
                    result.append(f"{num}/{d}")

        return result


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        2,  # Expected: ["1/2"]
        3,  # Expected: ["1/2", "1/3", "2/3"]
        4,  # Expected: ["1/2", "1/3", "1/4", "2/3", "3/4"]
        1   # Expected: []
    ]

    for i, n in enumerate(test_cases):
        result = solution.simplifiedFractions(n)
        print(f"Test case {i + 1}:")
        print(f"Input n: {n}")
        print(f"Simplified fractions: {result}")
        print()
