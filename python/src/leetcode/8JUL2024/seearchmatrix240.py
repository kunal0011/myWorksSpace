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


# Example usage:
matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target = 5

solution = Solution()
print(solution.searchMatrix(matrix, target))  # Output: True

target = 20
print(solution.searchMatrix(matrix, target))  # Output: False
