class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize the result and carry
        result = []
        carry = 0

        # Initialize two pointers for the strings a and b
        i, j = len(a) - 1, len(b) - 1

        # Traverse both strings from the end to the beginning
        while i >= 0 or j >= 0 or carry:
            # Get the current digit from a and b, or 0 if out of bounds
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            # Compute the sum of the digits and the carry
            total = digit_a + digit_b + carry
            carry = total // 2  # Update carry
            result.append(str(total % 2))  # Append the current bit to result

            # Move to the next digits
            i -= 1
            j -= 1

        # Since the result is built backwards, reverse it at the end
        return ''.join(reversed(result))
