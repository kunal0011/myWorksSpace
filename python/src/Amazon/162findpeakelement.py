from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                # If mid is greater than mid + 1, a peak is in the left half
                right = mid
            else:
                # If mid is less than mid + 1, a peak is in the right half
                left = mid + 1

        # At the end of the loop, left == right and points to a peak element
        return left
