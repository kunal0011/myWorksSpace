class Solution:
    def countPrimes(self, n: int) -> set[int]:
        """ Helper function to find all primes less than n """
        is_prime = [True] * n
        p = 2
        while (p * p < n):
            if (is_prime[p] == True):
                for i in range(p * p, n, p):
                    is_prime[i] = False
            p += 1
        return {p for p in range(2, n) if is_prime[p]}

    def countPrimeSetBits(self, L: int, R: int) -> int:
        # Determine the maximum number of set bits to consider
        # Since Python int can be as large as needed, we consider up to 32 bits.
        max_bits = 32

        # Get all prime numbers less than or equal to max_bits
        prime_set = self.countPrimes(max_bits + 1)

        count = 0
        for num in range(L, R + 1):
            # Count the number of set bits
            set_bits = bin(num).count('1')
            # Check if the count of set bits is a prime number
            if set_bits in prime_set:
                count += 1

        return count
