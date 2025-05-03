"""
LeetCode 405 - Convert a Number to Hexadecimal

Given an integer num, return a string representing its hexadecimal representation.
For negative integers, two's complement method is used.

All the letters in the answer string should be lowercase characters,
and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.

Example 1:
Input: num = 26
Output: "1a"

Example 2:
Input: num = -1
Output: "ffffffff"
Explanation: -1 in two's complement is 11111111111111111111111111111111 (32 bits)
             which in hexadecimal is ffffffff.
"""

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        # Handle negative numbers using 2's complement (32 bits)
        if num < 0:
            num = num + (1 << 32)
        
        # Hexadecimal digits
        hex_chars = "0123456789abcdef"
        result = []
        
        # Convert to hexadecimal
        while num > 0:
            digit = num & 15  # Same as num % 16
            result.append(hex_chars[digit])
            num = num >> 4    # Same as num // 16
        
        # Reverse and join the digits
        return ''.join(result[::-1])


# Test driver
def main():
    solution = Solution()
    
    # Test cases
    test_cases = [
        26,     # Should return "1a"
        -1,     # Should return "ffffffff"
        0,      # Should return "0"
        16,     # Should return "10"
        -2,     # Should return "fffffffe"
        255     # Should return "ff"
    ]
    
    for num in test_cases:
        result = solution.toHex(num)
        print(f"\nInput: num = {num}")
        print(f"Output: {result}")


if __name__ == "__main__":
    main()