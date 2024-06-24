from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If mid element is greater than the right element, the minimum is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # If mid element is less than or equal to the right element, the minimum is in the left half
                right = mid

        # After the loop ends, left == right and points to the minimum element
        return nums[left]


# Example usage:
sol = Solution()
print(sol.findMin([4, 5, 6, 7, 0, 1, 2]))  # Output: 0
print(sol.findMin([0, 1, 2, 4, 5, 6, 7]))  # Output: 0
print(sol.findMin([2, 3, 4, 5, 1]))        # Output: 1
print(sol.findMin([3, 4, 5, 1, 2]))        # Output: 1
