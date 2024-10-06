class Solution:
    def largestRectangleArea(self, heights) -> int:
        # Stack to store indices
        stack = []
        max_area = 0
        # Append a 0 height at the end to flush out the remaining heights
        heights.append(0)

        for i in range(len(heights)):
            # Pop from stack while the current height is smaller than the height of the bar at stack's top
            while stack and heights[i] < heights[stack[-1]]:
                # Get the height of the bar at the top of the stack
                h = heights[stack.pop()]
                # Calculate the width of the rectangle
                width = i if not stack else i - stack[-1] - 1
                # Calculate the area and update max_area
                max_area = max(max_area, h * width)

            # Push current bar's index to the stack
            stack.append(i)

        return max_area

# Test cases


def test_largest_rectangle_area():
    solution = Solution()

    # Test case 1
    heights1 = [2, 1, 5, 6, 2, 3]
    # The largest rectangle can be formed by the heights [5, 6] with area 5*2 = 10.
    expected_result_1 = 10
    assert solution.largestRectangleArea(
        heights1) == expected_result_1, "Test case 1 failed"

    # Test case 2
    heights2 = [2, 4]
    # The largest rectangle is the single bar of height 4.
    expected_result_2 = 4
    assert solution.largestRectangleArea(
        heights2) == expected_result_2, "Test case 2 failed"

    # Test case 3
    heights3 = [1, 1, 1, 1, 1]
    # The largest rectangle is formed by the entire width.
    expected_result_3 = 5
    assert solution.largestRectangleArea(
        heights3) == expected_result_3, "Test case 3 failed"

    print("All test cases passed!")


# Run the tests
test_largest_rectangle_area()
