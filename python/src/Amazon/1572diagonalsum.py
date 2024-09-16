class Solution:
    def diagonalSum(self, mat):
        n = len(mat)
        total_sum = 0

        for i in range(n):
            # Add primary diagonal element
            total_sum += mat[i][i]
            # Add secondary diagonal element
            total_sum += mat[i][n - 1 - i]

        # If the matrix has an odd size, subtract the middle element (it was counted twice)
        if n % 2 == 1:
            total_sum -= mat[n // 2][n // 2]

        return total_sum


# Testing
solution = Solution()
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Python Test Result:", solution.diagonalSum(mat))  # Output should be 25
