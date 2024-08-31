class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # Shift the result to the left to make room for the next bit
            result <<= 1
            # Add the last bit of n to the result
            result |= n & 1
            # Shift n to the right to process the next bit
            n >>= 1
        return result
