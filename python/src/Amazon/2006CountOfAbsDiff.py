from collections import defaultdict


class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        count = 0
        freq_map = defaultdict(int)

        # Iterate through the array
        for num in nums:
            # Check for valid pairs with difference k
            count += freq_map[num - k]
            count += freq_map[num + k]

            # Update frequency map
            freq_map[num] += 1

        return count
