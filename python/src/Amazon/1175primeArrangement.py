import math

MOD = 10**9 + 7


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        # Helper function to determine if a number is prime
        def is_prime(num):
            if num <= 1:
                return False
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True

        # Count how many prime numbers are there from 1 to n
        prime_count = sum(is_prime(i) for i in range(1, n + 1))

        # The rest are non-prime
        non_prime_count = n - prime_count

        # Return the factorial of prime_count and non_prime_count modulo MOD
        return (math.factorial(prime_count) * math.factorial(non_prime_count)) % MOD


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    n1 = 5
    result1 = sol.numPrimeArrangements(n1)
    assert result1 == 12, f"Test case 1 failed: {result1}"

    # Test case 2
    n2 = 100
    result2 = sol.numPrimeArrangements(n2)
    assert result2 == 682289015, f"Test case 2 failed: {result2}"

    print("All test cases passed!")
