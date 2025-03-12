"""
LeetCode 415 - Add Strings

Problem Statement:
-----------------
Given two non-negative integers num1 and num2 represented as strings, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.

Key Points:
----------
1. Both numbers are non-negative integers represented as strings
2. Cannot use built-in big integer libraries
3. Cannot convert the entire string to integer directly
4. Must handle arbitrary length numbers
5. Must perform digit-by-digit addition with carry

Examples:
--------
Input: num1 = "11", num2 = "123"
Output: "134"

Input: num1 = "456", num2 = "77"
Output: "533"

Input: num1 = "0", num2 = "0"
Output: "0"

Constraints:
-----------
* 1 <= num1.length, num2.length <= 10^4
* num1 and num2 consist of only digits
* num1 and num2 don't have any leading zeros except for the zero itself
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        Add two numbers represented as strings.
        
        Time Complexity: O(max(N,M)) where N and M are lengths of input strings
        Space Complexity: O(max(N,M)) to store the result
        """
        i, j = len(num1) - 1, len(num2) - 1  # Pointers to the last digits
        carry = 0
        result = []

        # Process digits from right to left
        while i >= 0 or j >= 0 or carry:
            # Get digit from num1 or 0 if exhausted
            n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            # Get digit from num2 or 0 if exhausted
            n2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            # Calculate sum and new carry
            total = n1 + n2 + carry
            carry = total // 10
            result.append(str(total % 10))

            i -= 1
            j -= 1

        # Join and reverse the result
        return ''.join(reversed(result)) if result else "0"

def test_add_strings():
    """
    Test driver for the add strings problem
    """
    test_cases = [
        ("11", "123", "134"),  # Different length numbers
        ("456", "77", "533"),  # Different length numbers
        ("0", "0", "0"),  # Zero case
        ("1", "9", "10"),  # Simple carry case
        ("999", "1", "1000"),  # Multiple carries
        ("9133", "0", "9133"),  # Adding zero
        ("98", "9", "107"),  # Carry propagation
        ("9999999", "1", "10000000"),  # Large carry propagation
        ("1234567890", "9876543210", "11111111100"),  # Large numbers
    ]
    
    solution = Solution()
    
    for i, (num1, num2, expected) in enumerate(test_cases, 1):
        result = solution.addStrings(num1, num2)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test case {i}: {status}")
        print(f"Input: num1 = {num1}, num2 = {num2}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print("-" * 40)

if __name__ == "__main__":
    test_add_strings()
