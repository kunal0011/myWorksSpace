class Solution:
    def findComplement(self, num: int) -> int:
        # Get the bit length of num
        bit_length = num.bit_length()
        # Create a mask with all bits set to 1 (same length as num)
        mask = (1 << bit_length) - 1
        # XOR num with the mask to get the complement
        return num ^ mask


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    num1 = 5
    print(sol.findComplement(num1))  # Expected output: 2

    # Test case 2
    num2 = 1
    print(sol.findComplement(num2))  # Expected output: 0
