from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from the second last row and move upwards
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Update the current cell with the minimum path sum
                triangle[row][col] += min(triangle[row + 1]
                                          [col], triangle[row + 1][col + 1])

        # The top element now contains the minimum path sum from top to bottom
        return triangle[0][0]
