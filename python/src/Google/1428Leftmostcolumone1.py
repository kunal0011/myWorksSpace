"""
LeetCode 1428: Leftmost Column with at Least a One
Problem Statement:
A binary matrix means that all elements are either 0 or 1. For each individual row of the matrix, 
this row is sorted in non-decreasing order.
Given a row-sorted binary matrix, find the leftmost column index with a 1 in it.
Constraints:
- rows == mat.length
- cols == mat[i].length
- 1 <= rows, cols <= 100
- mat[i][j] is either 0 or 1.
- mat[i] is sorted in non-decreasing order.
"""


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        """
        Logic: Use the property that matrix is row-sorted to optimize the search
        1. Start from top-right corner
        2. If current element is 1, move left (there might be more 1s to the left)
        3. If current element is 0, move down (no 1s will be to the left in current row)
        4. Continue until we either find leftmost 1 or determine no 1 exists

        Time Complexity: O(M + N) where M is rows and N is columns
        Space Complexity: O(1)
        """
        rows, cols = binaryMatrix.dimensions()

        # Start from the top-right corner
        row, col = 0, cols - 1
        leftmost_col = -1

        # Traverse the matrix
        while row < rows and col >= 0:
            if binaryMatrix.get(row, col) == 1:
                leftmost_col = col  # Update leftmost_col when a 1 is found
                col -= 1  # Move left to find if there's another 1
            else:
                row += 1  # Current position is 0, check next row

        return leftmost_col


class BinaryMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.calls = 0  # Track number of get() calls for optimization check

    def get(self, x, y):
        self.calls += 1
        if 0 <= x < len(self.matrix) and 0 <= y < len(self.matrix[0]):
            return self.matrix[x][y]
        else:
            raise IndexError("Index out of bounds")

    def dimensions(self):
        return [len(self.matrix), len(self.matrix[0])]


# Test driver
def run_tests():
    test_cases = [
        # Test Case 1: Standard case
        [
            [0, 0, 0, 1],
            [0, 0, 1, 1],
            [0, 1, 1, 1]
        ],
        # Test Case 2: No ones
        [
            [0, 0, 0],
            [0, 0, 0]
        ],
        # Test Case 3: All ones
        [
            [1, 1, 1],
            [1, 1, 1]
        ],
        # Test Case 4: Single column with one
        [
            [0],
            [1]
        ]
    ]

    solution = Solution()
    for i, matrix in enumerate(test_cases, 1):
        binary_matrix = BinaryMatrix(matrix)
        result = solution.leftMostColumnWithOne(binary_matrix)
        print(f"\nTest Case {i}:")
        print(f"Matrix: {matrix}")
        print(f"Leftmost column with 1: {result}")
        print(f"Number of get() calls: {binary_matrix.calls}")


if __name__ == "__main__":
    run_tests()
