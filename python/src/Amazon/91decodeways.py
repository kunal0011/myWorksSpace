"""
LeetCode 91. Decode Ways

Problem Statement:
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters 
using the reverse of the mapping above (there may be multiple ways).
Given a string s containing only digits, return the number of ways to decode it.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" since "6" is different from "06".

Constraints:
- 1 <= s.length <= 100
- s contains only digits and may contain leading zero(s).
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        # dp[i] represents number of ways to decode s[0:i]
        dp = [0] * (len(s) + 1)
        dp[0] = 1  # Empty string
        dp[1] = 1  # First character

        for i in range(2, len(s) + 1):
            # Check if single digit is valid
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            # Check if two digits are valid
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]

        return dp[len(s)]


def visualize_decoding(s: str) -> None:
    """Helper function to visualize all possible decodings"""
    def decode(s: str, start: int, curr: list[str], result: list[str]):
        if start == len(s):
            result.append(' '.join(curr))
            return

        # Try single digit
        if s[start] != '0':
            digit = int(s[start])
            char = chr(ord('A') + digit - 1)
            curr.append(char)
            decode(s, start + 1, curr, result)
            curr.pop()

        # Try two digits
        if start + 1 < len(s):
            two_digits = int(s[start:start+2])
            if 10 <= two_digits <= 26:
                char = chr(ord('A') + two_digits - 1)
                curr.append(char)
                decode(s, start + 2, curr, result)
                curr.pop()

    result = []
    decode(s, 0, [], result)
    return result


def test_num_decodings():
    solution = Solution()

    test_cases = [
        {
            "s": "12",
            "expected": 2,
            "description": "Basic case"
        },
        {
            "s": "226",
            "expected": 3,
            "description": "Multiple ways"
        },
        {
            "s": "06",
            "expected": 0,
            "description": "Leading zero"
        },
        {
            "s": "27",
            "expected": 1,
            "description": "Single way"
        },
        {
            "s": "1201234",
            "expected": 3,
            "description": "Complex case"
        },
        {
            "s": "0",
            "expected": 0,
            "description": "Single zero"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        s = test_case["s"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"Input: s = '{s}'")

        result = solution.numDecodings(s)

        assert result == expected, \
            f"Expected {expected}, but got {result}"

        # Show possible decodings if result > 0
        if result > 0:
            decodings = visualize_decoding(s)
            print("Possible decodings:")
            for decoding in decodings:
                print(f"  {decoding}")

        print("✓ Test case passed!")


if __name__ == "__main__":
    test_num_decodings()
    print("\nAll test cases passed! 🎉")
