"""
LeetCode 378: Kth Smallest Element in a Sorted Matrix

Given an n x n matrix where each row and column is sorted in ascending order, find the kth smallest element in the matrix.
Note that it's the kth smallest element in the sorted order, not the kth distinct element.

Example:
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
Output: 13

The matrix has the following properties:
1. Each row is sorted in ascending order
2. Each column is sorted in ascending order
3. Matrix is n x n (square matrix)

Time Complexity: O(k * log(min(k,n))) where n is the size of matrix
Space Complexity: O(min(k,n))
"""

import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        n = len(matrix)
        min_heap = []
        
        # Optimization: We only need to consider up to k rows initially
        # Add the first element of first k rows to the heap
        for i in range(min(n, k)):
            heapq.heappush(min_heap, (matrix[i][0], i, 0))  # (value, row, col)
        
        # Find kth element
        result = 0
        for _ in range(k):
            val, row, col = heapq.heappop(min_heap)
            result = val
            
            # If there are more elements in this row, add the next one
            if col + 1 < n:
                heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
                
        return result


def run_test_cases() -> None:
    """Function to run comprehensive test cases"""
    solution = Solution()
    
    # Test case 1: Basic case
    matrix1 = [
        [1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k1 = 8
    result1 = solution.kthSmallest(matrix1, k1)
    print(f"\nTest Case 1:")
    print(f"Matrix = {matrix1}")
    print(f"k = {k1}")
    print(f"Expected: 13")
    print(f"Got: {result1}")
    print(f"Result: {'PASSED' if result1 == 13 else 'FAILED'}")
    
    # Test case 2: 1x1 matrix
    matrix2 = [[1]]
    k2 = 1
    result2 = solution.kthSmallest(matrix2, k2)
    print(f"\nTest Case 2:")
    print(f"Matrix = {matrix2}")
    print(f"k = {k2}")
    print(f"Expected: 1")
    print(f"Got: {result2}")
    print(f"Result: {'PASSED' if result2 == 1 else 'FAILED'}")
    
    # Test case 3: 2x2 matrix
    matrix3 = [
        [1, 2],
        [3, 4]
    ]
    k3 = 3
    result3 = solution.kthSmallest(matrix3, k3)
    print(f"\nTest Case 3:")
    print(f"Matrix = {matrix3}")
    print(f"k = {k3}")
    print(f"Expected: 3")
    print(f"Got: {result3}")
    print(f"Result: {'PASSED' if result3 == 3 else 'FAILED'}")
    
    # Test case 4: Matrix with duplicates
    matrix4 = [
        [1, 2, 2],
        [2, 3, 3],
        [2, 3, 4]
    ]
    k4 = 4
    result4 = solution.kthSmallest(matrix4, k4)
    print(f"\nTest Case 4:")
    print(f"Matrix = {matrix4}")
    print(f"k = {k4}")
    print(f"Expected: 2")
    print(f"Got: {result4}")
    print(f"Result: {'PASSED' if result4 == 2 else 'FAILED'}")
    
    # Test case 5: Empty matrix
    matrix5 = []
    k5 = 1
    result5 = solution.kthSmallest(matrix5, k5)
    print(f"\nTest Case 5:")
    print(f"Matrix = {matrix5}")
    print(f"k = {k5}")
    print(f"Expected: 0")
    print(f"Got: {result5}")
    print(f"Result: {'PASSED' if result5 == 0 else 'FAILED'}")


if __name__ == "__main__":
    run_test_cases()
