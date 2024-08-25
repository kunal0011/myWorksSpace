from typing import List


class Solution:

    def maxRotateFunction(self, nums: List[int]):
        n = len(nums)
        sum_nums = sum(nums)
        F = sum(i * num for i, num in enumerate(nums))

        max_value = F
        for k in range(1, n):
            F += sum_nums - n * nums[-k]
            max_value = max(max_value, F)

        return max_value

# Example usage:
# nums = [4, 3, 2, 6]
# print(maxRotateFunction(nums))  # Output: 26
