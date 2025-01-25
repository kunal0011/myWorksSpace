from typing import List

"""
LeetCode 48. Rotate Image

Problem Statement:
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:
- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000

Solution Logic:
1. First transpose the matrix (swap elements across main diagonal)
2. Then reverse each row
This effectively rotates the matrix 90 degrees clockwise
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the matrix in-place
        """
        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()


def print_matrix(matrix: List[List[int]], message: str = "") -> None:
    """
    Helper function to print matrix in a readable format
    """
    if message:
        print(message)
    for row in matrix:
        print(row)
    print()


def explain_rotation(matrix: List[List[int]]) -> None:
    """
    Function to explain the rotation process step by step
    """
    print(f"\nRotating matrix 90 degrees clockwise:")
    print("=" * 50)

    print_matrix(matrix, "Original matrix:")

    n = len(matrix)

    # Step 1: Transpose
    print("Step 1: Transpose the matrix")
    print("Swapping elements across main diagonal...")

    for i in range(n):
        for j in range(i, n):
            if i != j:
                print(
                    f"Swap ({i},{j})={matrix[i][j]} with ({j},{i})={matrix[j][i]}")
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            if i != j:
                print_matrix(matrix, "After swap:")

    print_matrix(matrix, "After transpose:")

    # Step 2: Reverse rows
    print("Step 2: Reverse each row")
    for i in range(n):
        print(f"Reversing row {i}: {matrix[i]}")
        matrix[i].reverse()
        print(f"After reverse: {matrix[i]}")

    print_matrix(matrix, "Final rotated matrix:")


def test_rotate():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "expected": [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
            "description": "3x3 matrix"
        },
        {
            "matrix": [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
            "expected": [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
            "description": "4x4 matrix"
        },
        {
            "matrix": [[1]],
            "expected": [[1]],
            "description": "1x1 matrix"
        },
        {
            "matrix": [[1, 2], [3, 4]],
            "expected": [[3, 1], [4, 2]],
            "description": "2x2 matrix"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        matrix = [row[:] for row in test_case["matrix"]]  # Deep copy
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print("Input matrix:")
        print_matrix(matrix)

        solution.rotate(matrix)

        assert matrix == expected, \
            f"\nTest case {i} failed!\nExpected:\n{expected}\nGot:\n{matrix}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_rotate()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_rotation([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        explain_rotation([[1, 2], [3, 4]])
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
