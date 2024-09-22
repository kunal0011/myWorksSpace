class Solution:
    def numberOfArithmeticSlices(self, A: list[int]) -> int:
        if len(A) < 3:
            return 0

        count = 0
        current_slices = 0

        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                current_slices += 1
                count += current_slices
            else:
                current_slices = 0

        return count


# Example usage:
solution = Solution()
print(solution.numberOfArithmeticSlices([1, 2, 3, 4]))  # Expected output: 3
print(solution.numberOfArithmeticSlices([1]))           # Expected output: 0
print(solution.numberOfArithmeticSlices([1, 3, 5, 7, 9]))  # Expected output: 6
