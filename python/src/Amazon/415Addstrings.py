class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1  # Pointers to the last digits
        carry = 0
        result = []

        # Loop through both numbers starting from the last digit
        while i >= 0 or j >= 0 or carry:
            # Get digit from num1 or 0 if out of bounds
            n1 = int(num1[i]) if i >= 0 else 0
            # Get digit from num2 or 0 if out of bounds
            n2 = int(num2[j]) if j >= 0 else 0

            total = n1 + n2 + carry  # Add the digits and the carry
            carry = total // 10  # Carry will be 1 if total is 10 or more
            # Append the last digit to the result
            result.append(str(total % 10))

            i -= 1  # Move to the next digit in num1
            j -= 1  # Move to the next digit in num2

        # The result is currently in reverse order, so reverse it back
        return ''.join(reversed(result))
