"""
LeetCode 415 - Add Strings

Given two non-negative integers num1 and num2 represented as strings, 
return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling 
large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Start from rightmost digits
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []
        
        # Process digits from right to left
        while i >= 0 or j >= 0 or carry:
            # Get digits or use 0 if exhausted
            x = ord(num1[i]) - ord('0') if i >= 0 else 0
            y = ord(num2[j]) - ord('0') if j >= 0 else 0
            
            # Calculate sum and carry
            total = x + y + carry
            carry = total // 10
            digit = total % 10
            
            # Add current digit to result
            result.append(str(digit))
            
            # Move pointers
            i -= 1
            j -= 1
        
        # Reverse and join the digits
        return ''.join(result[::-1])


# Test driver
def main():
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("11", "123"),      # Should return "134"
        ("456", "77"),      # Should return "533"
        ("0", "0"),         # Should return "0"
        ("1", "9"),         # Should return "10"
        ("999", "1"),       # Should return "1000"
        ("9133", "0"),      # Should return "9133"
        ("1234", "5678")    # Should return "6912"
    ]
    
    for num1, num2 in test_cases:
        result = solution.addStrings(num1, num2)
        print(f"\nInput: num1 = {num1}, num2 = {num2}")
        print(f"Output: {result}")


if __name__ == "__main__":
    main()