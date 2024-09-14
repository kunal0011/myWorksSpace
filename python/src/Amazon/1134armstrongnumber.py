class Solution:
    def isArmstrong(self, n: int) -> bool:
        # Convert the number to string to find digits
        digits = [int(d) for d in str(n)]
        num_digits = len(digits)

        # Calculate the sum of each digit raised to the power of the number of digits
        armstrong_sum = sum([d ** num_digits for d in digits])

        # Check if the sum equals the original number
        return armstrong_sum == n
