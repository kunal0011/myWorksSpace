from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            mid_row = mid // n
            mid_col = mid % n

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix(
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60))
