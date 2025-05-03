"""
LeetCode 308 - Range Sum Query 2D - Mutable

Given a 2D matrix matrix, handle multiple queries of the following types:
1. Update the value of an element in matrix.
2. Calculate the sum of the elements of matrix inside the rectangle defined by 
   its upper left corner (row1, col1) and lower right corner (row2, col2).

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10

Time Complexity:
- Constructor: O(m*n)
- Update: O(log m * log n)
- SumRegion: O(log m * log n)
where m and n are the dimensions of the matrix

Space Complexity: O(m*n)

Uses Binary Indexed Tree (Fenwick Tree) for efficient updates and range queries.
"""

class NumMatrix:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            return

        self.rows, self.cols = len(matrix), len(matrix[0])
        self.tree = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        self.matrix = [[0] * self.cols for _ in range(self.rows)]

        for r in range(self.rows):
            for c in range(self.cols):
                self.update(r, c, matrix[r][c])

    def update(self, row, col, val):
        """
        Updates a value in the matrix and maintains the Binary Indexed Tree.
        
        The operation x & -x isolates the least significant 1-bit:
        Example: For x = 12 (1100 in binary)
        -x is 2's complement: -12 = ~12 + 1 = ...11110100
        x & -x = 1100 & 11110100 = 100 (= 4)
        
        In BIT context:
        - If we're at index 6 (110):
          6 & -6 = 2 -> Move to index 8 (next power of 2)
        - If we're at index 5 (101):
          5 & -5 = 1 -> Move to index 6 (next number)
        - If we're at index 8 (1000):
          8 & -8 = 8 -> Move to index 16 (next power of 2)
        
        This helps navigate the BIT structure efficiently by jumping
        to the next relevant index without checking every position.
        
        Time complexity: O(log m * log n) due to BIT updates
        """
        if not self.rows or not self.cols:
            return

        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        r = row + 1

        while r <= self.rows:
            c = col + 1
            while c <= self.cols:
                self.tree[r][c] += delta
                c += (c & -c)  # Move to next column that needs update
            r += (r & -r)      # Move to next row that needs update

    def sumRegion(self, row1, col1, row2, col2):
        if not self.rows or not self.cols:
            return 0

        return (self._sum(row2 + 1, col2 + 1)
                - self._sum(row1, col2 + 1)
                - self._sum(row2 + 1, col1)
                + self._sum(row1, col1))

    def _sum(self, row, col):
        """
        Helper method to calculate sum from (0,0) to (row,col).
        
        The x & -x operation works by:
        1. Taking a number x (e.g., 12 = 1100)
        2. Computing -x using 2's complement (~x + 1)
        3. AND operation isolates rightmost 1-bit
        
        Examples:
        - For 12 (1100): x & -x = 4 (100)
        - For 10 (1010): x & -x = 2 (10)
        - For 8 (1000): x & -x = 8 (1000)
        
        This helps efficiently traverse parent nodes in BIT.
        Time complexity: O(log m * log n) due to BIT traversal
        """
        res = 0
        r = row

        while r > 0:
            c = col
            while c > 0:
                res += self.tree[r][c]
                c -= (c & -c)  # Move to parent column in BIT
            r -= (r & -r)      # Move to parent row in BIT

        return res

def test_numMatrix():
    # Test Case 1: Basic functionality
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    num_matrix = NumMatrix(matrix)
    
    # Test sumRegion
    assert num_matrix.sumRegion(2, 1, 4, 3) == 8
    assert num_matrix.sumRegion(1, 1, 2, 2) == 11
    assert num_matrix.sumRegion(1, 2, 2, 4) == 12
    
    # Test update
    num_matrix.update(3, 2, 2)
    assert num_matrix.sumRegion(2, 1, 4, 3) == 10

    # Test Case 2: Edge cases
    empty_matrix = []
    assert NumMatrix(empty_matrix).sumRegion(0, 0, 0, 0) == 0

    single_cell = [[1]]
    num_matrix_single = NumMatrix(single_cell)
    assert num_matrix_single.sumRegion(0, 0, 0, 0) == 1
    num_matrix_single.update(0, 0, 5)
    assert num_matrix_single.sumRegion(0, 0, 0, 0) == 5

    # Test Case 3: Large matrix operations
    large_matrix = [[i + j for j in range(10)] for i in range(10)]
    num_matrix_large = NumMatrix(large_matrix)
    assert num_matrix_large.sumRegion(0, 0, 9, 9) == 900  # Sum of 0 to 18 in steps
    num_matrix_large.update(5, 5, 100)
    assert num_matrix_large.sumRegion(4, 4, 6, 6) > 0

    print("All test cases passed successfully!")

if __name__ == "__main__":
    test_numMatrix()
