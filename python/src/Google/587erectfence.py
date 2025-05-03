"""
LeetCode 587 - Erect the Fence

You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.
You are asked to fence all the trees within the minimum area possible. Return the coordinates of trees 
that make up the perimeter of the fence (in any order).

Logic:
1. Use Graham Scan algorithm (Convex Hull):
   - Sort points by x-coordinate (and y if x is same)
   - Build lower hull (bottom part of fence)
   - Build upper hull (top part of fence)
   - Combine hulls to get perimeter points
2. Key idea: Use cross product to determine orientation of three points
   - Positive -> Counter-clockwise turn
   - Negative -> Clockwise turn
   - Zero -> Collinear

Time Complexity: O(n log n) for sorting
Space Complexity: O(n) for storing the hull
"""

from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # Helper function to calculate the orientation
        def orientation(p, q, r):
            # Return the cross product of vectors pq and qr
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        # Sort the points
        trees = sorted(trees)

        # Build the lower hull
        lower = []
        for p in trees:
            while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        # Build the upper hull
        upper = []
        for p in reversed(trees):
            while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        # Remove the last point of each half because it's repeated at the beginning of the other half
        return list(set(lower[:-1] + upper[:-1]))


def run_test_cases():
    solution = Solution()
    test_cases = [
        {
            "trees": [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]],
            "expected": [[1, 1], [2, 0], [4, 2], [3, 3], [2, 4]],
            "explanation": "All trees need to be fenced and form a pentagon"
        },
        {
            "trees": [[1, 2], [2, 2], [4, 2]],
            "expected": [[1, 2], [2, 2], [4, 2]],
            "explanation": "All trees are collinear along y=2"
        },
        {
            "trees": [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2], [4, 1]],
            "expected": [[1, 1], [2, 0], [4, 1], [4, 2], [3, 3], [2, 4]],
            "explanation": "Complex case with multiple points"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.outerTrees(test["trees"])
        # Convert to set of tuples for comparison (order doesn't matter)
        result_set = set(map(tuple, result))
        expected_set = set(map(tuple, test["expected"]))

        print(f"\nTest Case {i}:")
        print(f"Trees: {test['trees']}")
        print(f"Expected fence points: {test['expected']}")
        print(f"Got fence points: {result}")
        print(f"Explanation: {test['explanation']}")
        print(f"{'✓ Passed' if result_set == expected_set else '✗ Failed'}")


if __name__ == "__main__":
    run_test_cases()
