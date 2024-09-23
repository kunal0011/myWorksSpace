from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: -1}
        current_sum = 0
        max_len = 0

        for i, num in enumerate(nums):
            current_sum += num
            if current_sum - k in prefix_sum:
                max_len = max(max_len, i - prefix_sum[current_sum - k])
            if current_sum not in prefix_sum:
                prefix_sum[current_sum] = i

        return max_len
