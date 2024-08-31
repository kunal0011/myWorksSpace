from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        min_x, min_y = float('inf'), float('inf')
        max_x, max_y = float('-inf'), float('-inf')
        points = set()
        area = 0

        for x1, y1, x2, y2 in rectangles:
            # Calculate the total area of all small rectangles
            area += (x2 - x1) * (y2 - y1)

            # Update the bounding rectangle coordinates
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            # Store the points
            for point in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if point in points:
                    points.remove(point)
                else:
                    points.add(point)

        # The area of the bounding rectangle
        bounding_area = (max_x - min_x) * (max_y - min_y)

        # There should only be four points left in the set: the corners of the bounding rectangle
        if points != {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)}:
            return False

        # The area of all rectangles should equal the area of the bounding rectangle
        return area == bounding_area
