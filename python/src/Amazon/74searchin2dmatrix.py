"""
LeetCode 74. Search a 2D Matrix

Problem Statement:
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Explanation: 3 exists in the matrix.

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
Explanation: 13 does not exist in the matrix.
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            # Convert mid to matrix indices
            row, col = mid // n, mid % n
            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


def print_matrix_with_highlight(matrix: list[list[int]], highlight: tuple = None,
                                search_range: tuple = None) -> None:
    """Helper function to print matrix with optional highlighting"""
    m, n = len(matrix), len(matrix[0])

    # Print column numbers
    print("   ", end="")
    for j in range(n):
        print(f"{j:3}", end=" ")
    print("\n   " + "----" * n)

    for i in range(m):
        print(f"{i:2}|", end=" ")
        for j in range(n):
            if highlight and (i, j) == highlight:
                print(f"\033[92m{matrix[i][j]:3}\033[0m", end=" ")
            elif search_range and search_range[0] <= i * n + j <= search_range[1]:
                print(f"\033[93m{matrix[i][j]:3}\033[0m", end=" ")
            else:
                print(f"{matrix[i][j]:3}", end=" ")
        print()


def explain_matrix_search(matrix: list[list[int]], target: int) -> None:
    """
    Function to explain the matrix search process step by step
    """
    print(f"\nSearching for target {target} in matrix:")
    print("=" * 50)

    if not matrix or not matrix[0]:
        print("Matrix is empty!")
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    print("\nInitial matrix:")
    print_matrix_with_highlight(matrix)

    print(f"\nTreating matrix as sorted array from 0 to {m*n - 1}")
    flattened = [num for row in matrix for num in row]
    print(f"Flattened array: {flattened}")

    iteration = 1
    while left <= right:
        mid = (left + right) // 2
        row, col = mid // n, mid % n
        value = matrix[row][col]

        print(f"\nIteration {iteration}:")
        print(f"Search range: [{left}, {right}]")
        print(f"Middle index: {mid} (row={row}, col={col})")
        print(f"Current value: {value}")

        print("\nCurrent search state:")
        print_matrix_with_highlight(matrix, (row, col), (left, right))

        if value == target:
            print(f"\nTarget {target} found at position ({row}, {col})!")
            return True
        elif value < target:
            print(
                f"Value {value} is less than target {target}, searching right half")
            left = mid + 1
        else:
            print(
                f"Value {value} is greater than target {target}, searching left half")
            right = mid - 1

        iteration += 1

    print(f"\nTarget {target} not found in matrix")
    return False


def test_search_matrix():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "matrix": [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
            "target": 3,
            "expected": True,
            "description": "Target exists"
        },
        {
            "matrix": [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
            "target": 13,
            "expected": False,
            "description": "Target doesn't exist"
        },
        {
            "matrix": [[1]],
            "target": 1,
            "expected": True,
            "description": "Single element matrix"
        },
        {
            "matrix": [[1, 3, 5], [7, 9, 11]],
            "target": 9,
            "expected": True,
            "description": "Middle element"
        },
        {
            "matrix": [[1, 3, 5], [7, 9, 11]],
            "target": 12,
            "expected": False,
            "description": "Target greater than all elements"
        },
        {
            "matrix": [[1, 3, 5], [7, 9, 11]],
            "target": 0,
            "expected": False,
            "description": "Target less than all elements"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        matrix = test_case["matrix"]
        target = test_case["target"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Target: {target}")
        print("Matrix:")
        print_matrix_with_highlight(matrix)

        result = solution.searchMatrix(matrix, target)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_search_matrix()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_matrix_search(
            [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
        explain_matrix_search(
            [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
