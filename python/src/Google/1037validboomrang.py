"""
LeetCode 1037: Valid Boomerang

Problem Statement:
Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, 
return true if these points are a boomerang. A boomerang is a set of three points that are 
all distinct and not in a straight line.

Logic:
1. For three points to form a boomerang:
   - They must not be the same points (distinct)
   - They must not lie on a straight line (non-collinear)
2. Check collinearity using slope formula:
   - (y2-y1)/(x2-x1) != (y3-y1)/(x3-x1)
   - Cross multiply to avoid division by zero:
   - (y2-y1)(x3-x1) != (y3-y1)(x2-x1)
3. If equation is true, points form a boomerang

Time Complexity: O(1) constant time as always 3 points
Space Complexity: O(1) constant space
"""

from typing import List


class Solution:
    def isBoomerang(self, points: list[list[int]]) -> bool:
        (x1, y1), (x2, y2), (x3, y3) = points
        return (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1)


def test_is_boomerang():
    solution = Solution()

    # Test case 1: Valid boomerang
    points1 = [[1, 1], [2, 3], [3, 2]]
    result1 = solution.isBoomerang(points1)
    assert result1 == True, f"Test case 1 failed. Expected True, got {result1}"
    print(f"Test case 1 passed: points={points1}, is_boomerang={result1}")

    # Test case 2: Points in straight line
    points2 = [[1, 1], [2, 2], [3, 3]]
    result2 = solution.isBoomerang(points2)
    assert result2 == False, f"Test case 2 failed. Expected False, got {result2}"
    print(f"\nTest case 2 passed: points={points2}, is_boomerang={result2}")

    # Test case 3: Same points
    points3 = [[1, 1], [1, 1], [2, 2]]
    result3 = solution.isBoomerang(points3)
    assert result3 == False, f"Test case 3 failed. Expected False, got {result3}"
    print(f"\nTest case 3 passed: points={points3}, is_boomerang={result3}")

    # Test case 4: Points with zero difference
    points4 = [[0, 0], [1, 1], [0, 0]]
    result4 = solution.isBoomerang(points4)
    assert result4 == False, f"Test case 4 failed. Expected False, got {result4}"
    print(f"\nTest case 4 passed: points={points4}, is_boomerang={result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_is_boomerang()
