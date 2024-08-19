class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        reversed_number = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            # Extract the last digit
            digit = x % 10
            x //= 10

            # Check for overflow
            if (reversed_number > (INT_MAX - digit) // 10):
                return 0

            # Update the reversed number
            reversed_number = reversed_number * 10 + digit

        return sign * reversed_number


# Example usage
solution = Solution()
print(solution.reverse(123))   # Output: 321
print(solution.reverse(-123))  # Output: -321
print(solution.reverse(120))   # Output: 21
print(solution.reverse(1534236469))  # Output: 0 (overflow)
