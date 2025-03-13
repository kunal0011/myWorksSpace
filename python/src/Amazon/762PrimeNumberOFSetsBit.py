"""
LeetCode 762: Prime Number of Set Bits in Binary Representation

Given two integers left and right, return the count of numbers in the inclusive range [left, right] 
having a prime number of set bits in their binary representation.

Recall that:
- The number of set bits in a number is the number of 1's present when written in binary
- A prime number is greater than 1 with no positive divisors other than 1 and itself

Constraints:
- 1 <= left <= right <= 10^6
- 0 <= right - left <= 10^4
"""


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        """
        Optimized solution using a pre-computed set of primes
        Since numbers are <= 10^6, they have at most 20 bits
        We only need to check if count of set bits is prime up to 20
        """
        # Pre-compute primes up to 20 (max possible set bits for given constraints)
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        
        def count_bits(n: int) -> int:
            """Count set bits using bit manipulation"""
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count
        
        # Count numbers with prime number of set bits
        return sum(count_bits(num) in primes for num in range(left, right + 1))
    
    def countPrimeSetBits_alternative(self, left: int, right: int) -> int:
        """
        Alternative solution using built-in bin() function
        Slightly less efficient but more readable
        """
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bin(num).count('1') in primes for num in range(left, right + 1))


def test_prime_set_bits():
    """Test function for Prime Number of Set Bits solutions"""
    test_cases = [
        (6, 10, 4),            # Basic test case
        (10, 15, 5),           # Another basic test case
        (1, 1, 0),            # Single number
        (1, 10000, 4925),     # Large range
        (842, 888, 23),       # Random range
        (100000, 100100, 45), # High numbers
    ]
    
    solution = Solution()
    
    for i, (left, right, expected) in enumerate(test_cases, 1):
        # Test optimized solution
        result1 = solution.countPrimeSetBits(left, right)
        # Test alternative solution
        result2 = solution.countPrimeSetBits_alternative(left, right)
        
        print(f"\nTest case {i}:")
        print(f"Range: [{left}, {right}]")
        print(f"Expected: {expected}")
        print(f"Optimized: {result1} {'✓' if result1 == expected else '✗'}")
        print(f"Alternative: {result2} {'✓' if result2 == expected else '✗'}")
        
        # Validate first few numbers in range for debugging
        if right - left < 5:
            print("\nDetailed validation:")
            for num in range(left, right + 1):
                bits = bin(num).count('1')
                print(f"Number: {num}, Binary: {bin(num)[2:]}, Set bits: {bits}")


if __name__ == "__main__":
    test_prime_set_bits()
