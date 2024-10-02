from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(numRows):
            # Start each row with 1
            row = [1] * (i + 1)
            # Fill in the values in between the 1s
            for j in range(1, i):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
            # Append the row to the result
            res.append(row)

        return res
