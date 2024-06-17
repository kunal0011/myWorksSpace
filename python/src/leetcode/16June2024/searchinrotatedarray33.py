from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1

        while left <= right:

            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif mid-1 > 0 and nums[mid-1] == target:
                return mid-1
            elif mid+1 < len(nums) and nums[mid+1] == target:
                return mid+1
            elif nums[left] <= nums[mid] and target >= nums[left] and target <= nums[mid]:
                right = mid - 1
            elif nums[right] >= nums[mid] and target >= nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                if nums[left] >= nums[mid]:
                    right = mid-1
                elif nums[mid] >= nums[right]:
                    left = mid+1
                else:
                    break

        return -1


class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Determine which part is sorted
            if nums[left] <= nums[mid]:
                # Left part is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right part is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


if __name__ == "__main__":
    s = Solution1()
    # print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
    # print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
    # print(s.search([1], 0))
    # print(s.search([1, 3, 5], 1))
    # print(s.search([1], 1))
    # print(s.search([1, 3, 5], 4))
    print(s.search([5, 1, 3], 5))
