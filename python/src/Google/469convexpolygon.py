"""
LeetCode 469: Convex Polygon

Problem Statement:
You are given an array of points on the X-Y plane points where points[i] = [xi, yi].
Return true if the points form a convex polygon, and false otherwise.

A polygon is convex if all its internal angles are less than 180 degrees.
For this problem, we'll determine if a polygon is convex by checking if all turns are in 
the same direction (all clockwise or all counterclockwise).

Constraints:
- 3 <= points.length <= 10^4
- points[i].length == 2
- -10^4 <= xi, yi <= 10^4
- All the given points are unique
"""


def isConvex(points: list[list[int]]) -> bool:
    def cross_product(p1: list[int], p2: list[int], p3: list[int]) -> int:
        # Calculate cross product to determine turn direction
        # (x2-x1)(y3-y1) - (y2-y1)(x3-x1)
        return ((p2[0] - p1[0]) * (p3[1] - p1[1])) - ((p2[1] - p1[1]) * (p3[0] - p1[0]))

    n = len(points)
    if n < 3:
        return False

    # Initialize previous sign as None
    prev_sign = 0

    # Check each triplet of consecutive points
    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]
        p3 = points[(i + 2) % n]

        # Calculate cross product
        cp = cross_product(p1, p2, p3)

        # Skip if collinear
        if cp == 0:
            continue

        # Get current sign
        curr_sign = 1 if cp > 0 else -1

        # If previous sign exists and differs from current
        if prev_sign != 0 and curr_sign != prev_sign:
            return False

        prev_sign = curr_sign

    return True

# Test driver


def run_tests():
    test_cases = [
        {
            "points": [[0, 0], [0, 1], [1, 1], [1, 0]],
            "expected": True,
            "explanation": "Square - all angles are 90 degrees"
        },
        {
            "points": [[0, 0], [0, 2], [1, 1], [2, 2], [2, 0]],
            "expected": False,
            "explanation": "Not convex - has an internal angle > 180 degrees"
        },
        {
            "points": [[0, 0], [1, 0], [2, 1], [1, 2], [0, 2]],
            "expected": True,
            "explanation": "Pentagon - all internal angles < 180 degrees"
        },
        {
            "points": [[0, 0], [2, 0], [2, 2], [0, 2]],
            "expected": True,
            "explanation": "Rectangle - all angles are 90 degrees"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = isConvex(test["points"])
        status = "PASSED" if result == test["expected"] else "FAILED"
        print(f"Test {i}: {status}")
        print(f"Points: {test['points']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"Explanation: {test['explanation']}\n")


if __name__ == "__main__":
    print("Running test cases for Convex Polygon problem:\n")
    run_tests()

"""
Solution Logic Explanation:

1. Key Insight:
   - A polygon is convex if all turns go in the same direction
   - Use cross product to determine turn direction:
     * Positive = counterclockwise turn
     * Negative = clockwise turn
     * Zero = collinear points

2. Algorithm Steps:
   - For each consecutive triplet of points:
     * Calculate cross product
     * Skip if points are collinear (cross product = 0)
     * Check if turn direction matches previous turns
     * If directions differ, polygon is not convex

3. Time and Space Complexity:
   - Time: O(n) where n is number of points
   - Space: O(1) only need few variables

4. Edge Cases Handled:
   - Less than 3 points
   - Collinear points
   - Polygon closing back to first point
"""
