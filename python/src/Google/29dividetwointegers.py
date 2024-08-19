class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -(2**31)

        # Handle edge cases
        if dividend == 0:
            return 0
        if divisor == 0:
            raise ValueError("Divisor cannot be 0")
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT  # Overflow case

        # Determine the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Use absolute values for calculation
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)

        quotient = 0

        # Subtract divisor from dividend using bit shifts
        while abs_dividend >= abs_divisor:
            temp_divisor = abs_divisor
            multiple = 1

            while abs_dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1

            abs_dividend -= temp_divisor
            quotient += multiple

        # Apply the sign to the quotient
        quotient = sign * quotient

        # Ensure the result is within the 32-bit signed integer bounds
        return min(max(quotient, MIN_INT), MAX_INT)
