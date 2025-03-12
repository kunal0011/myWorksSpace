"""
LeetCode 476 - Number Complement

Problem Statement:
-----------------
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
- For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.

Given an integer num, return its complement.

Note:
- You could assume that the given integer fits in a 32-bit signed integer.
- For a given number N, its complement cannot be N itself.

Examples:
--------
Input: num = 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in decimal.

Input: num = 1
Output: 0
Explanation: 1 is "1" in binary, with complement "0" in binary, which is 0 in decimal.

Constraints:
-----------
* 1 <= num < 2^31
"""

class Solution:
    def findComplement(self, num: int) -> int:
        """
        Find the complement of the given integer.
        
        Algorithm:
        1. Find the bit length of the number
        2. Create a mask with all 1's of the same length
        3. XOR the number with mask to flip all bits
        
        Time Complexity: O(1) - bitwise operations are constant time
        Space Complexity: O(1) - only uses constant extra space
        
        Args:
            num: The input integer
        
        Returns:
            The complement of the input integer
        """
        if num == 0:
            return 1
            
        # Get the bit length of num
        bit_length = num.bit_length()
        
        # Create a mask with all bits set to 1 (same length as num)
        # We use (1 << bit_length) - 1 instead of ~num to handle leading zeros
        mask = (1 << bit_length) - 1
        
        # XOR num with the mask to get the complement
        return num ^ mask


def test_number_complement():
    """
    Comprehensive test driver for number complement problem
    """
    test_cases = [
        (
            5,
            2,
            "Basic test with binary 101"
        ),
        (
            1,
            0,
            "Edge case with single bit"
        ),
        (
            7,
            0,
            "All bits set (111)"
        ),
        (
            10,
            5,
            "Even number (1010)"
        ),
        (
            0,
            1,
            "Edge case with zero"
        ),
        (
            4,
            3,
            "Power of 2 (100)"
        ),
        (
            2,
            1,
            "Another power of 2 (10)"
        ),
        (
            15,
            0,
            "All bits set in 4 bits (1111)"
        ),
        (
            1024,
            1023,
            "Large power of 2"
        ),
        (
            8,
            7,
            "Power of 2 with multiple trailing zeros"
        )
    ]
    
    solution = Solution()
    
    print("\nRunning Number Complement Tests...")
    print("=" * 50)
    
    for i, (input_num, expected, description) in enumerate(test_cases, 1):
        result = solution.findComplement(input_num)
        status = "✓ PASSED" if result == expected else "✗ FAILED"
        print(f"\nTest case {i}: {status}")
        print(f"Description: {description}")
        print(f"Input: {input_num} (binary: {bin(input_num)[2:]})")
        print(f"Expected: {expected} (binary: {bin(expected)[2:]})")
        print(f"Got: {result} (binary: {bin(result)[2:]})")
        if result != expected:
            print(f"Note: Check bit manipulation logic")
        print("-" * 40)

if __name__ == "__main__":
    test_number_complement()
