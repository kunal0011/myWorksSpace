class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        size = 0

        # First pass: find the length of the fully decoded string
        for char in S:
            if char.isdigit():
                # Multiply the size when we encounter a digit
                size *= int(char)
            else:
                size += 1  # Increase the size for each letter

        # Second pass: work backwards to find the K-th character
        for i in range(len(S) - 1, -1, -1):
            K %= size  # Reduce K to be within the current size

            if K == 0 and S[i].isalpha():  # If K == 0 and we hit a letter, return it
                return S[i]

            if S[i].isdigit():
                size //= int(S[i])  # Divide size by the digit value
            else:
                size -= 1  # Decrease size for each letter


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    S1 = "leet2code3"
    K1 = 10
    print(sol.decodeAtIndex(S1, K1))  # Expected output: "o"

    # Test case 2
    S2 = "ha22"
    K2 = 5
    print(sol.decodeAtIndex(S2, K2))  # Expected output: "h"

    # Test case 3
    S3 = "a2345678999999999999999"
    K3 = 1
    print(sol.decodeAtIndex(S3, K3))  # Expected output: "a"
