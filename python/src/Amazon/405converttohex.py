class Solution:
    def toHex(self, num: int) -> str:
        """
        Convert an integer to hexadecimal representation.
        For negative numbers, uses two's complement method.
        
        Args:
            num: Integer number to convert (32-bit signed integer)
        Returns:
            str: Hexadecimal representation as a string
        """
        if num == 0:
            return "0"
            
        # Map for hex digits
        hex_chars = "0123456789abcdef"
        result = ""
        
        # Handle negative numbers using 32-bit two's complement
        # & with 0xFFFFFFFF to get unsigned 32-bit representation
        num &= 0xFFFFFFFF
        
        # Convert to hex by taking remainder with 16
        while num:
            result = hex_chars[num & 15] + result  # num & 15 is same as num % 16 but faster
            num >>= 4  # Right shift by 4 is same as num //= 16 but faster
            
        return result


def run_test_cases():
    """Test driver with various test cases"""
    solution = Solution()
    
    # Test cases: (input, expected_output)
    test_cases = [
        (26, "1a"),           # Positive number
        (-1, "ffffffff"),     # Negative number (two's complement)
        (0, "0"),            # Zero
        (16, "10"),          # Power of 16
        (-2, "fffffffe"),    # Negative number
        (2147483647, "7fffffff"),  # Max 32-bit integer
        (-2147483648, "80000000")  # Min 32-bit integer
    ]
    
    passed = 0
    total = len(test_cases)
    
    print("\nRunning test cases for Convert Number to Hexadecimal:")
    print("=" * 50)
    
    for i, (input_num, expected) in enumerate(test_cases, 1):
        result = solution.toHex(input_num)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test case {i}:")
        print(f"Input: {input_num}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Status: {status}")
        print("-" * 30)
        
        if status == "PASSED":
            passed += 1
    
    print(f"\nSummary: {passed}/{total} test cases passed")


if __name__ == "__main__":
    run_test_cases()
