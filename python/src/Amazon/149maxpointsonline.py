"""
LeetCode 149. Max Points on a Line

Problem Statement:
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
return the maximum number of points that lie on the same straight line.

Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Explanation: All points lie on the line y = x.

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation: The line through points [1,1], [4,1] contains 4 points.

Constraints:
- 1 <= points.length <= 300
- points[i].length == 2
- -10^4 <= xi, yi <= 10^4
- All the points are unique
"""

from typing import List, Dict, Tuple
from collections import defaultdict
from math import gcd


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        n = len(points)
        if n <= 2:
            return n

        def get_slope(p1: List[int], p2: List[int]) -> Tuple[int, int]:
            """Helper function to get slope in reduced form."""
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]

            if dx == 0:
                return (0, 1)  # Vertical line
            if dy == 0:
                return (1, 0)  # Horizontal line

            d = gcd(dx, dy)
            return (dx // d, dy // d)

        max_points = 2
        for i in range(n):
            slopes = defaultdict(int)
            for j in range(n):
                if i != j:
                    slope = get_slope(points[i], points[j])
                    slopes[slope] += 1

            if slopes:
                max_points = max(max_points, max(slopes.values()) + 1)

        return max_points

    def maxPointsWithDetails(self, points: List[List[int]]) -> Tuple[int, List[List[int]], Dict]:
        """
        Returns maximum points, points on the line, and slope information.
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        n = len(points)
        if n <= 2:
            return n, points, {}

        def get_slope(p1: List[int], p2: List[int]) -> Tuple[int, int]:
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]

            if dx == 0:
                return (0, 1)
            if dy == 0:
                return (1, 0)

            d = gcd(dx, dy)
            return (dx // d, dy // d)

        max_points = 2
        max_slope = None
        max_base_point = None
        all_slopes = {}

        for i in range(n):
            slopes = defaultdict(list)
            for j in range(n):
                if i != j:
                    slope = get_slope(points[i], points[j])
                    slopes[slope].append(points[j])

            for slope, points_on_line in slopes.items():
                points_on_line.append(points[i])
                count = len(points_on_line)
                all_slopes[(points[i][0], points[i][1], slope)
                           ] = points_on_line

                if count > max_points:
                    max_points = count
                    max_slope = slope
                    max_base_point = points[i]

        # Get points on the line with maximum points
        result_points = []
        if max_base_point and max_slope:
            result_points = all_slopes[(
                max_base_point[0], max_base_point[1], max_slope)]

        return max_points, result_points, all_slopes


def visualize_points(points: List[List[int]], line_points: List[List[int]] = None) -> None:
    """Helper function to visualize points and line."""
    import matplotlib.pyplot as plt

    # Extract x and y coordinates
    x = [p[0] for p in points]
    y = [p[1] for p in points]

    plt.figure(figsize=(10, 10))
    plt.scatter(x, y, color='blue', label='Points')

    if line_points:
        line_x = [p[0] for p in line_points]
        line_y = [p[1] for p in line_points]
        plt.scatter(line_x, line_y, color='red', label='Points on max line')

        # Draw line through points
        if len(line_points) >= 2:
            plt.plot(line_x, line_y, 'r--', alpha=0.5)

    plt.grid(True)
    plt.legend()
    plt.title('Points Distribution')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axis('equal')
    plt.show()


def test_max_points():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "points": [[1, 1], [2, 2], [3, 3]],
            "expected": 3,
            "description": "Points on y=x"
        },
        {
            "points": [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]],
            "expected": 4,
            "description": "Complex arrangement"
        },
        {
            "points": [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],
            "expected": 5,
            "description": "All points on one line"
        },
        {
            "points": [[1, 1]],
            "expected": 1,
            "description": "Single point"
        },
        {
            "points": [[1, 1], [2, 2]],
            "expected": 2,
            "description": "Two points"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print(f"Points: {test_case['points']}")

        # Test both implementations
        result1 = solution.maxPoints(test_case['points'])
        result2, line_points, slopes = solution.maxPointsWithDetails(
            test_case['points'])

        print(f"\nResults:")
        print(f"Maximum points on a line: {result1}")
        print(f"Points on the line: {line_points}")

        # Visualize points
        visualize_points(test_case['points'], line_points)

        assert result1 == test_case['expected'], \
            f"Basic approach failed. Expected {test_case['expected']}, got {result1}"
        assert result2 == test_case['expected'], \
            f"Detailed approach failed. Expected {test_case['expected']}, got {result2}"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_max_points()
