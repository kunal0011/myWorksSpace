from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Dictionary to store the first occurrence of each prefix sum
        prefix_sum_map = {0: -1}
        max_len = 0
        prefix_sum = 0

        for i, num in enumerate(nums):
            # Treat 0 as -1, 1 as +1
            if num == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            # If this prefix sum has been seen before
            if prefix_sum in prefix_sum_map:
                # Calculate the length of the subarray
                max_len = max(max_len, i - prefix_sum_map[prefix_sum])
            else:
                # Otherwise, store the index of the first occurrence of this prefix sum
                prefix_sum_map[prefix_sum] = i

        return max_len
