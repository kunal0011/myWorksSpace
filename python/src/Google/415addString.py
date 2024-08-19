class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1  # Pointers for both strings
        carry = 0
        result = []

        # Loop through both strings from the last digit to the first
        while i >= 0 or j >= 0 or carry:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0

            # Sum of the current digits and the carry
            current_sum = n1 + n2 + carry
            carry = current_sum // 10  # Update the carry for next iteration
            # Add the current digit to the result
            result.append(str(current_sum % 10))

            i -= 1  # Move to the previous digit in num1
            j -= 1  # Move to the previous digit in num2

        # Since we added digits from least significant to most, reverse the result
        return ''.join(result[::-1])
