class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIPv4(s: str) -> bool:
            # Split by '.' and check if there are exactly 4 parts
            parts = s.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                # Each part should be a digit, with no leading zeros unless it's exactly "0"
                if not part.isdigit() or not 0 <= int(part) <= 255 or (part[0] == '0' and len(part) > 1):
                    return False
            return True

        def isIPv6(s: str) -> bool:
            # Split by ':' and check if there are exactly 8 parts
            parts = s.split(':')
            if len(parts) != 8:
                return False
            hex_digits = "0123456789abcdefABCDEF"
            for part in parts:
                # Each part should be between 1 and 4 characters long, and all characters should be valid hex digits
                if not (1 <= len(part) <= 4) or any(c not in hex_digits for c in part):
                    return False
            return True

        # Check if the input is IPv4, IPv6, or neither
        if queryIP.count('.') == 3 and isIPv4(queryIP):
            return "IPv4"
        elif queryIP.count(':') == 7 and isIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    queryIP1 = "172.16.254.1"
    print(sol.validIPAddress(queryIP1))  # Expected output: "IPv4"

    # Test case 2
    queryIP2 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    print(sol.validIPAddress(queryIP2))  # Expected output: "IPv6"

    # Test case 3
    queryIP3 = "256.256.256.256"
    print(sol.validIPAddress(queryIP3))  # Expected output: "Neither"
