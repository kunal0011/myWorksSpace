class Solution:
    def minOperations(self, target: list[int]) -> int:
        operations = 0
        max_double_ops = 0

        # Iterate over each number in the target array
        for num in target:
            double_ops = 0

            # Reduce the number to zero
            while num > 0:
                # If num is odd, subtract 1 (this is a reverse increment operation)
                if num % 2 == 1:
                    num -= 1
                    operations += 1  # Count the increment operation

                # If num is still greater than 0, divide by 2 (this is a reverse doubling operation)
                if num > 0:
                    num //= 2
                    double_ops += 1  # Count the doubling operation

            # Track the maximum number of doubling operations
            max_double_ops = max(max_double_ops, double_ops)

        # Total operations = increment operations + max doubling operations
        return operations + max_double_ops
