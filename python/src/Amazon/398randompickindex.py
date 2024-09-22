import random
from collections import defaultdict


class RandomPickIndex:

    def __init__(self, nums: list[int]):
        self.indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)

    def pick(self, target: int) -> int:
        if target in self.indices:
            return random.choice(self.indices[target])
        return -1


# Example usage:
nums = [1, 2, 3, 3, 3]
random_picker = RandomPickIndex(nums)
print(random_picker.pick(3))  # Randomly output one of the indices 2, 3, or 4
print(random_picker.pick(1))  # Output: 0
print(random_picker.pick(4))  # Output: -1 (not found)
