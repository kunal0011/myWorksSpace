class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1.0

        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n > 0:
            if n % 2 == 1:  # If n is odd
                result *= x
            x *= x  # Square x
            n //= 2  # Divide n by 2
        return result
