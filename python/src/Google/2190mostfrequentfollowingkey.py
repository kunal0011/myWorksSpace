from collections import defaultdict


class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        freq_map = defaultdict(int)

        # Iterate through nums and check the pair (key, target)
        for i in range(len(nums) - 1):
            if nums[i] == key:
                target = nums[i + 1]
                freq_map[target] += 1

        # Find the target with the highest frequency
        most_frequent_target = -1
        max_count = 0
        for target, count in freq_map.items():
            if count > max_count or (count == max_count and target < most_frequent_target):
                most_frequent_target = target
                max_count = count

        return most_frequent_target
