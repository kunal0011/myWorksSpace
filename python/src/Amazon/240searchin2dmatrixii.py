"""
LeetCode 240 - Search a 2D Matrix II

Problem Statement:
Write an efficient algorithm that searches for a value target in an m x n integer matrix.
This matrix has the following properties:
- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

Solution Logic:
1. Start from top-right corner
2. Use matrix properties for efficient search:
   - If current > target, move left (smaller values)
   - If current < target, move down (larger values)
   - If current == target, found!
3. Time: O(m + n), Space: O(1)
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        # Start from the top-right corner
        row = 0
        col = cols - 1

        while row < rows and col >= 0:
            current = matrix[row][col]
            if current == target:
                return True
            elif current > target:
                col -= 1  # Move left
            else:
                row += 1  # Move down

        return False

def test_search_matrix():
    solution = Solution()
    
    # Test Case 1: Regular case
    matrix1 = [
        [1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30]
    ]
    target1 = 5
    print("Test 1: Target exists")
    print(f"Target: {target1}")
    print(f"Found: {solution.searchMatrix(matrix1, target1)}")  # Expected: True
    
    # Test Case 2: Target not found
    target2 = 20
    print("\nTest 2: Target doesn't exist")
    print(f"Target: {target2}")
    print(f"Found: {solution.searchMatrix(matrix1, target2)}")  # Expected: False
    
    # Test Case 3: Empty matrix
    matrix3 = []
    target3 = 1
    print("\nTest 3: Empty matrix")
    print(f"Target: {target3}")
    print(f"Found: {solution.searchMatrix(matrix3, target3)}")  # Expected: False
    
    # Test Case 4: Matrix with one element
    matrix4 = [[1]]
    target4 = 1
    print("\nTest 4: Single element matrix")
    print(f"Target: {target4}")
    print(f"Found: {solution.searchMatrix(matrix4, target4)}")  # Expected: True

if __name__ == "__main__":
    test_search_matrix()
