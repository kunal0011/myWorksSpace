"""
LeetCode 1727. Largest Submatrix With Rearrangements

Problem Statement:
You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns
of the matrix in any order. Return the area of the largest submatrix within matrix where every 
element of the submatrix is 1 after reordering the columns optimally.

Time Complexity: O(m*n*log(n)) where m is rows and n is columns
Space Complexity: O(m*n) for heights array
"""

from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # Logic:
        # 1. For each column, calculate heights of consecutive 1's from top to bottom
        # 2. For each row:
        #    - Sort heights in descending order (simulating optimal column rearrangement)
        #    - For each width j+1, calculate area using minimum height in that range
        # 3. Keep track of maximum area found

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


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        [[0, 0, 1], [1, 1, 1], [1, 0, 1]],  # Expected: 4
        [[1, 0, 1, 0, 1]],              # Expected: 3
        [[1, 1, 0], [1, 0, 1]],          # Expected: 2
        [[0, 0], [0, 0]],              # Expected: 0
    ]

    for i, matrix in enumerate(test_cases):
        result = solution.largestSubmatrix(matrix)
        print(f"Test case {i + 1}:")
        print("Matrix:")
        for row in matrix:
            print(row)
        print(f"Largest submatrix area: {result}")
        print()
