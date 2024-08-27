class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()

        # Start from the top-right corner
        row, col = 0, cols - 1
        leftmost_col = -1

        # Traverse the matrix
        while row < rows and col >= 0:
            if binaryMatrix.get(row, col) == 1:
                leftmost_col = col  # Update leftmost_col when a 1 is found
                col -= 1  # Move left
            else:
                row += 1  # Move down

        return leftmost_col


class BinaryMatrix:
    def __init__(self, matrix):
        # Initialize the BinaryMatrix with a given 2D list (matrix)
        self.matrix = matrix

    def get(self, x, y):
        # Return the element at position (x, y) in the matrix
        if 0 <= x < len(self.matrix) and 0 <= y < len(self.matrix[0]):
            return self.matrix[x][y]
        else:
            raise IndexError("Index out of bounds")

    def dimensions(self):
        # Return the dimensions of the matrix as a list [rows, cols]
        return [len(self.matrix), len(self.matrix[0])]


# Example usage
matrix = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1]
]

binary_matrix = BinaryMatrix(matrix)
print(binary_matrix.get(1, 2))  # Output: 1
print(binary_matrix.dimensions())  # Output: [3, 4]
