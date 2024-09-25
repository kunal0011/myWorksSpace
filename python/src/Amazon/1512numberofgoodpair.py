from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = defaultdict(int)  # To count the occurrences of each number
        good_pairs = 0

        # Iterate over the array
        for num in nums:
            # If this number has been seen `count[num]` times, we can form `count[num]` new pairs
            good_pairs += count[num]
            # Increment the count for this number
            count[num] += 1

        return good_pairs
