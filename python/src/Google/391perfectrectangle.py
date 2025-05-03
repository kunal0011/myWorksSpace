"""
LeetCode 391 - Perfect Rectangle

Problem Statement:
Given an array rectangles where rectangles[i] = [xi, yi, ai, bi] represents an axis-aligned rectangle with:
- Bottom-left corner at (xi, yi)
- Top-right corner at (ai, bi)
Return true if all the rectangles together form an exact cover of a rectangular region with no overlaps.

The solution uses a corner point counting approach:
1. All interior points must appear even number of times (as they are shared by rectangles)
2. Only the four corners of the perfect rectangle should appear once
3. Total area of small rectangles must equal area of the perfect rectangle

Time Complexity: O(n), where n is the number of rectangles
Space Complexity: O(n) for storing corner points
"""

class Solution:
    def isRectangleCover(self, rectangles: list[list[int]]) -> bool:
        # Set to store corners
        corners = set()
        
        # Track area and boundary
        area = 0
        min_x = float('inf')
        min_y = float('inf')
        max_x = float('-inf')
        max_y = float('-inf')
        
        for x, y, a, b in rectangles:
            # Update boundaries
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, a)
            max_y = max(max_y, b)
            
            # Calculate area
            area += (a - x) * (b - y)
            
            # Track corners using XOR operation with tuples
            # If a point appears even times, it will be removed from set
            for corner in [(x, y), (x, b), (a, y), (a, b)]:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)
        
        # Check if remaining corners are exactly the four corners of the perfect rectangle
        if corners != {(min_x, min_y), (min_x, max_y), 
                      (max_x, min_y), (max_x, max_y)}:
            return False
        
        # Check if area matches
        return area == (max_x - min_x) * (max_y - min_y)


def test_perfect_rectangle():
    solution = Solution()
    
    # Test cases
    test_cases = [
        (
            [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]],
            True,
            "Basic valid perfect rectangle"
        ),
        (
            [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]],
            False,
            "Invalid: gap in the middle"
        ),
        (
            [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]],
            False,
            "Invalid: overlap between rectangles"
        ),
        (
            [[0,0,1,1],[0,1,1,2],[1,0,2,1],[1,1,2,2]],
            True,
            "Valid 2x2 perfect rectangle"
        ),
        (
            [[0,0,1,1],[0,0,2,1],[1,0,2,1],[0,2,2,3]],
            False,
            "Invalid: overlap and gap"
        )
    ]
    
    for i, (rectangles, expected, description) in enumerate(test_cases, 1):
        result = solution.isRectangleCover(rectangles)
        print(f"Test case {i} - {description}:")
        print(f"Rectangles: {rectangles}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Pass: {result == expected}\n")


if __name__ == "__main__":
    test_perfect_rectangle()