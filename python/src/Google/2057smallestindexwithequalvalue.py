class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        for i, num in enumerate(nums):
            if i % 10 == num:
                return i
        return -1
