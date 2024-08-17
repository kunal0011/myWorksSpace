from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(houses):
            rob1, rob2 = 0, 0
            for amount in houses:
                new_rob = max(rob2, rob1 + amount)
                rob1 = rob2
                rob2 = new_rob
            return rob2

        if len(nums) == 1:
            return nums[0]

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
