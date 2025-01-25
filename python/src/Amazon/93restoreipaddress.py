"""
LeetCode 93. Restore IP Addresses

Problem Statement:
A valid IP address consists of exactly four integers separated by single dots.
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

Given a string s containing only digits, return all possible valid IP addresses
that can be formed by inserting dots into s. You are not allowed to reorder or
remove any digits in s. You may return the valid IP addresses in any order.

Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

Constraints:
- 1 <= s.length <= 20
- s contains only digits
"""


class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        def is_valid_part(part: str) -> bool:
            # Check if part is valid:
            # 1. Length between 1 and 3
            # 2. No leading zeros unless single digit
            # 3. Value between 0 and 255
            if len(part) > 3 or len(part) == 0:
                return False
            if len(part) > 1 and part[0] == '0':
                return False
            return 0 <= int(part) <= 255

        def backtrack(start: int, parts: list[str]):
            # If we have 4 parts and used all digits, we found a valid IP
            if len(parts) == 4 and start == len(s):
                result.append('.'.join(parts))
                return

            # If we have 4 parts but haven't used all digits, or
            # we've used all digits but don't have 4 parts, invalid
            if len(parts) == 4 or start == len(s):
                return

            # Try different lengths for the next part
            for i in range(1, 4):
                if start + i <= len(s):
                    part = s[start:start + i]
                    if is_valid_part(part):
                        parts.append(part)
                        backtrack(start + i, parts)
                        parts.pop()

        result = []
        backtrack(0, [])
        return result


def visualize_ip_formation(s: str, ip: str) -> str:
    """Helper function to visualize how an IP address is formed"""
    parts = ip.split('.')
    result = []
    pos = 0

    for part in parts:
        if pos > 0:
            result.append('.')
        result.append(part)
        pos += len(part) + 1

    return ''.join(result)


def test_restore_ip_addresses():
    solution = Solution()

    test_cases = [
        {
            "s": "25525511135",
            "expected": ["255.255.11.135", "255.255.111.35"],
            "description": "Standard case"
        },
        {
            "s": "0000",
            "expected": ["0.0.0.0"],
            "description": "All zeros"
        },
        {
            "s": "101023",
            "expected": [
                "1.0.10.23", "1.0.102.3", "10.1.0.23",
                "10.10.2.3", "101.0.2.3"
            ],
            "description": "Multiple valid combinations"
        },
        {
            "s": "1111",
            "expected": ["1.1.1.1"],
            "description": "Single digits"
        },
        {
            "s": "010010",
            "expected": ["0.10.0.10", "0.100.1.0"],
            "description": "Leading zeros"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        s = test_case["s"]
        expected = sorted(test_case["expected"])
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"Input string: {s}")

        result = sorted(solution.restoreIpAddresses(s))

        print("\nPossible IP addresses:")
        for ip in result:
            print(f"  {visualize_ip_formation(s, ip)}")

        assert result == expected, \
            f"Expected {expected}, but got {result}"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_restore_ip_addresses()
    print("\nAll test cases passed! 🎉")
