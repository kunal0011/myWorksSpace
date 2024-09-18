from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], K: int) -> int:
        # Sort the array to prioritize the smallest elements for negation
        nums.sort()

        # Negate the negative elements as much as we can
        for i in range(len(nums)):
            if nums[i] < 0 and K > 0:
                nums[i] = -nums[i]
                K -= 1

        # If K is still odd, we need to negate the smallest element again
        if K % 2 == 1:
            nums.sort()  # Re-sort to find the smallest element
            nums[0] = -nums[0]

        # Return the sum of the array
        return sum(nums)


# Testing
solution = Solution()
nums = [4, 2, 3]
K = 1
print("Python Test Result:", solution.largestSumAfterKNegations(nums, K))  # Output: 5
