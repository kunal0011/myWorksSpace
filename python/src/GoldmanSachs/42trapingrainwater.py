from typing import List


class Solution:
    def trap(height):
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water_trapped += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water_trapped += right_max - height[right]
                right -= 1

        return water_trapped


def trap(height):
    stack = []
    water_trapped = 0
    current = 0

    while current < len(height):
        # While stack is not empty and the current height is greater than the height at the stack's top index
        while stack and height[current] > height[stack[-1]]:
            top = stack.pop()  # Get the top of the stack
            if not stack:
                break  # No left boundary

            # Distance between the current index and the new top of the stack
            distance = current - stack[-1] - 1
            bounded_height = min(
                height[current], height[stack[-1]]) - height[top]
            water_trapped += distance * bounded_height

        stack.append(current)
        current += 1

    return water_trapped
