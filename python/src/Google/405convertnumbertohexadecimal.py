class Solution:
    def toHex(self, num: int) -> str:
        # Edge case for zero
        if num == 0:
            return "0"

        # Mapping for hexadecimal digits
        hex_map = "0123456789abcdef"

        # For negative numbers, convert to 32-bit two's complement representation
        if num < 0:
            num += 2**32

        hex_str = []

        # Convert to hexadecimal
        while num > 0:
            hex_str.append(hex_map[num & 15])  # Get the last 4 bits as hex
            num >>= 4  # Right shift by 4 bits to process the next set of bits

        # Reverse the list and join to form the final hexadecimal string
        return ''.join(reversed(hex_str))
