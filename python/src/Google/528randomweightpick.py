import random
import bisect


class Solution:

    def __init__(self, w):
        # Create a cumulative sum array
        self.prefix_sums = []
        cumulative_sum = 0
        for weight in w:
            cumulative_sum += weight
            self.prefix_sums.append(cumulative_sum)
        self.total_sum = cumulative_sum

    def pickIndex(self):
        # Generate a random number in the range [1, total_sum]
        target = random.randint(1, self.total_sum)

        # Use binary search to find the target within the prefix_sums array
        index = bisect.bisect_left(self.prefix_sums, target)
        return index
