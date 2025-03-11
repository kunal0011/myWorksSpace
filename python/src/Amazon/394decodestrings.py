"""
LeetCode 394: Decode String

Problem Statement:
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets 
is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Time Complexity: O(n), where n is the length of the decoded string
Space Complexity: O(m), where m is the length of the input string
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_string = ""
        
        for char in s:
            if char.isdigit():
                # Build the number before '['
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Save the current state and start a new one
                stack.append((current_string, current_num))
                current_string = ""
                current_num = 0
            elif char == ']':
                # Pop previous state and apply multiplication
                prev_string, num = stack.pop()
                current_string = prev_string + num * current_string
            else:
                # Add characters to current string
                current_string += char
                
        return current_string

def test_decode_string():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()
    
    test_cases = [
        {
            "s": "3[a]2[bc]",
            "expected": "aaabcbc",
            "description": "Basic case with different patterns"
        },
        {
            "s": "3[a2[c]]",
            "expected": "accaccacc",
            "description": "Nested brackets"
        },
        {
            "s": "2[abc]3[cd]ef",
            "expected": "abcabccdcdcdef",
            "description": "Multiple patterns with suffix"
        },
        {
            "s": "abc3[cd]xyz",
            "expected": "abccdcdcdxyz",
            "description": "Pattern with prefix and suffix"
        },
        {
            "s": "10[a]",
            "expected": "aaaaaaaaaa",
            "description": "Two-digit number"
        },
        {
            "s": "2[3[a]b]",
            "expected": "aaabaaab",
            "description": "Complex nested pattern"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        s = test_case["s"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"Input: s = '{s}'")
        
        result = solution.decodeString(s)
        assert result == expected, f"Expected '{expected}', but got '{result}'"
        print(f"✓ Test case passed! Output: '{result}'")

if __name__ == "__main__":
    test_decode_string()
    print("\nAll test cases passed! 🎉")
