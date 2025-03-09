"""
Problem: Count Primes (LeetCode 204)

Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0

Constraints:
0 <= n <= 5 * 10^6
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        """
        Counts the number of prime numbers less than n.

        Args:
            n: The upper limit (exclusive) for counting primes.

        Returns:
            The number of prime numbers less than n.
        """
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        # Sieve of Eratosthenes
        p = 2
        while p * p < n:
            if is_prime[p]:
                for i in range(p * p, n, p):
                    is_prime[i] = False
            p += 1

        return sum(is_prime)

"""
Logic Explanation:

The algorithm used to count prime numbers is the Sieve of Eratosthenes.

1.  Initialization:
    -   Create a boolean list `is_prime` of size `n`, initially marking all numbers as potentially prime (True).
    -   Mark 0 and 1 as not prime (False).

2.  Sieving Process:
    -   Iterate from 2 up to the square root of `n`. We only need to go up to the square root because if a number n is composite, it must have a factor less than or equal to its square root.
    -   For each number `p` in this range:
        -   If `is_prime[p]` is True (meaning p is a prime number):
            -   Mark all multiples of `p` starting from `p*p` up to `n` as not prime (False). We start at `p*p` because all smaller multiples of `p` would have already been marked as not prime by smaller prime numbers. We step by p to mark the multiples.

3.  Counting Primes:
    -   After the sieving process is complete, count the number of True values in the `is_prime` list. This count represents the number of prime numbers less than `n`.
"""

def test_count_primes():
    """
    Tests the countPrimes function with several test cases.
    """
    sol = Solution()

    # Test cases: (input, expected output)
    test_cases = [
        (10, 4),  # 2, 3, 5, 7
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 1),  # 2
        (4, 2),  # 2, 3
        (5, 2),
        (6, 3),
        (7, 3),
        (8, 4),
        (9, 4),
        (11, 4),
        (100, 25),
        (499979,41537),
        (1000,168),
        (50,15)

    ]

    for n, expected in test_cases:
        result = sol.countPrimes(n)
        assert result == expected, f"Failed for n = {n}: Expected {expected}, but got {result}"

    print("All test cases passed!")

# Run the tests
test_count_primes()
