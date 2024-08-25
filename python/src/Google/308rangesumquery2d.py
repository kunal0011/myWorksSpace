class NumMatrix:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            return

        self.rows, self.cols = len(matrix), len(matrix[0])
        self.tree = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        self.matrix = [[0] * self.cols for _ in range(self.rows)]

        for r in range(self.rows):
            for c in range(self.cols):
                self.update(r, c, matrix[r][c])

    def update(self, row, col, val):
        if not self.rows or not self.cols:
            return

        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        r = row + 1

        while r <= self.rows:
            c = col + 1
            while c <= self.cols:
                self.tree[r][c] += delta
                c += (c & -c)
            r += (r & -r)

    def sumRegion(self, row1, col1, row2, col2):
        if not self.rows or not self.cols:
            return 0

        return (self._sum(row2 + 1, col2 + 1)
                - self._sum(row1, col2 + 1)
                - self._sum(row2 + 1, col1)
                + self._sum(row1, col1))

    def _sum(self, row, col):
        res = 0
        r = row

        while r > 0:
            c = col
            while c > 0:
                res += self.tree[r][c]
                c -= (c & -c)
            r -= (r & -r)

        return res
