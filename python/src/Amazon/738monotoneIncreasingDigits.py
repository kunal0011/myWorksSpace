class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        digits = list(str(N))  # Convert the number to a list of digits
        length = len(digits)
        mark = length  # Mark where we need to set digits to '9'

        # Traverse the digits from right to left
        for i in range(length - 1, 0, -1):
            if digits[i] < digits[i - 1]:  # Find where the monotone property is broken
                mark = i
                # Decrease the problematic digit
                digits[i - 1] = str(int(digits[i - 1]) - 1)

        # Set all digits after the mark to '9'
        for i in range(mark, length):
            digits[i] = '9'

        # Convert the list of digits back to an integer
        return int("".join(digits))
