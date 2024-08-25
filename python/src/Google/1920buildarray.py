from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # Initialize the result array
        ans = [0] * len(nums)

        # Fill in the result array based on the given rule
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]

        return ans


# Example usage
solution = Solution()
nums = [0, 2, 1, 5, 3, 4]
print(solution.buildArray(nums))  # Output: [0,1,2,4,5,3]
