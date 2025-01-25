from typing import List

"""
LeetCode 54. Spiral Matrix

Problem Statement:
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse right
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # Traverse down
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # Traverse left
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                # Traverse up
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result


def explain_spiral_order(matrix: List[List[int]]) -> None:
    """
    Function to explain the spiral traversal process step by step
    """
    print(f"\nTraversing matrix in spiral order:")
    for row in matrix:
        print(row)
    print("=" * 50)

    def print_matrix_with_path(matrix: List[List[int]],
                               visited: List[List[bool]],
                               current: tuple = None) -> None:
        """Print matrix with path and current position"""
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if current and (i, j) == current:
                    print("*", end="\t")  # Current position
                elif visited[i][j]:
                    print("•", end="\t")  # Visited
                else:
                    print(matrix[i][j], end="\t")
            print()
        print()

    if not matrix:
        print("Empty matrix")
        return []

    m, n = len(matrix), len(matrix[0])
    visited = [[False] * n for _ in range(m)]
    result = []

    top, bottom = 0, m - 1
    left, right = 0, n - 1

    while top <= bottom and left <= right:
        print("Current boundaries:")
        print(f"Top: {top}, Bottom: {bottom}, Left: {left}, Right: {right}\n")

        # Traverse right
        print("Traversing right →")
        for j in range(left, right + 1):
            result.append(matrix[top][j])
            visited[top][j] = True
            print(f"Adding {matrix[top][j]}")
            print_matrix_with_path(matrix, visited, (top, j))
        top += 1

        # Traverse down
        print("Traversing down ↓")
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
            visited[i][right] = True
            print(f"Adding {matrix[i][right]}")
            print_matrix_with_path(matrix, visited, (i, right))
        right -= 1

        if top <= bottom:
            # Traverse left
            print("Traversing left ←")
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
                visited[bottom][j] = True
                print(f"Adding {matrix[bottom][j]}")
                print_matrix_with_path(matrix, visited, (bottom, j))
            bottom -= 1

        if left <= right:
            # Traverse up
            print("Traversing up ↑")
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
                visited[i][left] = True
                print(f"Adding {matrix[i][left]}")
                print_matrix_with_path(matrix, visited, (i, left))
            left += 1

    print("\nFinal result:", result)
    return result


def test_spiral_order():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "expected": [1, 2, 3, 6, 9, 8, 7, 4, 5],
            "description": "3x3 matrix"
        },
        {
            "matrix": [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            "expected": [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
            "description": "3x4 matrix"
        },
        {
            "matrix": [[1]],
            "expected": [1],
            "description": "1x1 matrix"
        },
        {
            "matrix": [[1, 2], [3, 4]],
            "expected": [1, 2, 4, 3],
            "description": "2x2 matrix"
        },
        {
            "matrix": [[1, 2, 3]],
            "expected": [1, 2, 3],
            "description": "1x3 matrix"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        matrix = test_case["matrix"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print("Input matrix:")
        for row in matrix:
            print(row)

        result = solution.spiralOrder(matrix)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_spiral_order()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        explain_spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
