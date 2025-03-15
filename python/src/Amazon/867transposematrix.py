"""
LeetCode 867: Transpose Matrix

Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, 
switching the matrix's row and column indices.

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 1000
- 1 <= matrix[i][j] <= 10^5
"""

from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        # Initialize result matrix with correct dimensions
        result = [[0] * m for _ in range(n)]
        
        # Fill the transposed matrix
        for i in range(m):
            for j in range(n):
                result[j][i] = matrix[i][j]
                
        return result

def validate_matrix(matrix: List[List[int]]) -> bool:
    """Validate matrix according to constraints"""
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    if not (1 <= m <= 1000 and 1 <= n <= 1000):
        return False
        
    return all(1 <= x <= 10**5 for row in matrix for x in row)

def print_matrix(matrix: List[List[int]], label: str = "Matrix"):
    """Pretty print matrix"""
    print(f"\n{label}:")
    for row in matrix:
        print(" ".join(f"{x:4d}" for x in row))

def test_transpose():
    """Test function for Matrix Transpose"""
    test_cases = [
        ([[1,2,3],[4,5,6],[7,8,9]], [[1,4,7],[2,5,8],[3,6,9]]),
        ([[1,2,3],[4,5,6]], [[1,4],[2,5],[3,6]]),
        ([[1]], [[1]]),
        ([[1,2]], [[1],[2]]),
        ([[1,2,3,4],[5,6,7,8]], [[1,5],[2,6],[3,7],[4,8]])
    ]
    
    solution = Solution()
    
    for i, (matrix, expected) in enumerate(test_cases, 1):
        is_valid = validate_matrix(matrix)
        result = solution.transpose(matrix)
        
        print(f"\nTest case {i}:")
        print_matrix(matrix, "Input Matrix")
        print_matrix(result, "Transposed Matrix")
        print(f"Dimensions: {len(matrix)}x{len(matrix[0])} → {len(result)}x{len(result[0])}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        # Verify transpose properties
        if len(matrix) == len(matrix[0]):  # Square matrix
            double_transpose = solution.transpose(result)
            print(f"Double transpose equals original: {'✓' if double_transpose == matrix else '✗'}")

if __name__ == "__main__":
    test_transpose()
