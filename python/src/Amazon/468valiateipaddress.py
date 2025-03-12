"""
LeetCode 468 - Validate IP Address

Problem Statement:
-----------------
Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address
or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where:
* 0 <= xi <= 255
* Each xi cannot contain leading zeros
* Each xi must be a decimal number

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:
* 1 <= xi.length <= 4
* xi is a hexadecimal string which may contain digits, lowercase ('a' to 'f') and uppercase ('A' to 'F')
* Leading zeros are allowed in xi

Examples:
--------
Input: queryIP = "172.16.254.1"
Output: "IPv4"

Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"

Input: queryIP = "256.256.256.256"
Output: "Neither"

Constraints:
-----------
* queryIP consists only of English letters, digits and the characters '.' and ':'.
"""

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        """
        Validate if the given string is a valid IPv4 or IPv6 address.
        
        Algorithm:
        1. First check the delimiter count to determine potential IP version
        2. For IPv4:
           - Split by '.' and validate each part
           - Check for valid decimal numbers between 0-255
           - Check for invalid leading zeros
        3. For IPv6:
           - Split by ':' and validate each part
           - Check for valid hex digits and length constraints
        
        Time Complexity: O(n) where n is length of queryIP
        Space Complexity: O(1) as we only use constant extra space
        """
        def isIPv4(s: str) -> bool:
            """
            Validate IPv4 address format.
            Must be exactly 4 parts, each 0-255, no leading zeros except single '0'.
            """
            try:
                parts = s.split('.')
                if len(parts) != 4:
                    return False
                    
                for part in parts:
                    # Check for empty parts or parts with length > 3
                    if not part or len(part) > 3:
                        return False
                    # Check for leading zeros
                    if len(part) > 1 and part[0] == '0':
                        return False
                    # Check numeric range
                    num = int(part)
                    if not 0 <= num <= 255:
                        return False
                return True
            except ValueError:
                return False

        def isIPv6(s: str) -> bool:
            """
            Validate IPv6 address format.
            Must be exactly 8 parts, each 1-4 hex digits.
            """
            try:
                parts = s.split(':')
                if len(parts) != 8:
                    return False
                    
                for part in parts:
                    # Check length constraints
                    if not 1 <= len(part) <= 4:
                        return False
                    # Validate hex digits
                    int(part, 16)  # Will raise ValueError if invalid hex
                return True
            except ValueError:
                return False

        # Main validation logic
        if '.' in queryIP:
            return "IPv4" if isIPv4(queryIP) else "Neither"
        elif ':' in queryIP:
            return "IPv6" if isIPv6(queryIP) else "Neither"
        return "Neither"


def test_ip_validation():
    """
    Comprehensive test driver for IP address validation
    """
    test_cases = [
        # IPv4 test cases
        (
            "172.16.254.1",
            "IPv4",
            "Basic valid IPv4 address"
        ),
        (
            "172.16.254.01",
            "Neither",
            "IPv4 with leading zero"
        ),
        (
            "172.16.256.1",
            "Neither",
            "IPv4 with value > 255"
        ),
        (
            "1.1.1.1",
            "IPv4",
            "IPv4 with single digits"
        ),
        (
            "01.01.01.01",
            "Neither",
            "IPv4 with leading zeros"
        ),
        
        # IPv6 test cases
        (
            "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
            "IPv6",
            "Basic valid IPv6 address"
        ),
        (
            "2001:db8:85a3:0:0:8A2E:0370:7334",
            "IPv6",
            "Valid IPv6 with mixed case"
        ),
        (
            "2001:0db8:85a3:0:0:8A2E:0370:7334:",
            "Neither",
            "IPv6 with extra colon"
        ),
        (
            "02001:0db8:85a3:0000:0000:8a2e:0370:7334",
            "Neither",
            "IPv6 with part > 4 characters"
        ),
        
        # Edge cases
        (
            "192.168.1.1.",
            "Neither",
            "IPv4 with trailing dot"
        ),
        (
            "1.2.3",
            "Neither",
            "IPv4 with too few parts"
        ),
        (
            "1:2:3:4:5:6:7",
            "Neither",
            "IPv6 with too few parts"
        ),
        (
            "1.2.3.4.5",
            "Neither",
            "IPv4 with too many parts"
        ),
        (
            "",
            "Neither",
            "Empty string"
        ),
        (
            "192.168.01.1",
            "Neither",
            "IPv4 with invalid leading zero"
        ),
        (
            "2001:0db8:85a3::8A2E:0370:7334",
            "Neither",
            "IPv6 with double colon shorthand (not allowed in this problem)"
        )
    ]
    
    solution = Solution()
    
    for i, (test_ip, expected, description) in enumerate(test_cases, 1):
        result = solution.validIPAddress(test_ip)
        status = "PASSED" if result == expected else "FAILED"
        print(f"\nTest case {i}: {status}")
        print(f"Description: {description}")
        print(f"Input IP: {test_ip}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        if result != expected:
            print(f"Note: Check validation rules for this case")
        print("-" * 40)

if __name__ == "__main__":
    test_ip_validation()
