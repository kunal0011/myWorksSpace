class Solution:
    """
    LeetCode 191 - Number of 1 Bits

    Problem Statement:
    Write a function that takes an unsigned integer and returns the number of '1' bits it has
    (also known as the Hamming weight).

    Note:
    - In some languages, there is no unsigned integer type. In this case, the input will be given 
      as a signed integer type. It should not affect your implementation, as the integer's internal 
      binary representation is the same, whether it is signed or unsigned.
    """

    def hammingWeight(self, n: int) -> int:
        """
        Solution 1: Using bit shifting
        Time Complexity: O(1) - as integer has fixed number of bits (32)
        Space Complexity: O(1)
        """
        count = 0
        while n:
            count += n & 1  # Check if least significant bit is 1
            n >>= 1        # Right shift by 1
        return count

    def hammingWeight_brian_kernighan(self, n: int) -> int:
        """
        Solution 2: Using Brian Kernighan's algorithm
        Time Complexity: O(1) - actually O(number of 1 bits)
        Space Complexity: O(1)

        This method uses the fact that n & (n-1) always removes
        the rightmost set bit of n.
        """
        count = 0
        while n:
            n &= (n - 1)  # Clear the least significant set bit
            count += 1
        return count


def run_tests():
    """Test driver for Number of 1 Bits solutions"""
    solution = Solution()

    # Test cases
    test_cases = [
        {
            'input': 11,  # Binary: 1011
            'expected': 3
        },
        {
            'input': 128,  # Binary: 10000000
            'expected': 1
        },
        {
            'input': 4294967293,  # Binary: 11111111111111111111111111111101
            'expected': 31
        },
        {
            'input': 0,
            'expected': 0
        }
    ]

    # Test both implementations
    methods = [
        ('Bit Shifting', solution.hammingWeight),
        ('Brian Kernighan', solution.hammingWeight_brian_kernighan)
    ]

    for method_name, method in methods:
        print(f"\nTesting {method_name} method:")
        print("-" * 50)

        for i, test in enumerate(test_cases, 1):
            result = method(test['input'])
            passed = result == test['expected']
            print(f"Test {i}:")
            print(f"Input: {test['input']} (Binary: {bin(test['input'])[2:]})")
            print(f"Expected: {test['expected']}")
            print(f"Got: {result}")
            print(f"Result: {'✓ PASS' if passed else '✗ FAIL'}\n")


if __name__ == "__main__":
    run_tests()
