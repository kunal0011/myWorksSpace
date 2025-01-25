from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False

        # Check if first row has any zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break

        # Check if first column has any zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        # Use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set zeros based on markers (except first row and column)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Set first row to zero if needed
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Set first column to zero if needed
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0


def print_matrix(matrix: List[List[int]], highlight: tuple = None) -> None:
    """Helper function to print matrix with optional highlighting"""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if highlight and (i, j) == highlight:
                print(f"\033[92m{matrix[i][j]}\033[0m", end=" ")
            else:
                print(matrix[i][j], end=" ")
        print()


def explain_set_zeroes(matrix: List[List[int]]) -> None:
    """
    Function to explain the matrix zeroing process step by step
    """
    print("\nSetting matrix zeroes")
    print("=" * 50)

    print("\nOriginal matrix:")
    print_matrix(matrix)

    m, n = len(matrix), len(matrix[0])
    matrix_copy = [row[:] for row in matrix]  # Create a copy for demonstration

    # Check first row and column
    first_row_has_zero = False
    first_col_has_zero = False

    print("\nStep 1: Checking first row for zeros")
    for j in range(n):
        if matrix_copy[0][j] == 0:
            first_row_has_zero = True
            print(f"Found zero at position (0,{j})")
            break

    print("\nStep 2: Checking first column for zeros")
    for i in range(m):
        if matrix_copy[i][0] == 0:
            first_col_has_zero = True
            print(f"Found zero at position ({i},0)")
            break

    print("\nStep 3: Using first row and column as markers")
    for i in range(1, m):
        for j in range(1, n):
            if matrix_copy[i][j] == 0:
                print(
                    f"Found zero at ({i},{j}), marking row {i} and column {j}")
                matrix_copy[i][0] = 0
                matrix_copy[0][j] = 0
                print("Current matrix state:")
                print_matrix(matrix_copy)

    print("\nStep 4: Setting zeros based on markers")
    for i in range(1, m):
        for j in range(1, n):
            if matrix_copy[i][0] == 0 or matrix_copy[0][j] == 0:
                matrix_copy[i][j] = 0

    print("\nStep 5: Handling first row and column")
    if first_row_has_zero:
        print("Setting first row to zero")
        for j in range(n):
            matrix_copy[0][j] = 0

    if first_col_has_zero:
        print("Setting first column to zero")
        for i in range(m):
            matrix_copy[i][0] = 0

    print("\nFinal matrix:")
    print_matrix(matrix_copy)


def test_set_zeroes():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "matrix": [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
            "expected": [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
            "description": "Basic case"
        },
        {
            "matrix": [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
            "expected": [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
            "description": "Multiple zeros"
        },
        {
            "matrix": [[1, 0]],
            "expected": [[0, 0]],
            "description": "Single row"
        },
        {
            "matrix": [[1], [0]],
            "expected": [[0], [0]],
            "description": "Single column"
        },
        {
            "matrix": [[0]],
            "expected": [[0]],
            "description": "Single element"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        matrix = [row[:] for row in test_case["matrix"]]  # Create a copy
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print("Input matrix:")
        print_matrix(matrix)

        solution.setZeroes(matrix)

        assert matrix == expected, \
            f"\nTest case {i} failed!\nExpected:\n{expected}\nGot:\n{matrix}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_set_zeroes()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_set_zeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        explain_set_zeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
