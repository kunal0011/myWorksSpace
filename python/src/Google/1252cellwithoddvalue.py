class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        row_count = [0] * m
        col_count = [0] * n

        # Apply operations to row_count and col_count
        for r, c in indices:
            row_count[r] += 1
            col_count[c] += 1

        # Count cells with odd values
        odd_cells = 0

        for r in range(m):
            for c in range(n):
                if (row_count[r] + col_count[c]) % 2 == 1:
                    odd_cells += 1

        return odd_cells
