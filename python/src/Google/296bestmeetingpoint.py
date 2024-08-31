from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        # Get the list of x-coordinates and y-coordinates of all homes
        rows = []
        cols = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)

        # The best meeting point is at the median of the sorted coordinates
        rows.sort()
        cols.sort()

        median_row = rows[len(rows) // 2]
        median_col = cols[len(cols) // 2]

        # Calculate the total distance to the median point
        distance = sum(abs(r - median_row) for r in rows) + \
            sum(abs(c - median_col) for c in cols)

        return distance
