"""
LeetCode 402 - Remove K Digits

Given string num representing a non-negative integer and integer k,
return the smallest possible integer after removing k digits from num.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all digits, the number is 0.
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Edge case: if k equals length of num, return "0"
        if k >= len(num):
            return "0"
        
        # Use stack to keep track of digits
        stack = []
        
        # Process each digit
        for digit in num:
            # Remove digits that are larger than current digit
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If k > 0, remove remaining digits from the end
        while k > 0:
            stack.pop()
            k -= 1
        
        # Construct the result
        result = ''.join(stack)
        
        # Remove leading zeros
        result = result.lstrip('0')
        
        # Return "0" if result is empty
        return result if result else "0"


# Test driver
def main():
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("1432219", 3),  # Should return "1219"
        ("10200", 1),    # Should return "200"
        ("10", 2),       # Should return "0"
        ("112", 1),      # Should return "11"
        ("1234567890", 9)  # Should return "0"
    ]
    
    for num, k in test_cases:
        result = solution.removeKdigits(num, k)
        print(f"\nInput: num = {num}, k = {k}")
        print(f"Output: {result}")


if __name__ == "__main__":
    main()