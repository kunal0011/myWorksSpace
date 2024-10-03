from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Check if the middle element is the target
            if nums[mid] == target:
                return True

            # If we can't be sure about the halves due to duplicates, move the left pointer
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            # Check if the left half is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, the right half must be sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
