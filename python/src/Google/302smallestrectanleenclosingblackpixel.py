"""
LeetCode 302 - Smallest Rectangle Enclosing Black Pixels

Problem Statement:
You are given an m x n binary matrix image where 0 represents a white pixel and 1 represents a black pixel.
The black pixels are connected (i.e., there is only one black region).
Pixels are connected horizontally and vertically.
Given two integers x and y that represents the location of one of the black pixels,
return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

Time Complexity: O(m * log n + n * log m) where m and n are dimensions of the matrix
Space Complexity: O(1)
"""

def minArea(image, x, y):
    if not image or not image[0]:
        return 0
    
    m, n = len(image), len(image[0])
    
    def searchColumns(i, j, top, option):
        while i < j:
            mid = (i + j) // 2
            found = False
            
            # Search this column for any black pixel
            for k in range(m):
                if image[k][mid] == '1':
                    found = True
                    break
            
            if found == option:
                j = mid
            else:
                i = mid + 1
        return i
    
    def searchRows(i, j, left, option):
        while i < j:
            mid = (i + j) // 2
            found = False
            
            # Search this row for any black pixel
            for k in range(n):
                if image[mid][k] == '1':
                    found = True
                    break
            
            if found == option:
                j = mid
            else:
                i = mid + 1
        return i
    
    # Binary search for boundaries
    left = searchColumns(0, y, True, True)
    right = searchColumns(y + 1, n, False, False)
    top = searchRows(0, x, True, True)
    bottom = searchRows(x + 1, m, False, False)
    
    return (right - left) * (bottom - top)

# Example usage
if __name__ == "__main__":
    image = [
        "0010",
        "0110",
        "0100"
    ]
    x, y = 0, 2  # One of the black pixels
    print(f"Smallest rectangle area: {minArea(image, x, y)}")  # Output: 6