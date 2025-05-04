"""
LeetCode 1844. Replace All Digits with Characters

Problem Statement:
You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.
There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.
For example, shift('a', 2) = 'c' (shift 'a' by 2 positions to get 'c')
For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).
Return s after replacing all digits.

Time Complexity: O(n) where n is length of string
Space Complexity: O(n) for result array
"""


class Solution:
    def replaceDigits(self, s: str) -> str:
        # Logic:
        # 1. Iterate through string indices
        # 2. For even indices, keep the character as is
        # 3. For odd indices, replace digit with shifted character:
        #    - Take previous character (s[i-1])
        #    - Add digit value to its ASCII code
        #    - Convert back to character

        result = []

        for i in range(len(s)):
            if i % 2 == 0:
                result.append(s[i])
            else:
                result.append(chr(ord(s[i - 1]) + int(s[i])))

        return ''.join(result)


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        "a1c1e1",       # Expected: "abcdef"
        "a1b2c3d4e",    # Expected: "abbdcfeg"
        "v0g6",         # Expected: "vvm"
        "z1",           # Expected: "za"
    ]

    for i, test_str in enumerate(test_cases):
        result = solution.replaceDigits(test_str)
        print(f"Test case {i + 1}:")
        print(f"Input string: {test_str}")
        print(f"Output string: {result}")

        # Show the shift operations for better understanding
        print("Step by step replacement:")
        for j in range(1, len(test_str), 2):
            if j < len(test_str):
                prev_char = test_str[j-1]
                digit = int(test_str[j])
                new_char = chr(ord(prev_char) + digit)
                print(f"  shift('{prev_char}', {digit}) = '{new_char}'")
        print()
