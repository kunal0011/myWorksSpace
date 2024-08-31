class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1  # Check if the last bit is 1
            n >>= 1  # Right shift n by 1 to process the next bit
        return count
