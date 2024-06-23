from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0

        # Variables to track if first row and first column need to be zeroed
        first_row_zero = False
        first_col_zero = False

        # Check if first row should be zeroed
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Check if first column should be zeroed
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Use first row and first column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Nullify rows based on markers in first column
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        # Nullify columns based on markers in first row
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # Nullify first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Nullify first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


if __name__ == '__main__':
    s = Solution()
    print(s.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
