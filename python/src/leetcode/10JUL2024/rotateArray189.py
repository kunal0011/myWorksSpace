from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # In case k is greater than n

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


# Example usage
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
sol = Solution()
sol.rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
