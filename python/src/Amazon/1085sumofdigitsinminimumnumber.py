class Solution:
    def sumOfDigits(self, A: list[int]) -> int:
        # Step 1: Find the minimum number in the array
        min_num = min(A)

        # Step 2: Calculate the sum of its digits
        digit_sum = sum(int(digit) for digit in str(min_num))

        # Step 3: Return 1 if the sum is even, 0 if odd
        return 1 if digit_sum % 2 == 0 else 0
