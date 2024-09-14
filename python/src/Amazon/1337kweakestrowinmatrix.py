class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        # Create a list of (number_of_ones, row_index)
        row_strengths = [(sum(row), i) for i, row in enumerate(mat)]

        # Sort the list by number_of_ones and then by row_index
        row_strengths.sort()

        # Extract the indices of the k weakest rows
        return [row_strengths[i][1] for i in range(k)]
