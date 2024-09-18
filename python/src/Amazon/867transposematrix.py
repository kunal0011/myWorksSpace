class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        # Transpose the matrix
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # Expected output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print(sol.transpose(matrix1))

    # Test case 2
    matrix2 = [[1, 2, 3], [4, 5, 6]]
    print(sol.transpose(matrix2))  # Expected output: [[1, 4], [2, 5], [3, 6]]
