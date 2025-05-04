"""
LeetCode 1828. Queries on Number of Points Inside a Circle

Problem Statement:
You are given an array 'points' where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane.
Multiple points can have the same coordinates. You are also given an array 'queries' where queries[j] = [xj, yj, rj]
describes a circle centered at (xj, yj) with radius rj. For each query, compute the number of points inside the circle.
Points on the border of the circle are considered inside.

Time Complexity: O(Q*P) where Q is number of queries and P is number of points
Space Complexity: O(Q) for storing results
"""

from typing import List
import math


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Logic:
        # 1. For each query circle (x, y, r):
        #    - Check each point's distance to circle center
        #    - If distance <= radius, point is inside circle
        #    - Use distance formula: d = sqrt((x2-x1)^2 + (y2-y1)^2)
        #    - Square both sides to avoid sqrt: d^2 <= r^2
        # 2. Return array of counts for each query

        result = []

        for qx, qy, qr in queries:
            count = 0
            for px, py in points:
                if (qx - px) ** 2 + (qy - py) ** 2 <= qr ** 2:
                    count += 1
            result.append(count)

        return result


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        (
            [[1, 3], [3, 3], [5, 3], [2, 2]],
            [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
        ),  # Expected: [3,2,2]
        (
            [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],
            [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 4, 1]]
        ),  # Expected: [2,3,2,1]
        (
            [[1, 1]],
            [[0, 0, 1], [1, 1, 1], [2, 2, 1]]
        )   # Expected: [0,1,0]
    ]

    for i, (points, queries) in enumerate(test_cases):
        result = solution.countPoints(points, queries)
        print(f"Test case {i + 1}:")
        print(f"Points: {points}")
        print("Queries:")
        for j, (x, y, r) in enumerate(queries):
            print(f"  Circle {j+1}: center=({x},{y}), radius={r}")
            print(f"  Points inside: {result[j]}")
        print()
