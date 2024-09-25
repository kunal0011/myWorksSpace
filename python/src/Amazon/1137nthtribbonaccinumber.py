class Solution:
    def tribonacci(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        # Initializing the first three values
        a, b, c = 0, 1, 1

        # Iterating from 3 to n
        for i in range(3, n + 1):
            trib = a + b + c  # Current Tribonacci number
            a, b, c = b, c, trib  # Update for the next iteration

        return c
