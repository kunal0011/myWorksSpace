"""
LeetCode 223 - Rectangle Area

Problem Statement:
Given the coordinates of two rectangles in a 2D plane, return the total area covered by the two rectangles.
The first rectangle is defined by its bottom-left corner (ax1, ay1) and top-right corner (ax2, ay2).
The second rectangle is defined by its bottom-left corner (bx1, by1) and top-right corner (bx2, by2).

Solution Logic:
1. Calculate individual areas of both rectangles
2. Find overlapping area:
   - Calculate overlap width: min(ax2,bx2) - max(ax1,bx1)
   - Calculate overlap height: min(ay2,by2) - max(ay1,by1)
   - If no overlap, width or height will be negative/zero
3. Total area = Area1 + Area2 - Overlap
4. Time: O(1), Space: O(1)
"""

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # Area of the first rectangle
        area1 = (ax2 - ax1) * (ay2 - ay1)
        # Area of the second rectangle
        area2 = (bx2 - bx1) * (by2 - by1)

        # Calculate overlap in the x dimension
        overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))
        # Calculate overlap in the y dimension
        overlap_height = max(0, min(ay2, by2) - max(ay1, by1))

        # Overlapping area
        overlap_area = overlap_width * overlap_height

        # Total area covered by both rectangles
        total_area = area1 + area2 - overlap_area

        return total_area

def test_rectangle_area():
    solution = Solution()
    
    # Test Case 1: Rectangles with overlap
    print("Test 1: Overlapping rectangles")
    result1 = solution.computeArea(-3, 0, 3, 4, 0, -1, 9, 2)
    print("Rectangle 1: (-3,0) to (3,4)")
    print("Rectangle 2: (0,-1) to (9,2)")
    print(f"Total area: {result1}")  # Expected: 45
    
    # Test Case 2: No overlap
    print("\nTest 2: Non-overlapping rectangles")
    result2 = solution.computeArea(-2, -2, 2, 2, 3, 3, 4, 4)
    print("Rectangle 1: (-2,-2) to (2,2)")
    print("Rectangle 2: (3,3) to (4,4)")
    print(f"Total area: {result2}")  # Expected: 17
    
    # Test Case 3: One rectangle inside another
    print("\nTest 3: Nested rectangles")
    result3 = solution.computeArea(-2, -2, 2, 2, -1, -1, 1, 1)
    print("Rectangle 1: (-2,-2) to (2,2)")
    print("Rectangle 2: (-1,-1) to (1,1)")
    print(f"Total area: {result3}")  # Expected: 16

if __name__ == "__main__":
    test_rectangle_area()
