from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Binary search to find the closest element
        left, right = 0, len(arr) - 1

        # Narrow the range to k elements
        while right - left >= k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1

        # Return the k closest elements, already sorted
        return arr[left:left + k]
