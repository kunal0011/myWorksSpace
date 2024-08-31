class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR the two numbers
        xor_result = x ^ y

        # Count the number of 1's in the binary representation of the result
        return bin(xor_result).count('1')
