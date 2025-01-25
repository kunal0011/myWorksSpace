from typing import List

"""
LeetCode 59. Spiral Matrix II

Problem Statement:
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Explanation: The output matrix should be filled in spiral order.

Example 2:
Input: n = 1
Output: [[1]]

Constraints:
- 1 <= n <= 20
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize matrix with zeros
        matrix = [[0] * n for _ in range(n)]

        # Define boundaries
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        num = 1

        while left <= right and top <= bottom:
            # Fill top row
            for j in range(left, right + 1):
                matrix[top][j] = num
                num += 1
            top += 1

            # Fill right column
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            if top <= bottom:
                # Fill bottom row
                for j in range(right, left - 1, -1):
                    matrix[bottom][j] = num
                    num += 1
                bottom -= 1

            if left <= right:
                # Fill left column
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1

        return matrix


def print_matrix(matrix: List[List[int]], highlight: tuple = None) -> None:
    """Helper function to print matrix with optional highlighting"""
    n = len(matrix)

    # Print column numbers
    print("   ", end="")
    for j in range(n):
        print(f"{j:2}", end=" ")
    print("\n   " + "---" * n)

    for i in range(n):
        print(f"{i:2}|", end=" ")
        for j in range(n):
            if highlight and (i, j) == highlight:
                print(f"\033[92m{matrix[i][j]:2}\033[0m", end=" ")
            else:
                print(f"{matrix[i][j]:2}", end=" ")
        print()
    print()


def explain_spiral_generation(n: int) -> None:
    """
    Function to explain the spiral matrix generation process step by step
    """
    print(f"\nGenerating {n}x{n} spiral matrix")
    print("=" * 50)

    matrix = [[0] * n for _ in range(n)]
    left, right = 0, n - 1
    top, bottom = 0, n - 1
    num = 1

    while left <= right and top <= bottom:
        # Fill top row
        print(f"\nFilling top row (row {top})")
        for j in range(left, right + 1):
            matrix[top][j] = num
            print(f"Setting position ({top},{j}) to {num}")
            print_matrix(matrix, (top, j))
            num += 1
        top += 1

        # Fill right column
        print(f"\nFilling right column (column {right})")
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            print(f"Setting position ({i},{right}) to {num}")
            print_matrix(matrix, (i, right))
            num += 1
        right -= 1

        if top <= bottom:
            # Fill bottom row
            print(f"\nFilling bottom row (row {bottom})")
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = num
                print(f"Setting position ({bottom},{j}) to {num}")
                print_matrix(matrix, (bottom, j))
                num += 1
            bottom -= 1

        if left <= right:
            # Fill left column
            print(f"\nFilling left column (column {left})")
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                print(f"Setting position ({i},{left}) to {num}")
                print_matrix(matrix, (i, left))
                num += 1
            left += 1

    print("\nFinal matrix:")
    print_matrix(matrix)
    return matrix


def test_spiral_matrix():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "n": 3,
            "expected": [[1, 2, 3], [8, 9, 4], [7, 6, 5]],
            "description": "3x3 matrix"
        },
        {
            "n": 1,
            "expected": [[1]],
            "description": "1x1 matrix"
        },
        {
            "n": 4,
            "expected": [
                [1, 2, 3, 4],
                [12, 13, 14, 5],
                [11, 16, 15, 6],
                [10, 9, 8, 7]
            ],
            "description": "4x4 matrix"
        },
        {
            "n": 2,
            "expected": [[1, 2], [4, 3]],
            "description": "2x2 matrix"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        n = test_case["n"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: n = {n}")

        result = solution.generateMatrix(n)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")
        print("\nGenerated matrix:")
        print_matrix(result)


if __name__ == "__main__":
    try:
        test_spiral_matrix()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_spiral_generation(3)
        explain_spiral_generation(4)
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
