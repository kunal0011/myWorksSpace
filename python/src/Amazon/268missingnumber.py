from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)  # Start with n, since the index stops at n-1
        for i in range(len(nums)):
            # XOR the index and the value at that index
            missing ^= i ^ nums[i]
        return missing
