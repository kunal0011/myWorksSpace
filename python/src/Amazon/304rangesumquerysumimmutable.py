from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return

        self.rows, self.cols = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]

        # Calculate prefix sum
        for r in range(1, self.rows + 1):
            for c in range(1, self.cols + 1):
                self.prefix_sum[r][c] = (
                    matrix[r-1][c-1] +
                    self.prefix_sum[r-1][c] +
                    self.prefix_sum[r][c-1] -
                    self.prefix_sum[r-1][c-1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Using the inclusion-exclusion principle
        return (
            self.prefix_sum[row2 + 1][col2 + 1]
            - self.prefix_sum[row1][col2 + 1]
            - self.prefix_sum[row2 + 1][col1]
            + self.prefix_sum[row1][col1]
        )
