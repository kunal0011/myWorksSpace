from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])

        # Calculate heights (number of consecutive 1's)
        heights = [[0] * n for _ in range(m)]

        for j in range(n):
            heights[0][j] = matrix[0][j]
            for i in range(1, m):
                if matrix[i][j] == 1:
                    heights[i][j] = heights[i-1][j] + 1

        max_area = 0

        for i in range(m):
            # Sort heights for the current row in descending order
            sorted_heights = sorted(heights[i], reverse=True)

            # Calculate maximum area with the current row's heights
            for j in range(n):
                max_area = max(max_area, sorted_heights[j] * (j + 1))

        return max_area
