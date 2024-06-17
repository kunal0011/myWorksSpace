class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        count = 0
        max_val = 2**31 - 1
        min_val = -(2**31)
        flag = False
        left = 0
        right = dividend

        if dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
            right = max_val if dividend > max_val else dividend
        elif dividend < 0:
            dividend = -dividend
            flag = True
            right = max_val + 1 if dividend < max_val + 1 else dividend
        elif divisor < 0:
            divisor = -divisor
            flag = True
            right = max_val + 1 if dividend < max_val + 1 else dividend
        if dividend < right:
            right = -dividend if dividend < 0 else dividend

        if divisor > dividend:
            return 0
        elif divisor == dividend:
            return -1 if flag else 1

        while left <= right:

            mid = (left + right) // 2
            if mid * divisor == dividend:
                return -mid if flag else mid
            elif mid * divisor < dividend and (mid + 1) * divisor > dividend:
                return -mid if flag else mid
            elif (mid - 1) * divisor < dividend and mid * divisor > dividend:
                return -(mid - 1) if flag else (mid - 1)
            elif mid * divisor > dividend and (mid + 1) * divisor > dividend:
                right = mid - 1
            elif mid * divisor < dividend and (mid - 1) * divisor < dividend:
                left = mid + 1

        return min_val if flag else max_val


class Solution1:
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


if __name__ == "__main__":
    s = Solution1()
    print(s.divide(-231, 3))
