from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        l = []

        def backtrack(index: int) -> None:

            if index == n:
                l.append(nums[:])
                return None

            for i in range(index, n):
                nums[index], nums[i] = nums[i], nums[index]
                backtrack(index+1)
                nums[index], nums[i] = nums[i], nums[index]

        backtrack(0)
        return l
