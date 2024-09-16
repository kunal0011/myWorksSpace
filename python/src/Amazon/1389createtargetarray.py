from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for num, idx in zip(nums, index):
            target.insert(idx, num)
        return target


# Testing
solution = Solution()
nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]
print("Python Test Result:", solution.createTargetArray(
    nums, index))  # Output should be [0, 4, 1, 3, 2]
