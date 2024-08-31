from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort the balloons by their end points
        points.sort(key=lambda x: x[1])

        arrows = 1
        current_end = points[0][1]

        for i in range(1, len(points)):
            if points[i][0] > current_end:
                # If the start of the current balloon is after the end of the last one
                arrows += 1
                current_end = points[i][1]

        return arrows
