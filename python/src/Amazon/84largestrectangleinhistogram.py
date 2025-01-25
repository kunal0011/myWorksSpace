"""
LeetCode 84. Largest Rectangle in Histogram

Problem Statement:
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The largest rectangle has area = 10 (height = 5, width = 2)

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
- 1 <= heights.length <= 105
- 0 <= heights[i] <= 104
"""


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # Add 0 at the end to handle remaining stack elements
        heights.append(0)
        stack = [-1]  # Stack to store indices
        max_area = 0

        for i in range(len(heights)):
            # While current height is smaller than height at stack top
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        # Remove the added 0
        heights.pop()
        return max_area


def visualize_histogram(heights: list[int], highlight_area: tuple = None) -> None:
    """Helper function to visualize histogram with optional area highlight"""
    max_height = max(heights)

    # Print histogram
    for h in range(max_height, 0, -1):
        print(f"{h:2d} |", end=" ")
        for bar in heights:
            if bar >= h:
                print("█", end=" ")
            else:
                print(" ", end=" ")
        print()

    # Print base line
    print("   +" + "-" * (len(heights) * 2))
    print("    ", end="")
    for i in range(len(heights)):
        print(i, end=" ")
    print()

    # Print highlight info if provided
    if highlight_area:
        start, end, height = highlight_area
        area = height * (end - start + 1)
        print(f"\nHighlighted area: {area}")
        print(f"Height: {height}")
        print(f"Width: {end - start + 1}")
        print(f"Range: [{start}, {end}]")


def test_largest_rectangle():
    solution = Solution()

    test_cases = [
        {
            "heights": [2, 1, 5, 6, 2, 3],
            "expected": 10,
            "description": "Standard case"
        },
        {
            "heights": [2, 4],
            "expected": 4,
            "description": "Two bars"
        },
        {
            "heights": [2, 1, 2],
            "expected": 3,
            "description": "Valley pattern"
        },
        {
            "heights": [1],
            "expected": 1,
            "description": "Single bar"
        },
        {
            "heights": [1, 1, 1, 1],
            "expected": 4,
            "description": "Equal heights"
        },
        {
            "heights": [5, 4, 3, 2, 1],
            "expected": 9,
            "description": "Decreasing heights"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        heights = test_case["heights"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"Heights: {heights}")
        visualize_histogram(heights)

        result = solution.largestRectangleArea(heights)

        assert result == expected, \
            f"Expected {expected}, but got {result}"
        print(f"✓ Test case passed! Largest area: {result}")


if __name__ == "__main__":
    test_largest_rectangle()
    print("\nAll test cases passed! 🎉")
