from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)

        # Compute prefix sum array
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        # Deque to store indices of prefix_sum
        deq = deque()
        min_length = float('inf')

        for i in range(n + 1):
            # Ensure we maintain a valid subarray with sum at least k
            while deq and prefix_sum[i] - prefix_sum[deq[0]] >= k:
                min_length = min(min_length, i - deq.popleft())

            # Maintain deque increasing order by removing elements that are less useful
            while deq and prefix_sum[i] <= prefix_sum[deq[-1]]:
                deq.pop()

            deq.append(i)

        return min_length if min_length != float('inf') else -1
