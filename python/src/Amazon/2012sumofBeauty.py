class Solution:
    def sumOfBeauties(self, nums: list[int]) -> int:
        n = len(nums)

        # Create leftMax and rightMin arrays
        leftMax = [0] * n
        rightMin = [0] * n

        leftMax[0] = nums[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], nums[i])

        rightMin[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            rightMin[i] = min(rightMin[i + 1], nums[i])

        sumOfBeauty = 0

        # Calculate the sum of beauty
        for i in range(1, n - 1):
            if leftMax[i - 1] < nums[i] < rightMin[i + 1]:
                sumOfBeauty += 2
            elif nums[i - 1] < nums[i] and nums[i] < nums[i + 1]:
                sumOfBeauty += 1

        return sumOfBeauty
