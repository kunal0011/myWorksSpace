from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # Sort the array
        nums.sort()

        # Find the starting and ending index of the target
        result = []
        for i, num in enumerate(nums):
            if num == target:
                result.append(i)

        return result
