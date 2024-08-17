from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        result = []
        dq = deque()  # Will store indices of the elements

        for i in range(len(nums)):
            # Remove elements out of the current window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove elements smaller than the current element from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add current element index to the deque
            dq.append(i)

            # Append the current max (from the front of the deque) to the result
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
