class Solution:
    def sortedSquares(self, nums):
        # Initialize two pointers
        left, right = 0, len(nums) - 1
        result = [0] * len(nums)  # Result array of the same size as nums
        position = len(nums) - 1  # Position to fill from the end

        # Two-pointer approach
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[position] = nums[left] ** 2
                left += 1
            else:
                result[position] = nums[right] ** 2
                right -= 1
            position -= 1

        return result
