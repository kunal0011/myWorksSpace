from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # Convert the list of numbers to a set for O(1) average-time complexity lookups
        num_set = set(nums)

        # Continue updating original while it is found in the set
        while original in num_set:
            original *= 2

        return original
