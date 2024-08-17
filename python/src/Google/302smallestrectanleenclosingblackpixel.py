from typing import List

# You are given a 2D grid image where each cell is either black (1) or white (0). You are also given a starting pixel (sr, sc) that is guaranteed to be black. The task is to find the area of the smallest rectangle that can enclose all black pixels in the grid, using the starting pixel as a part of the rectangle.
# Define Binary Search Functions:

# Find Left Bound: Binary search to find the leftmost column that contains black pixels.
# Find Right Bound: Binary search to find the rightmost column that contains black pixels.
# Find Top Bound: Binary search to find the topmost row that contains black pixels.
# Find Bottom Bound: Binary search to find the bottommost row that contains black pixels.
# Binary Search Implementation:

# For each search function, adjust the search space based on whether the middle column or row contains black pixels.


class Solution:
    def minArea(self, image: List[List[str]], sr: int, sc: int) -> int:
        def has_black_pixel(x1, x2, y):
            return any(image[x][y] == '1' for x in range(x1, x2 + 1))

        def has_black_pixel_col(x, y1, y2):
            return any(image[x][y] == '1' for y in range(y1, y2 + 1))

        def binary_search_row(low, high, fixed_col, target_row, find_min):
            while low < high:
                mid = (low + high) // 2
                if has_black_pixel(mid, mid, fixed_col):
                    high = mid if find_min else mid - 1
                else:
                    low = mid + 1 if find_min else mid - 1
            return low

        def binary_search_col(low, high, fixed_row, target_col, find_min):
            while low < high:
                mid = (low + high) // 2
                if has_black_pixel(fixed_row, fixed_row, mid):
                    high = mid if find_min else mid - 1
                else:
                    low = mid + 1 if find_min else mid - 1
            return low

        rows, cols = len(image), len(image[0])
        top = binary_search_row(0, sr, sc, sr, True)
        bottom = binary_search_row(sr, rows - 1, sc, sr, False)
        left = binary_search_col(0, sc, sr, sc, True)
        right = binary_search_col(sc, cols - 1, sr, sc, False)

        return (bottom - top + 1) * (right - left + 1)
