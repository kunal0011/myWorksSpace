from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # First pass: Calculate prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Second pass: Calculate suffix products and multiply with prefix products
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


# Example usage:
nums = [1, 2, 3, 4]
solution = Solution()
print(solution.productExceptSelf(nums))  # Output: [24, 12, 8, 6]
