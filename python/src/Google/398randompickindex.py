import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        result = -1

        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                # Replace the result with the current index with probability 1/count
                if random.randint(1, count) == 1:
                    result = i

        return result
