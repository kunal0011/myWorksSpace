from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        def firstElement(nums, target) -> int:
            nonlocal left
            nonlocal right

            while left <= right:
                mid = (left + right) // 2
                if mid == 0 and nums[mid] == target:
                    return mid
                elif mid >= 1 and nums[mid] == target and nums[mid - 1] != target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid-1
            return -1

        def lastElement(nums, target) -> int:
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if mid == len(nums)-1 and nums[mid] == target:
                    return mid
                elif mid <= len(nums)-2 and nums[mid] == target and nums[mid + 1] != target:
                    return mid
                # elif mid+1 >= len(nums) and nums[mid] == target:
                #     return mid
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    left = mid+1
            return -1
        x = firstElement(nums, target)
        y = lastElement(nums, target)
        return [x, y]


class Solution1:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeftmost(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def findRightmost(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        leftmost = findLeftmost(nums, target)
        rightmost = findRightmost(nums, target)

        if leftmost <= rightmost < len(nums) and nums[leftmost] == target and nums[rightmost] == target:
            return [leftmost, rightmost]
        else:
            return [-1, -1]


if __name__ == "__main__":
    s = Solution1()
    # print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
    print(s.searchRange([1, 1, 2], 1))
