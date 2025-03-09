"""
LeetCode 311 - Sparse Matrix Multiplication

Problem Statement:
Given two sparse matrices mat1 of size m x k and mat2 of size k x n,
return their multiplication. A sparse matrix has most elements equal to 0.

Logic:
1. Optimize matrix multiplication for sparse matrices:
   - Skip computations when encountering zeros
   - Only multiply non-zero elements
2. For each cell in result matrix:
   - Only process when mat1[i][j] != 0
   - Only multiply with non-zero elements in mat2
3. Time complexity: O(m*k*n) worst case, but much better for sparse matrices
"""

from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(k):
                if mat1[i][j] != 0:
                    for l in range(n):
                        if mat2[j][l] != 0:
                            result[i][l] += mat1[i][j] * mat2[j][l]

        return result

def test_sparse_matrix_multiply():
    solution = Solution()
    
    # Test cases
    test_cases = [
        {
            'mat1': [[1,0,0],[-1,0,3]],
            'mat2': [[7,0,0],[0,0,0],[0,0,1]],
            'expected': [[7,0,0],[-7,0,3]]
        },
        {
            'mat1': [[0]],
            'mat2': [[0]],
            'expected': [[0]]
        },
        {
            'mat1': [[1,0],[0,1]],
            'mat2': [[1,1],[1,1]],
            'expected': [[1,1],[1,1]]
        },
        {
            'mat1': [[1,2,3],[4,5,6]],
            'mat2': [[7,8],[9,10],[11,12]],
            'expected': [[58,64],[139,154]]
        }
    ]
    
    for i, test_case in enumerate(test_cases):
        result = solution.multiply(test_case['mat1'], test_case['mat2'])
        assert result == test_case['expected'], \
            f"Test case {i + 1} failed: expected {test_case['expected']}, got {result}"
        print(f"Test case {i + 1} passed:")
        print("Matrix 1:")
        for row in test_case['mat1']: print(row)
        print("Matrix 2:")
        for row in test_case['mat2']: print(row)
        print("Result:")
        for row in result: print(row)
        print()

if __name__ == "__main__":
    test_sparse_matrix_multiply()
    print("All test cases passed!")