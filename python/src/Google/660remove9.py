class Solution:
    def newInteger(self, n: int) -> int:
        # Convert the number `n` to its base-9 equivalent.
        # Since we're excluding the digit 9, the numbers are essentially base-9 numbers.
        res = 0
        base = 1
        while n > 0:
            res += (n % 9) * base
            n //= 9
            base *= 10
        return res
