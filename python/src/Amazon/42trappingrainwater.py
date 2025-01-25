from typing import List

"""
LeetCode 42. Trapping Rain Water

Problem Statement:
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The elevation map is shown above. The blue section represents trapped water.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        # Initialize pointers and variables
        left, right = 0, len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water_trapped = 0

        # Use two pointers to scan from both ends
        while left < right:
            if height[left] < height[right]:
                # If current height is less than left_max, water can be trapped
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water_trapped += left_max - height[left]
                left += 1
            else:
                # If current height is less than right_max, water can be trapped
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water_trapped += right_max - height[right]
                right -= 1

        return water_trapped


def explain_solution(height: List[int]) -> None:
    """
    Function to explain the trapping water calculation step by step
    """
    print(f"\nCalculating trapped water for heights: {height}")
    print("=" * 50)

    if not height:
        print("Empty array, no water can be trapped")
        return 0

    left, right = 0, len(height) - 1
    left_max = height[left]
    right_max = height[right]
    water_trapped = 0

    print("\nUsing two pointer approach:")
    print(f"Initial state: left={left}, right={right}")
    print(f"Initial max heights: left_max={left_max}, right_max={right_max}")

    while left < right:
        print(f"\nCurrent pointers: left={left}, right={right}")
        print(
            f"Current max heights: left_max={left_max}, right_max={right_max}")

        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
                print(f"Updated left_max to {left_max}")
            else:
                trapped = left_max - height[left]
                water_trapped += trapped
                print(f"Trapped {trapped} units at position {left}")
            left += 1
            print(f"Moving left pointer to {left}")
        else:
            if height[right] >= right_max:
                right_max = height[right]
                print(f"Updated right_max to {right_max}")
            else:
                trapped = right_max - height[right]
                water_trapped += trapped
                print(f"Trapped {trapped} units at position {right}")
            right -= 1
            print(f"Moving right pointer to {right}")

    print(f"\nTotal water trapped: {water_trapped}")
    return water_trapped


def test_trap():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "height": [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
            "expected": 6,
            "description": "Standard case with multiple traps"
        },
        {
            "height": [4, 2, 0, 3, 2, 5],
            "expected": 9,
            "description": "Case with deep valley"
        },
        {
            "height": [1, 2, 3, 4, 5],
            "expected": 0,
            "description": "Monotonic increasing - no water trapped"
        },
        {
            "height": [5, 4, 3, 2, 1],
            "expected": 0,
            "description": "Monotonic decreasing - no water trapped"
        },
        {
            "height": [],
            "expected": 0,
            "description": "Empty array"
        },
        {
            "height": [1],
            "expected": 0,
            "description": "Single element"
        },
        {
            "height": [1, 0, 1],
            "expected": 1,
            "description": "Simple trap"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        height = test_case["height"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: height = {height}")

        result = solution.trap(height.copy())

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_trap()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_solution([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
        explain_solution([4, 2, 0, 3, 2, 5])
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
