"""
LeetCode 304 - Range Sum Query 2D - Immutable

Problem Statement:
Given a 2D matrix matrix, handle multiple queries of the following type:
- Calculate the sum of the elements of matrix inside the rectangle defined by its 
  upper left corner (row1, col1) and lower right corner (row2, col2).

Logic:
1. Use 2D prefix sum array for O(1) queries:
   - prefix_sum[i][j] = sum of all elements in rectangle (0,0) to (i-1,j-1)
2. For initialization:
   - Build (m+1) x (n+1) prefix sum array
   - Use dynamic programming: current cell = current value + left + top - diagonal
3. For sumRegion query:
   - Use inclusion-exclusion principle
   - Result = bottom-right - top - left + top-left
"""

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

def test_num_matrix():
    # Test cases
    test_cases = [
        {
            'matrix': [
                [3, 0, 1, 4, 2],
                [5, 6, 3, 2, 1],
                [1, 2, 0, 1, 5],
                [4, 1, 0, 1, 7],
                [1, 0, 3, 0, 5]
            ],
            'queries': [
                ((2, 1, 4, 3), 8),    # Region sum = 8
                ((1, 1, 2, 2), 11),   # Region sum = 11
                ((1, 2, 2, 4), 12)    # Region sum = 12
            ]
        },
        {
            'matrix': [[1]],
            'queries': [((0, 0, 0, 0), 1)]  # Single element
        },
        {
            'matrix': [[1, 2], [3, 4]],
            'queries': [((0, 0, 1, 1), 10)]  # Full matrix
        }
    ]
    
    for i, test_case in enumerate(test_cases):
        num_matrix = NumMatrix(test_case['matrix'])
        print(f"\nTest case {i + 1}:")
        print("Matrix:")
        for row in test_case['matrix']:
            print(row)
            
        for j, (query, expected) in enumerate(test_case['queries']):
            row1, col1, row2, col2 = query
            result = num_matrix.sumRegion(row1, col1, row2, col2)
            assert result == expected, f"Query {j + 1} failed: expected {expected}, got {result}"
            print(f"Query {j + 1}: sum({row1},{col1} to {row2},{col2}) = {result}")

if __name__ == "__main__":
    test_num_matrix()
    print("All test cases passed!")
