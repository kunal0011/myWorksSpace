class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        direction = 1  # 1 for up-right, -1 for down-left
        row, col = 0, 0

        for _ in range(m * n):
            result.append(mat[row][col])

            # Move in the current direction
            if direction == 1:  # Moving up-right
                if col == n - 1:  # Hit the last column
                    row += 1
                    direction = -1
                elif row == 0:  # Hit the top row
                    col += 1
                    direction = -1
                else:
                    row -= 1
                    col += 1
            else:  # Moving down-left
                if row == m - 1:  # Hit the last row
                    col += 1
                    direction = 1
                elif col == 0:  # Hit the first column
                    row += 1
                    direction = 1
                else:
                    row += 1
                    col -= 1

        return result
