class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        result = ""

        # Convert to 32-bit unsigned
        num &= 0xFFFFFFFF

        while num > 0:
            result = hex_chars[num % 16] + result
            num //= 16

        return result


# Example usage:
solution = Solution()
print(solution.toHex(26))     # Expected output: "1a"
print(solution.toHex(-1))     # Expected output: "ffffffff"
print(solution.toHex(0))      # Expected output: "0"
