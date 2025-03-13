"""
LeetCode 738: Monotone Increasing Digits

Given an integer n, return the largest number that is less than or equal to n 
with monotone increasing digits.

A number has monotone increasing digits if and only if each pair of adjacent digits x and y 
satisfy x <= y.

Example 1:
Input: n = 10
Output: 9
Explanation: 9 is the largest number less than 10 with monotone increasing digits.

Example 2:
Input: n = 1234
Output: 1234
Explanation: 1234 is already monotone increasing.

Example 3:
Input: n = 332
Output: 299
Explanation: 299 is the largest number less than 332 with monotone increasing digits.

Constraints:
0 <= n <= 10^9
"""

class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        # Edge cases
        if N < 10:
            return N
            
        # Convert number to string for easier manipulation
        s = list(str(N))
        n = len(s)
        
        # Find the rightmost pair where left > right
        i = 1
        while i < n and s[i-1] <= s[i]:
            i += 1
            
        # If already monotone increasing, return original number
        if i == n:
            return N
            
        # Find the leftmost digit that needs to be decreased
        while i > 0 and s[i-1] > s[i]:
            s[i-1] = str(int(s[i-1]) - 1)
            i -= 1
            
        # Fill rest with '9's
        return int(str(''.join(s[:i+1])) + '9' * (n-i-1))


def test_monotone_increasing_digits():
    """Test function with comprehensive test cases"""
    solution = Solution()
    test_cases = [
        # Basic test cases
        (10, 9),
        (1234, 1234),
        (332, 299),
        
        # Edge cases
        (0, 0),
        (9, 9),
        
        # Complex cases
        (100, 99),
        (1000, 999),
        (2333, 2333),
        (23332, 22999),
        (98765, 89999),
        
        # Special cases
        (120, 119),
        (321, 299),
        (333, 333),
        (1234321, 1233999)
    ]

    for i, (test_input, expected) in enumerate(test_cases, 1):
        result = solution.monotoneIncreasingDigits(test_input)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status}")
        print(f"Input: {test_input}")
        print(f"Expected: {expected}")
        print(f"Got: {result}\n")

if __name__ == "__main__":
    test_monotone_increasing_digits()
