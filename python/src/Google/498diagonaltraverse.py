"""
LeetCode 498 - Diagonal Traverse

Problem Statement:
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Example:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Explanation: Elements are visited in diagonal order going up-right, then down-left, alternating direction.

Time Complexity: O(m*n) where m and n are dimensions of matrix
Space Complexity: O(1) excluding the space needed for output array
"""


def findDiagonalOrder(mat: list[list[int]]) -> list[int]:
    if not mat or not mat[0]:
        return []

    m, n = len(mat), len(mat[0])
    result = []
    row = col = 0
    going_up = True

    while len(result) < m * n:
        result.append(mat[row][col])

        if going_up:
            if col == n-1:          # Reached last column
                row += 1
                going_up = False
            elif row == 0:          # Reached first row
                col += 1
                going_up = False
            else:                   # Keep going up
                row -= 1
                col += 1
        else:
            if row == m-1:          # Reached last row
                col += 1
                going_up = True
            elif col == 0:          # Reached first column
                row += 1
                going_up = True
            else:                   # Keep going down
                row += 1
                col -= 1

    return result

# Test driver


def run_tests():
    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 4, 7, 5, 3, 6, 8, 9]),
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
        ([[1]], [1]),
        ([], []),
        ([[1, 2, 3]], [1, 2, 3])
    ]

    for i, (matrix, expected) in enumerate(test_cases, 1):
        result = findDiagonalOrder(matrix)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status}")
        print(f"Input: {matrix}")
        print(f"Expected: {expected}")
        print(f"Got: {result}\n")


if __name__ == "__main__":
    run_tests()
