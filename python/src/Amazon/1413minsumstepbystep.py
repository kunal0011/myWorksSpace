from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        current_sum = 0
        min_sum = 0

        for num in nums:
            current_sum += num
            min_sum = min(min_sum, current_sum)

        return -min_sum + 1


# Testing
solution = Solution()
nums = [1, -2, -3]
print("Python Test Result:", solution.minStartValue(nums))  # Output should be 5
