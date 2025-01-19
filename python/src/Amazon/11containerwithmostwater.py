"""
Problem 11: Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints 
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: 
- The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]
- The maximum area is obtained by choosing the 2nd and 8th lines (height[1] = 8 and height[8] = 7)
- Area = min(8, 7) * (8 - 1) = 7 * 7 = 49

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

Approach:
1. Use two pointers technique - left and right pointers at the ends
2. Calculate area = min(height[left], height[right]) * (right - left)
3. Move the pointer with smaller height inward
4. Keep track of maximum area seen so far
5. Continue until pointers meet

Time Complexity: O(n) - single pass through the array
Space Complexity: O(1) - constant extra space
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            # Calculate the area
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            max_water = max(max_water, current_area)

            # Move the pointers
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water


def test_container_with_most_water():
    solution = Solution()

    # Test cases: (heights, expected_result, description)
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49, "Example case with multiple heights"),
        ([1, 1], 1, "Minimum case with two heights"),
        ([4, 3, 2, 1, 4], 16, "Equal heights at ends"),
        ([1, 2, 4, 3], 4, "Small array case"),
        ([1, 8, 6, 2, 5, 4, 8, 25, 7], 49, "Case with very tall line"),
        ([1, 1, 1, 1, 1], 4, "Equal heights"),
        ([1, 2, 3, 4, 5, 6], 8, "Increasing heights"),
        ([6, 5, 4, 3, 2, 1], 8, "Decreasing heights"),
        ([0, 0], 0, "Zero heights"),
        ([10000, 1, 1, 1, 10000], 40000, "Maximum height case"),
    ]

    print("\nRunning Container With Most Water Tests:")
    print("=" * 50)

    passed = 0
    total = len(test_cases)

    for i, (heights, expected, desc) in enumerate(test_cases, 1):
        result = solution.maxArea(heights)
        status = "PASS" if result == expected else "FAIL"
        color = "\033[92m" if status == "PASS" else "\033[91m"

        print(f"\nTest Case {i}: {desc}")
        print(f"Heights: {heights}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Status: {color}{status}\033[0m")

        if result == expected:
            passed += 1

    print("\n" + "=" * 50)
    print(f"\nTest Summary:")
    print(f"Total Tests: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {total - passed}")
    success_rate = (passed / total) * 100
    print(f"Success Rate: {success_rate:.2f}%")


if __name__ == "__main__":
    test_container_with_most_water()
