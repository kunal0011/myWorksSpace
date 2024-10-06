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
