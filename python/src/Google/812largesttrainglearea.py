"""
LeetCode 812: Largest Triangle Area

Problem Statement:
Given an array of points on the X-Y plane points where points[i] = [xi, yi],
return the area of the largest triangle that can be formed by any three different points.
Answers within 10^-5 of the actual answer will be accepted.

Logic:
1. Use combinations from itertools to generate all possible triplets of points
2. For each triplet, calculate triangle area using the formula:
   Area = |x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)| / 2
3. Keep track of maximum area found
4. Return the largest area

Time Complexity: O(n^3) where n is the number of points
Space Complexity: O(1) since we only store the maximum area
"""

from itertools import combinations
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(p1, p2, p3):
            return abs(p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2

        max_area = 0
        for p1, p2, p3 in combinations(points, 3):
            max_area = max(max_area, area(p1, p2, p3))
        return max_area


def test_largest_triangle_area():
    solution = Solution()

    # Test case 1: Basic triangle
    points1 = [[0, 0], [0, 1], [1, 0]]
    result1 = solution.largestTriangleArea(points1)
    expected1 = 0.5
    assert abs(
        result1 - expected1) < 1e-5, f"Test case 1 failed. Expected {expected1}, got {result1}"
    print(f"Test case 1 passed: points={points1}, area={result1}")

    # Test case 2: Multiple triangles
    points2 = [[0, 0], [0, 1], [1, 0], [1, 1]]
    result2 = solution.largestTriangleArea(points2)
    expected2 = 1.0
    assert abs(
        result2 - expected2) < 1e-5, f"Test case 2 failed. Expected {expected2}, got {result2}"
    print(f"\nTest case 2 passed: points={points2}, area={result2}")

    # Test case 3: Points in a line
    points3 = [[0, 0], [1, 1], [2, 2]]
    result3 = solution.largestTriangleArea(points3)
    expected3 = 0.0
    assert abs(
        result3 - expected3) < 1e-5, f"Test case 3 failed. Expected {expected3}, got {result3}"
    print(f"\nTest case 3 passed: points={points3}, area={result3}")

    # Test case 4: Negative coordinates
    points4 = [[-2, 0], [0, -2], [2, 0]]
    result4 = solution.largestTriangleArea(points4)
    expected4 = 4.0
    assert abs(
        result4 - expected4) < 1e-5, f"Test case 4 failed. Expected {expected4}, got {result4}"
    print(f"\nTest case 4 passed: points={points4}, area={result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_largest_triangle_area()
