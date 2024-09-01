class Solution:
    def findBlackPixel(self, picture, N):
        m, n = len(picture), len(picture[0])

        # Count the number of black pixels in each row and column
        row_count = [0] * m
        col_count = [0] * n
        rows = ["".join(row) for row in picture]

        # Count black pixels in rows and columns
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    row_count[i] += 1
                    col_count[j] += 1

        # Find valid rows and count lonely pixels
        count = 0
        for i in range(m):
            if row_count[i] == N:
                for j in range(n):
                    if picture[i][j] == 'B' and col_count[j] == N:
                        # Check if all rows with a 'B' in column j are the same as row i
                        if rows.count(rows[i]) == N:
                            count += 1

        return count
