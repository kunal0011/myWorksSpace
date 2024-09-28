from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        # Initialize the height array where heights[j] is the current height of column j
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        # Iterate through each row
        for i in range(rows):
            for j in range(cols):
                # Update the height of the histogram: if it's '1', increase height by 1, otherwise reset to 0
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Compute the maximal rectangle for the current histogram (row as base)
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        # Helper function to calculate largest rectangle in a histogram
        stack = []
        max_area = 0
        # Sentinel to flush out remaining heights in the stack
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

        heights.pop()  # Remove the sentinel
        return max_area
