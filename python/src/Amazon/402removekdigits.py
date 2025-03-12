"""
LeetCode 402: Remove K Digits

Problem Statement:
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

Logic:
1. Use monotonic stack approach:
   - Keep a stack of digits
   - For each digit, while k > 0 and stack top is larger than current digit, pop stack
   - This ensures we keep smallest possible sequence
2. Handle remaining k by removing from end
3. Remove leading zeros and handle empty result

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(n) for the stack
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"
            
        stack = []
        
        # Build monotonic increasing stack
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If we still need to remove digits, remove from the end
        while k > 0:
            stack.pop()
            k -= 1
        
        # Build result string
        result = ''.join(stack).lstrip('0')
        
        return result if result else "0"

def test_remove_k_digits():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()
    
    test_cases = [
        {
            "num": "1432219",
            "k": 3,
            "expected": "1219",
            "description": "Basic case with multiple removals"
        },
        {
            "num": "10200",
            "k": 1,
            "expected": "200",
            "description": "Remove leading digit with zeros"
        },
        {
            "num": "10",
            "k": 2,
            "expected": "0",
            "description": "Remove all digits"
        },
        {
            "num": "112",
            "k": 1,
            "expected": "11",
            "description": "Remove from middle"
        },
        {
            "num": "1234567890",
            "k": 9,
            "expected": "0",
            "description": "Remove all but one digit"
        },
        {
            "num": "9",
            "k": 1,
            "expected": "0",
            "description": "Single digit removal"
        },
        {
            "num": "10001",
            "k": 4,
            "expected": "0",
            "description": "Remove multiple zeros"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        num = test_case["num"]
        k = test_case["k"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"Input: num = '{num}', k = {k}")
        
        result = solution.removeKdigits(num, k)
        assert result == expected, f"Expected '{expected}', but got '{result}'"
        print(f"✓ Test case passed! Output: '{result}'")

if __name__ == "__main__":
    test_remove_k_digits()
    print("\nAll test cases passed! 🎉")
