"""
LeetCode 452: Minimum Number of Arrows to Burst Balloons

Problem Statement:
There are some spherical balloons spread in two-dimensional space. For each balloon, 
provided input is the start and end coordinates of the horizontal diameter.

An arrow can be shot up exactly vertically from different points along the x-axis.
A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend.
There is no limit to the number of arrows that can be shot.
A shot arrow keeps traveling up infinitely.

Return the minimum number of arrows that must be shot to burst all balloons.

Constraints:
- 1 <= points.length <= 10^5
- points[i].length == 2
- -2^31 <= xstart < xend <= 2^31 - 1
"""


def findMinArrowShots(points: list[list[int]]) -> int:
    if not points:
        return 0

    # Sort by end points
    points.sort(key=lambda x: x[1])

    arrows = 1
    current_end = points[0][1]

    # Check each balloon
    for start, end in points[1:]:
        # If current balloon starts after previous end,
        # need new arrow
        if start > current_end:
            arrows += 1
            current_end = end

    return arrows

# Test driver


def run_tests():
    test_cases = [
        {
            "points": [[10, 16], [2, 8], [1, 6], [7, 12]],
            "expected": 2,
            "explanation": "One arrow at x=6 bursts [2,8],[1,6], another at x=11 bursts [10,16],[7,12]"
        },
        {
            "points": [[1, 2], [3, 4], [5, 6], [7, 8]],
            "expected": 4,
            "explanation": "Each balloon needs its own arrow"
        },
        {
            "points": [[1, 2], [2, 3], [3, 4], [4, 5]],
            "expected": 2,
            "explanation": "Two arrows can burst all balloons"
        },
        {
            "points": [[1, 5], [2, 3], [3, 4], [4, 5]],
            "expected": 2,
            "explanation": "Two overlapping groups of balloons"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = findMinArrowShots(test["points"])
        status = "PASSED" if result == test["expected"] else "FAILED"
        print(f"Test {i}: {status}")
        print(f"Balloon intervals: {test['points']}")
        print(f"Expected arrows: {test['expected']}")
        print(f"Got: {result}")
        print(f"Explanation: {test['explanation']}\n")


if __name__ == "__main__":
    print("Running test cases for Minimum Number of Arrows problem:\n")
    run_tests()

"""
Solution Logic Explanation:

1. Key Insight:
   - Sort balloons by end coordinate
   - Greedy approach: shoot arrow at earliest possible position
   - Each arrow can burst multiple overlapping balloons

2. Algorithm Steps:
   - Sort balloons by end points
   - Track current arrow position at first balloon's end
   - For each subsequent balloon:
     * If starts after current arrow, need new arrow
     * Otherwise, can use same arrow

3. Optimizations:
   - Sort by end point rather than start point
   - Only need to track end points
   - No need to track actual arrow positions

Time Complexity: O(n log n) for sorting
Space Complexity: O(1) excluding input space
"""
