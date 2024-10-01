from collections import defaultdict
from math import gcd
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        max_points = 0

        for i in range(len(points)):
            slopes = defaultdict(int)
            duplicates = 1  # Count the point itself
            curr_max = 0

            for j in range(i + 1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx == 0 and dy == 0:
                    # Same point as i
                    duplicates += 1
                    continue

                # Normalize the slope by GCD
                g = gcd(dx, dy)
                dx //= g
                dy //= g

                # Ensure consistent handling of signs
                if dx < 0:
                    dx = -dx
                    dy = -dy
                elif dx == 0:
                    # Vertical line, always normalize dy to be positive
                    dy = abs(dy)

                slopes[(dx, dy)] += 1
                curr_max = max(curr_max, slopes[(dx, dy)])

            # Add the duplicates to the max points found for the current point
            max_points = max(max_points, curr_max + duplicates)

        return max_points
